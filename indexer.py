"""
Hybrid Search Indexer:
1. Builds an inverted BM25 index with token frequencies and document lengths.
2. Generates 384-d dense vector embeddings using offline 'all-MiniLM-L6-v2'.
3. Creates restaurant and locality lookup tables for instant entity resolution.
"""

import json
import math
import os
import re
import pickle
from collections import defaultdict, Counter
import numpy as np
from bm25 import BM25Index

# Use local cache for SentenceTransformer
LOCAL_MODEL_PATH = os.path.expanduser(
    r"~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/1110a243fdf4706b3f48f1d95db1a4f5529b4d41"
)

def tokenize(text: str) -> list[str]:
    return [t for t in re.split(r"[^\w]+", text.lower()) if len(t) > 1]

def build_index(dataset_path: str, output_dir: str = "."):
    print(f"Loading dataset from {dataset_path}...")
    with open(dataset_path, "r", encoding="utf-8") as f:
        restaurants = json.load(f)

    flattened_dishes = []
    restaurant_catalog = {}
    known_localities = set()

    for rest in restaurants:
        r_id = rest["id"]
        r_name = rest["restaurant_name"]
        locality = rest["locality"]
        known_localities.add(locality)
        known_localities.add(locality.split()[0])  # e.g. "Koramangala" from "Koramangala 5th Block"

        restaurant_catalog[r_id] = {
            "id": r_id,
            "name": r_name,
            "locality": locality,
            "city": rest["city"],
            "coordinates": rest["coordinates"],
            "cuisines": rest["cuisines"],
            "rating": rest["aggregate_rating"],
            "rating_count": rest["popularity_votes"],
            "delivery_time_mins": rest["delivery_time_mins"],
            "distance_km": rest["distance_km"],
            "is_pure_veg": rest["is_pure_veg"],
            "discount_offer": rest.get("discount_offer", ""),
            "featured_image": rest.get("featured_image", "")
        }

        for dish in rest["menu_items"]:
            # Denormalized dish document
            doc = {
                "dish_id": dish["dish_id"],
                "name": dish["name"],
                "category": dish["category"],
                "description": dish["description"],
                "price": dish["price"],
                "is_veg": dish["is_veg"],
                "spicy_level": dish["spicy_level"],
                "dietary_tags": dish["dietary_tags"],
                "is_bestseller": dish.get("is_bestseller", False),
                "rating": dish["rating"],
                "rating_count": dish["rating_count"],
                "preparation_time_mins": dish["preparation_time_mins"],
                "calories_kcal": dish["calories_kcal"],
                "tags": dish["tags"],
                "ingredients": dish["ingredients"],
                "customizations": dish.get("customization_options", []),
                # Parent fields
                "restaurant_id": r_id,
                "restaurant_name": r_name,
                "locality": locality,
                "coordinates": rest["coordinates"],
                "restaurant_rating": rest["aggregate_rating"],
                "restaurant_votes": rest["popularity_votes"],
                "delivery_time_mins": rest["delivery_time_mins"],
                "distance_km": rest["distance_km"]
            }
            flattened_dishes.append(doc)

    print(f"Total flattened dishes to index: {len(flattened_dishes)}")

    # 1. Prepare BM25 Corpus
    print("Building BM25 Inverted Index...")
    corpus_tokens = []
    text_corpus_for_embeddings = []

    for d in flattened_dishes:
        # Weighted token sequence: name 3x, tags 2x, ingredients 2x, category, description, restaurant_name 2x
        weighted_text = (
            f"{d['name']} {d['name']} {d['name']} "
            f"{' '.join(d['tags'])} {' '.join(d['tags'])} "
            f"{' '.join(d['ingredients'])} {' '.join(d['ingredients'])} "
            f"{d['category']} {d['restaurant_name']} {d['restaurant_name']} "
            f"{d['description']} {d['locality']}"
        )
        tokens = tokenize(weighted_text)
        corpus_tokens.append(tokens)

        # Semantic representation text
        sem_text = (
            f"{d['name']} from {d['restaurant_name']}. Category: {d['category']}. "
            f"{d['description']} Key ingredients: {', '.join(d['ingredients'])}. "
            f"Diet: {', '.join(d['dietary_tags'])}."
        )
        text_corpus_for_embeddings.append(sem_text)

    bm25 = BM25Index()
    bm25.fit(corpus_tokens)

    # 2. Dense Embeddings via SentenceTransformer
    emb_file = os.path.join(output_dir, "dish_embeddings.npy")
    if os.path.exists(emb_file):
        print(f"Loading existing embeddings from {emb_file}...")
        embeddings = np.load(emb_file)
        print(f"Loaded embeddings shape: {embeddings.shape}")
    else:
        print(f"Loading local SentenceTransformer model from:\n{LOCAL_MODEL_PATH}")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(LOCAL_MODEL_PATH)
        print(f"Generating dense vector embeddings for {len(text_corpus_for_embeddings)} dishes...")
        embeddings = model.encode(text_corpus_for_embeddings, batch_size=128, show_progress_bar=True, normalize_embeddings=True)
        embeddings = np.array(embeddings, dtype=np.float32)
        print(f"Embeddings shape: {embeddings.shape}")
        np.save(emb_file, embeddings)
        print(f"Saved embeddings to {emb_file}")

    index_payload = {
        "flattened_dishes": flattened_dishes,
        "restaurant_catalog": restaurant_catalog,
        "known_restaurants": [r["name"] for r in restaurant_catalog.values()],
        "known_localities": sorted(list(known_localities)),
        "bm25": bm25
    }

    index_file = os.path.join(output_dir, "search_index.pkl")
    with open(index_file, "wb") as f:
        pickle.dump(index_payload, f)
    print(f"Saved inverted index and catalogs to {index_file}")
    print("Indexing complete!")

if __name__ == "__main__":
    build_index(r"d:\Search_Engine\food_delivery_search_dataset_100.json")
