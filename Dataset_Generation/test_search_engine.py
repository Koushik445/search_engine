"""
Interactive search demonstration against the 100-restaurant dataset.
Supports text matching, geo-distance ranking, multi-criteria filtering, and facet aggregations.
"""

import json
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0 # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

class FoodSearchEngine:
    def __init__(self, dataset_path):
        with open(dataset_path, "r", encoding="utf-8") as f:
            self.restaurants = json.load(f)

    def search_dishes(self, query, user_lat=12.9352, user_lon=77.6245, max_price=None, is_veg=None, max_distance_km=None):
        q_tokens = query.lower().split()
        results = []

        for rest in self.restaurants:
            r_lat = rest["coordinates"]["latitude"]
            r_lon = rest["coordinates"]["longitude"]
            dist = round(haversine_distance(user_lat, user_lon, r_lat, r_lon), 1)

            if max_distance_km and dist > max_distance_km:
                continue

            for dish in rest["menu_items"]:
                if is_veg is not None and dish["is_veg"] != is_veg:
                    continue
                if max_price is not None and dish["price"] > max_price:
                    continue

                # Compute search score
                name_words = dish["name"].lower()
                desc_words = dish["description"].lower()
                tag_words = " ".join(dish["tags"]).lower()
                ing_words = " ".join(dish["ingredients"]).lower()

                score = 0
                for token in q_tokens:
                    if token in name_words:
                        score += 10
                    if token in tag_words:
                        score += 5
                    if token in ing_words:
                        score += 3
                    if token in desc_words:
                        score += 2

                if score > 0:
                    results.append({
                        "dish_name": dish["name"],
                        "restaurant_name": rest["restaurant_name"],
                        "locality": rest["locality"],
                        "category": dish["category"],
                        "price": dish["price"],
                        "is_veg": dish["is_veg"],
                        "spicy_level": dish["spicy_level"],
                        "dietary_tags": dish["dietary_tags"],
                        "rating": dish["rating"],
                        "distance_km": dist,
                        "delivery_time_mins": rest["delivery_time_mins"],
                        "relevance_score": score
                    })

        # Sort by relevance and rating
        results.sort(key=lambda x: (x["relevance_score"], x["rating"]), reverse=True)
        return results

if __name__ == "__main__":
    engine = FoodSearchEngine(r"d:\Search_Engine\food_delivery_search_dataset_100.json")

    sample_queries = [
        ("crispy chicken wings", {"is_veg": False}),
        ("truffle pizza", {"max_price": 600}),
        ("paneer biryani", {"is_veg": True}),
        ("cold brew", {}),
        ("gluten-free", {})
    ]

    print("=" * 70)
    print("DEMO SEARCH EXECUTION ON 100-RESTAURANT DATASET")
    print("=" * 70)

    for q, filters in sample_queries:
        print(f"\n[QUERY]: '{q}' | Filters: {filters}")
        hits = engine.search_dishes(q, **filters)
        print(f"Total matching results: {len(hits)}")
        for i, hit in enumerate(hits[:3], 1):
            veg_label = "[VEG]" if hit['is_veg'] else "[NON-VEG]"
            print(f"  {i}. {veg_label} {hit['dish_name']} (Rs. {hit['price']}) - {hit['restaurant_name']} ({hit['locality']})")
            print(f"     Rating: {hit['rating']} / 5.0 | Dist: {hit['distance_km']} km | Time: {hit['delivery_time_mins']}m | Score: {hit['relevance_score']}")
