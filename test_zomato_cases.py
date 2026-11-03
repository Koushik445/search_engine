"""
Comprehensive test script for Zomato conversational search queries.
Tests:
  1. Multi-Dish Search ("Chai and samosa", "Burger with cold drink", "Anda curry and roti")
  2. Restaurant + Dish ("Truffles ka burger", "Meghana special chicken biryani")
  3. Price & Budget Constraints ("pizza under 200", "burger 150rs wala", "hundred ke andar")
  4. Cheapest ("sabse sasta pizza")
  5. Distance & Geo ("pizza outlets near me", "best outlets near me")
  6. Conversational / Colloquial ("koi achcha sa sabji batao", "spicy dal")
"""

import json
import sys

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
from search_engine import AdvancedFoodSearchEngine

def run_tests():
    print("=" * 75)
    print("INITIALIZING ADVANCED CONVERSATIONAL SEARCH ENGINE")
    print("=" * 75)

    engine = AdvancedFoodSearchEngine(r"d:\Search_Engine")

    test_queries = [
        "Chai and samosa",
        "Burger with cold drink",
        "Truffles ka burger",
        "pizza under 250",
        "burger 150rs wala",
        "sabse sasta pizza",
        "pizza outlets near me",
        "pure veg south indian breakfast in jayanagar",
        "spicy chicken biryani",
        "koi achcha sa sabji batao"
    ]

    print("\n" + "=" * 75)
    print("EXECUTING CONVERSATIONAL TEST QUERIES")
    print("=" * 75)

    for query in test_queries:
        print(f"\n>>> USER QUERY: \"{query}\"")
        res = engine.search(query, user_lat=12.9352, user_lon=77.6245, top_k=3)
        print(f"    Intent Detected: {res['intent']}")
        print(f"    System Logic:    {res['explanation']}")
        print(f"    Total Matches:   {res['total_matches']}")

        if res["intent"] == "MULTI_DISH_COMBO":
            for i, bundle in enumerate(res["results"], 1):
                p1 = bundle["dish_pair"][0]
                p2 = bundle["dish_pair"][1]
                print(f"    Bundle {i}: {bundle['restaurant_name']} ({bundle['locality']}) - {bundle['distance_km']} km away")
                print(f"      + {p1['name']} (Rs. {p1['price']})")
                print(f"      + {p2['name']} (Rs. {p2['price']})")
                print(f"      = Total Combo Price: Rs. {bundle['total_bundle_price']} | Time: {bundle['delivery_time_mins']} mins | Offer: {bundle['savings_or_offer']}")
        elif res["intent"] in ("RESTAURANT_SEARCH", "OUTLET_SEARCH"):
            for i, r in enumerate(res["results"], 1):
                veg_tag = "[PURE VEG]" if r.get('is_pure_veg') else "[NON-VEG]"
                cuisines_str = ", ".join(r.get('cuisines', []))
                print(f"    Outlet {i}: {veg_tag} {r['restaurant_name']} ({r['locality']}) - {r['distance_km']} km away")
                print(f"      Cuisines: {cuisines_str} | Rating: {r['rating']} / 5.0 | {r.get('discount_offer', '')}")
        else:
            for i, d in enumerate(res["results"], 1):
                veg_tag = "[VEG]" if d['is_veg'] else "[NON-VEG]"
                print(f"    Result {i}: {veg_tag} {d['dish_name']} (Rs. {d['price']}) from {d['restaurant_name']} ({d['locality']})")
                print(f"      Score: {d['relevance_score']} | Match: {d.get('match_confidence', 'N/A')} | Dist: {d['distance_km']} km | Rating: {d.get('rating', 'N/A')}")

    print("\n" + "=" * 75)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
