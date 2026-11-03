"""
Dataset validation and search capability test suite.
"""

import json

def validate_dataset(filepath):
    print(f"Validating {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 100, f"Expected 100 restaurants, found {len(data)}"
    
    rest_ids = set()
    dish_ids = set()
    total_dishes = 0
    categories_found = set()
    dietary_tags_found = set()
    min_dishes = 999
    max_dishes = 0

    for r in data:
        # Check restaurant ID
        assert r["id"] not in rest_ids, f"Duplicate restaurant ID: {r['id']}"
        rest_ids.add(r["id"])

        # Check required fields
        required_rest_fields = [
            "id", "restaurant_name", "locality", "city", "coordinates", "cuisines",
            "average_cost_for_two", "price_range", "aggregate_rating", "popularity_votes",
            "delivery_time_mins", "distance_km", "is_pure_veg", "menu_items"
        ]
        for field in required_rest_fields:
            assert field in r, f"Missing field {field} in restaurant {r['id']}"

        dishes = r["menu_items"]
        num_dishes = len(dishes)
        total_dishes += num_dishes
        min_dishes = min(min_dishes, num_dishes)
        max_dishes = max(max_dishes, num_dishes)

        # Ensure restaurant has many dishes
        assert num_dishes >= 20, f"Restaurant {r['id']} ({r['restaurant_name']}) has only {num_dishes} dishes"

        # Check pure veg constraint
        if r["is_pure_veg"]:
            for d in dishes:
                assert d["is_veg"] is True, f"Non-veg dish {d['name']} found in pure-veg restaurant {r['restaurant_name']}"

        # Check dishes
        required_dish_fields = [
            "dish_id", "name", "category", "description", "price", "is_veg",
            "spicy_level", "dietary_tags", "rating", "rating_count", "tags", "ingredients"
        ]
        for d in dishes:
            assert d["dish_id"] not in dish_ids, f"Duplicate dish ID: {d['dish_id']}"
            dish_ids.add(d["dish_id"])

            for df in required_dish_fields:
                assert df in d, f"Missing dish field {df} in dish {d.get('dish_id')}"

            assert len(d["description"].strip()) >= 20, f"Short description in {d['name']}: {d['description']}"
            assert d["price"] > 0, f"Invalid price {d['price']} in {d['name']}"
            categories_found.add(d["category"])
            for tag in d["dietary_tags"]:
                dietary_tags_found.add(tag)

    print("\n--- VALIDATION SUMMARY ---")
    print(f"Total Restaurants: {len(data)}")
    print(f"Total Unique Dishes: {total_dishes}")
    print(f"Dishes per restaurant range: {min_dishes} to {max_dishes} (Average: {total_dishes/len(data):.1f})")
    print(f"Distinct Dish Categories ({len(categories_found)}): {sorted(list(categories_found))}")
    print(f"Dietary Tags Represented: {sorted(list(dietary_tags_found))}")
    
    # Test sample search engine queries
    print("\n--- TEST SEARCH ENGINE QUERIES ---")
    
    # 1. Search for "Biryani"
    biryani_matches = [
        (r["restaurant_name"], d["name"], d["price"])
        for r in data for d in r["menu_items"]
        if "biryani" in d["name"].lower() or "biryani" in d["tags"]
    ]
    print(f"1. Query 'biryani': {len(biryani_matches)} dishes matched across restaurants.")

    # 2. Search for "vegan" or "gluten-free"
    vegan_matches = [
        d["name"] for r in data for d in r["menu_items"]
        if "Vegan" in d["dietary_tags"]
    ]
    print(f"2. Filter 'Vegan': {len(vegan_matches)} dishes available.")

    # 3. Search for "cheesy" or "truffle" in description
    truffle_matches = [
        (r["restaurant_name"], d["name"])
        for r in data for d in r["menu_items"]
        if "truffle" in d["description"].lower() or "truffle" in d["tags"]
    ]
    print(f"3. Semantic Query 'truffle': {len(truffle_matches)} items found.")

    # 4. Filter "High rating (>= 4.5) & Quick Delivery (<= 25 mins)"
    quick_top_rated = [
        (r["restaurant_name"], r["locality"], r["delivery_time_mins"], r["aggregate_rating"])
        for r in data
        if r["aggregate_rating"] >= 4.5 and r["delivery_time_mins"] <= 25
    ]
    print(f"4. Filter 'Rating >= 4.5 & Delivery <= 25 mins': {len(quick_top_rated)} restaurants.")

    print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    validate_dataset(r"d:\Search_Engine\food_delivery_search_dataset_100.json")

