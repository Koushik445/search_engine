"""
Conversational & Inclusive Food Delivery Search Engine
Implements Zomato's 2-Step Architecture:
  Step 1: Multi-Intent Natural Language Understanding & Hybrid Retrieval (BM25 + Dense Vectors)
  Step 2: Multi-Factor Re-Ranking & Cross-Entity Dish Bundling
"""

import os
import math
import pickle
import numpy as np
from typing import List, Dict, Any, Optional

import query_parser
from query_parser import ConversationalQueryParser, ParsedQuery
from bm25 import BM25Index

LOCAL_MODEL_PATH = os.path.expanduser(
    r"~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/1110a243fdf4706b3f48f1d95db1a4f5529b4d41"
)

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2.0)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(max(0.0, 1.0 - a)))
    return round(R * c, 2)

class AdvancedFoodSearchEngine:
    def __init__(self, index_dir: str = "."):
        self.index_dir = index_dir
        index_file = os.path.join(index_dir, "search_index.pkl")
        emb_file = os.path.join(index_dir, "dish_embeddings.npy")

        if not os.path.exists(index_file) or not os.path.exists(emb_file):
            raise FileNotFoundError(f"Missing index files in {index_dir}. Run indexer.py first.")

        print("Loading search index...")
        with open(index_file, "rb") as f:
            data = pickle.load(f)

        self.flattened_dishes = data["flattened_dishes"]
        self.restaurant_catalog = data["restaurant_catalog"]
        self.known_restaurants = data["known_restaurants"]
        self.known_localities = data["known_localities"]
        self.bm25 = data["bm25"]

        print("Loading dense vector embeddings...")
        self.dish_embeddings = np.load(emb_file)  # (N, 384)

        print("Initializing NLP query parser...")
        self.parser = ConversationalQueryParser(self.known_restaurants, self.known_localities)

        print("Loading SentenceTransformer model for runtime query encoding...")
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(LOCAL_MODEL_PATH)
        print("Search engine ready for live queries!")

    def _get_query_embedding(self, text: str) -> np.ndarray:
        emb = self.model.encode([text], normalize_embeddings=True)
        return emb[0]

    def _compute_single_dish_scores(self, dish_text: str, user_lat: float, user_lon: float, parsed: ParsedQuery) -> np.ndarray:
        """Computes hybrid dense+sparse score for all dishes."""
        tokens = query_parser.re.split(r"[^\w]+", dish_text.lower())
        tokens = [t for t in tokens if len(t) > 1]

        # 1. BM25 score
        bm25_raw = self.bm25.score(tokens)
        bm25_max = np.max(bm25_raw) if len(bm25_raw) > 0 and np.max(bm25_raw) > 0 else 1.0
        bm25_norm = bm25_raw / bm25_max

        # 2. Dense Semantic Cosine Similarity
        q_emb = self._get_query_embedding(dish_text)
        dense_sim = np.dot(self.dish_embeddings, q_emb)  # since both are unit-normalized
        dense_sim = np.clip(dense_sim, 0.0, 1.0)

        # 3. Hybrid blend
        hybrid = 0.55 * dense_sim + 0.45 * bm25_norm
        return hybrid

    def search(
        self,
        query: str,
        user_lat: float = 12.9352,
        user_lon: float = 77.6245,
        top_k: int = 10
    ) -> Dict[str, Any]:
        """
        Processes multi-intent natural language queries with conversational parsing,
        multi-dish bundling, and multi-factor ranking.
        """
        parsed = self.parser.parse(query)

        # Dispatch based on intent
        if parsed.intent_type == "MULTI_DISH" and len(parsed.target_dishes) >= 2:
            return self._handle_multi_dish_search(parsed, user_lat, user_lon, top_k)
        elif parsed.intent_type == "RESTAURANT_DISH" and parsed.target_restaurant:
            return self._handle_restaurant_dish_search(parsed, user_lat, user_lon, top_k)
        elif parsed.intent_type == "RESTAURANT_SEARCH" and parsed.target_restaurant:
            return self._handle_restaurant_only_search(parsed, user_lat, user_lon, top_k)
        elif parsed.intent_type == "RESTAURANT_CUISINE_SEARCH":
            return self._handle_restaurant_cuisine_search(parsed, user_lat, user_lon, top_k)
        else:
            return self._handle_standard_search(parsed, user_lat, user_lon, top_k)

    def _apply_hard_filters(self, dish: Dict[str, Any], parsed: ParsedQuery, user_lat: float, user_lon: float) -> Optional[float]:
        """Returns distance in km if passes all hard filters, otherwise None."""
        # 1. Vegetarian filter
        if parsed.is_veg is not None:
            if parsed.is_veg and not dish["is_veg"]:
                return None
            if not parsed.is_veg and dish["is_veg"] and parsed.is_veg is False:
                # If explicitly asked for non-veg
                pass

        # 2. Max Price filter
        if parsed.max_price is not None and dish["price"] > parsed.max_price:
            return None

        # 3. Locality filter
        if parsed.locality:
            loc_lower = parsed.locality.lower()
            if loc_lower not in dish["locality"].lower():
                return None

        # 4. Distance
        coords = dish["coordinates"]
        dist = haversine_distance(user_lat, user_lon, coords["latitude"], coords["longitude"])
        return dist

    def _handle_standard_search(self, parsed: ParsedQuery, user_lat: float, user_lon: float, top_k: int) -> Dict[str, Any]:
        target_text = parsed.target_dishes[0] if parsed.target_dishes else parsed.raw_query
        hybrid_scores = self._compute_single_dish_scores(target_text, user_lat, user_lon, parsed)

        # Enforce anchor keyword if present (e.g. "pizza" in "sabse sasta pizza", "burger" in "burger 150rs")
        anchor_nouns = {"pizza", "burger", "biryani", "coffee", "chai", "tea", "dosa", "idli", "shawarma", "pasta", "salad", "cake", "ice cream", "sushi", "ramen", "curry", "paneer"}
        q_tokens_set = set(query_parser.re.split(r"[^\w]+", target_text.lower()))
        required_anchors = anchor_nouns.intersection(q_tokens_set)

        results = []
        for doc_id, dish in enumerate(self.flattened_dishes):
            if required_anchors:
                dish_text_repr = f"{dish['name']} {dish['category']} {' '.join(dish['tags'])}".lower()
                if not any(a in dish_text_repr for a in required_anchors):
                    continue

            dist = self._apply_hard_filters(dish, parsed, user_lat, user_lon)
            if dist is None:
                continue

            base_score = float(hybrid_scores[doc_id])
            if base_score < 0.15:
                continue

            # Multi-factor re-ranking:
            # 1. Distance decay: 1 / (1 + 0.12 * dist)
            dist_factor = 1.0 / (1.0 + 0.12 * dist)

            # 2. Restaurant rating factor: (rating / 5.0)^1.5
            r_rating = dish["restaurant_rating"]
            rating_factor = (r_rating / 5.0) ** 1.5

            # 3. Bestseller boost
            bestseller_factor = 1.2 if dish.get("is_bestseller") else 1.0

            # 4. Dietary match boost
            health_factor = 1.2 if parsed.is_healthy and ("Salad" in dish["category"] or "Bowl" in dish["category"]) else 1.0

            final_score = base_score * dist_factor * rating_factor * bestseller_factor * health_factor

            results.append({
                "dish_id": dish["dish_id"],
                "dish_name": dish["name"],
                "category": dish["category"],
                "description": dish["description"],
                "price": dish["price"],
                "is_veg": dish["is_veg"],
                "spicy_level": dish["spicy_level"],
                "dietary_tags": dish["dietary_tags"],
                "rating": dish["rating"],
                "is_bestseller": dish["is_bestseller"],
                "calories_kcal": dish["calories_kcal"],
                "restaurant_id": dish["restaurant_id"],
                "restaurant_name": dish["restaurant_name"],
                "locality": dish["locality"],
                "restaurant_rating": dish["restaurant_rating"],
                "delivery_time_mins": dish["delivery_time_mins"],
                "distance_km": dist,
                "relevance_score": round(final_score, 4),
                "match_confidence": f"{int(min(99, max(50, final_score * 100)))}%"
            })

        # Apply sorting overrides if user requested "sabse sasta" or "near me"
        if parsed.sort_by == "price_asc":
            results.sort(key=lambda x: (x["price"], -x["relevance_score"]))
        elif parsed.sort_by == "distance_asc":
            results.sort(key=lambda x: (x["distance_km"], -x["relevance_score"]))
        elif parsed.sort_by == "rating_desc":
            results.sort(key=lambda x: (-x["restaurant_rating"], -x["relevance_score"]))
        else:
            results.sort(key=lambda x: -x["relevance_score"])

        return {
            "query": parsed.raw_query,
            "intent": parsed.intent_type,
            "explanation": parsed.explanation or "Semantic + lexical relevance search",
            "total_matches": len(results),
            "results": results[:top_k]
        }

    def _handle_restaurant_dish_search(self, parsed: ParsedQuery, user_lat: float, user_lon: float, top_k: int) -> Dict[str, Any]:
        target_rest = parsed.target_restaurant.lower()
        dish_text = parsed.target_dishes[0] if parsed.target_dishes else ""

        hybrid_scores = self._compute_single_dish_scores(dish_text or target_rest, user_lat, user_lon, parsed)

        results = []
        for doc_id, dish in enumerate(self.flattened_dishes):
            if target_rest not in dish["restaurant_name"].lower():
                continue

            dist = self._apply_hard_filters(dish, parsed, user_lat, user_lon)
            if dist is None:
                continue

            base_score = float(hybrid_scores[doc_id])
            dist_factor = 1.0 / (1.0 + 0.10 * dist)
            final_score = base_score * dist_factor

            results.append({
                "dish_id": dish["dish_id"],
                "dish_name": dish["name"],
                "category": dish["category"],
                "description": dish["description"],
                "price": dish["price"],
                "is_veg": dish["is_veg"],
                "spicy_level": dish["spicy_level"],
                "dietary_tags": dish["dietary_tags"],
                "rating": dish["rating"],
                "is_bestseller": dish["is_bestseller"],
                "restaurant_id": dish["restaurant_id"],
                "restaurant_name": dish["restaurant_name"],
                "locality": dish["locality"],
                "restaurant_rating": dish["restaurant_rating"],
                "delivery_time_mins": dish["delivery_time_mins"],
                "distance_km": dist,
                "relevance_score": round(final_score, 4)
            })

        results.sort(key=lambda x: -x["relevance_score"])
        return {
            "query": parsed.raw_query,
            "intent": parsed.intent_type,
            "target_restaurant": parsed.target_restaurant,
            "explanation": f"Filtered to {parsed.target_restaurant} with dish relevance for '{dish_text}'",
            "total_matches": len(results),
            "results": results[:top_k]
        }

    def _handle_restaurant_only_search(self, parsed: ParsedQuery, user_lat: float, user_lon: float, top_k: int) -> Dict[str, Any]:
        target_rest = parsed.target_restaurant.lower()
        matches = []

        for r_id, rest in self.restaurant_catalog.items():
            if target_rest in rest["name"].lower():
                coords = rest["coordinates"]
                dist = haversine_distance(user_lat, user_lon, coords["latitude"], coords["longitude"])
                matches.append({
                    "restaurant_id": r_id,
                    "restaurant_name": rest["name"],
                    "locality": rest["locality"],
                    "cuisines": rest["cuisines"],
                    "rating": rest["rating"],
                    "rating_count": rest["rating_count"],
                    "delivery_time_mins": rest["delivery_time_mins"],
                    "distance_km": dist,
                    "discount_offer": rest["discount_offer"],
                    "is_pure_veg": rest["is_pure_veg"]
                })

        matches.sort(key=lambda x: x["distance_km"])
        return {
            "query": parsed.raw_query,
            "intent": parsed.intent_type,
            "explanation": f"Found matching restaurant outlets for '{parsed.target_restaurant}'",
            "total_matches": len(matches),
            "results": matches[:top_k]
        }

    def _handle_restaurant_cuisine_search(self, parsed: ParsedQuery, user_lat: float, user_lon: float, top_k: int) -> Dict[str, Any]:
        term = parsed.target_dishes[0].lower() if parsed.target_dishes else ""
        matches = []

        for r_id, rest in self.restaurant_catalog.items():
            cuisines_text = " ".join(rest["cuisines"]).lower()
            name_text = rest["name"].lower()

            # Check if restaurant serves this cuisine or dish category
            has_match = (
                term in cuisines_text
                or term in name_text
                or any(term in dish["name"].lower() or term in dish["tags"] for dish in self.flattened_dishes if dish["restaurant_id"] == r_id)
            )

            if has_match:
                coords = rest["coordinates"]
                dist = haversine_distance(user_lat, user_lon, coords["latitude"], coords["longitude"])
                if parsed.locality and parsed.locality.lower() not in rest["locality"].lower():
                    continue

                matches.append({
                    "restaurant_id": r_id,
                    "restaurant_name": rest["name"],
                    "locality": rest["locality"],
                    "cuisines": rest["cuisines"],
                    "rating": rest["rating"],
                    "rating_count": rest["rating_count"],
                    "delivery_time_mins": rest["delivery_time_mins"],
                    "distance_km": dist,
                    "discount_offer": rest["discount_offer"],
                    "is_pure_veg": rest["is_pure_veg"]
                })

        # Sort by distance (since "near me" is commonly asked) or rating
        if parsed.sort_by == "rating_desc":
            matches.sort(key=lambda x: -x["rating"])
        else:
            matches.sort(key=lambda x: x["distance_km"])

        return {
            "query": parsed.raw_query,
            "intent": "OUTLET_SEARCH",
            "explanation": f"Discovered restaurant outlets specializing in '{term}'",
            "total_matches": len(matches),
            "results": matches[:top_k]
        }

    def _handle_multi_dish_search(self, parsed: ParsedQuery, user_lat: float, user_lon: float, top_k: int) -> Dict[str, Any]:
        """
        Zomato-style Multiple Dish Search:
        When a customer searches 'Chai and samosa' or 'Burger with cold drink',
        find restaurants that can fulfill BOTH dishes in a single delivery!
        """
        dish1_query = parsed.target_dishes[0]
        dish2_query = parsed.target_dishes[1]

        scores1 = self._compute_single_dish_scores(dish1_query, user_lat, user_lon, parsed)
        scores2 = self._compute_single_dish_scores(dish2_query, user_lat, user_lon, parsed)

        # Group matches by restaurant
        rest_dish1_candidates = {}
        rest_dish2_candidates = {}

        for doc_id, dish in enumerate(self.flattened_dishes):
            dist = self._apply_hard_filters(dish, parsed, user_lat, user_lon)
            if dist is None:
                continue

            r_id = dish["restaurant_id"]
            s1 = float(scores1[doc_id])
            s2 = float(scores2[doc_id])

            if s1 > 0.22:
                if r_id not in rest_dish1_candidates or s1 > rest_dish1_candidates[r_id]["score"]:
                    rest_dish1_candidates[r_id] = {"dish": dish, "score": s1, "dist": dist}

            if s2 > 0.22:
                if r_id not in rest_dish2_candidates or s2 > rest_dish2_candidates[r_id]["score"]:
                    rest_dish2_candidates[r_id] = {"dish": dish, "score": s2, "dist": dist}

        # Find intersection: Restaurants having BOTH items
        common_restaurants = set(rest_dish1_candidates.keys()).intersection(set(rest_dish2_candidates.keys()))

        bundles = []
        for r_id in common_restaurants:
            item1 = rest_dish1_candidates[r_id]
            item2 = rest_dish2_candidates[r_id]
            rest_meta = self.restaurant_catalog[r_id]

            total_bundle_price = item1["dish"]["price"] + item2["dish"]["price"]
            if parsed.max_price and total_bundle_price > parsed.max_price:
                continue

            dist = item1["dist"]
            dist_factor = 1.0 / (1.0 + 0.12 * dist)
            rating_factor = (rest_meta["rating"] / 5.0) ** 1.5
            bundle_score = ((item1["score"] + item2["score"]) / 2.0) * dist_factor * rating_factor

            bundles.append({
                "restaurant_id": r_id,
                "restaurant_name": rest_meta["name"],
                "locality": rest_meta["locality"],
                "restaurant_rating": rest_meta["rating"],
                "distance_km": dist,
                "delivery_time_mins": rest_meta["delivery_time_mins"],
                "bundle_score": round(bundle_score, 4),
                "total_bundle_price": total_bundle_price,
                "dish_pair": [
                    {
                        "matched_for": dish1_query,
                        "name": item1["dish"]["name"],
                        "price": item1["dish"]["price"],
                        "category": item1["dish"]["category"],
                        "is_veg": item1["dish"]["is_veg"]
                    },
                    {
                        "matched_for": dish2_query,
                        "name": item2["dish"]["name"],
                        "price": item2["dish"]["price"],
                        "category": item2["dish"]["category"],
                        "is_veg": item2["dish"]["is_veg"]
                    }
                ],
                "savings_or_offer": rest_meta.get("discount_offer", "Combo Available")
            })

        bundles.sort(key=lambda x: -x["bundle_score"])

        return {
            "query": parsed.raw_query,
            "intent": "MULTI_DISH_COMBO",
            "paired_queries": [dish1_query, dish2_query],
            "explanation": f"Discovered single restaurants serving BOTH '{dish1_query}' AND '{dish2_query}' in one order",
            "total_matches": len(bundles),
            "results": bundles[:top_k]
        }
