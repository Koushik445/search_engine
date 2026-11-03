"""
Interactive Conversational Search Engine CLI
Run: python cli_search.py
"""

import sys
from search_engine import AdvancedFoodSearchEngine

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

def main():
    print("=" * 70)
    print("  FOOD DELIVERY CONVERSATIONAL SEARCH ENGINE (Zomato-style NLS)")
    print("=" * 70)
    print("Loading engine and pre-computed neural embeddings...")
    engine = AdvancedFoodSearchEngine(r"d:\Search_Engine")
    print("\nSearch engine is ready! Try queries like:")
    print("  - 'Chai and samosa'")
    print("  - 'Burger with cold drink'")
    print("  - 'Truffles ka burger'")
    print("  - 'pizza under 250'")
    print("  - 'burger 150rs wala'")
    print("  - 'sabse sasta pizza'")
    print("  - 'pure veg breakfast in jayanagar'")
    print("  - 'spicy mutton biryani near me'")
    print("  - 'type \"exit\" or \"quit\" to leave'\n")

    user_lat, user_lon = 12.9352, 77.6245  # Default location: Koramangala

    while True:
        try:
            query = input("\n[Search Query] > ").strip()
            if not query:
                continue
            if query.lower() in ("exit", "quit", "q"):
                print("Exiting search engine. Goodbye!")
                break

            res = engine.search(query, user_lat=user_lat, user_lon=user_lon, top_k=5)

            print("\n" + "-" * 70)
            print(f"QUERY: \"{res['query']}\"")
            print(f"INTENT: {res['intent']} | LOGIC: {res['explanation']}")
            print(f"TOTAL MATCHES: {res['total_matches']}")
            print("-" * 70)

            if res["intent"] == "MULTI_DISH_COMBO":
                if not res["results"]:
                    print("No single restaurant found serving both items simultaneously.")
                for i, b in enumerate(res["results"], 1):
                    p1 = b["dish_pair"][0]
                    p2 = b["dish_pair"][1]
                    print(f"\n[{i}] {b['restaurant_name']} ({b['locality']}) - {b['distance_km']} km away")
                    print(f"    • {p1['name']} (Rs. {p1['price']})")
                    print(f"    • {p2['name']} (Rs. {p2['price']})")
                    print(f"    => Combo Total: Rs. {b['total_bundle_price']} | Delivery: {b['delivery_time_mins']}m | {b['savings_or_offer']}")
            elif res["intent"] in ("RESTAURANT_SEARCH", "OUTLET_SEARCH"):
                for i, r in enumerate(res["results"], 1):
                    veg_str = "[PURE VEG]" if r.get("is_pure_veg") else "[NON-VEG]"
                    print(f"\n[{i}] {veg_str} {r['restaurant_name']} ({r['locality']})")
                    print(f"    Distance: {r['distance_km']} km | Delivery: {r['delivery_time_mins']} mins | Rating: {r['rating']} ★")
                    print(f"    Cuisines: {', '.join(r.get('cuisines', []))}")
                    if r.get("discount_offer"):
                        print(f"    Offer: {r['discount_offer']}")
            else:
                for i, d in enumerate(res["results"], 1):
                    veg_str = "[VEG]" if d['is_veg'] else "[NON-VEG]"
                    print(f"\n[{i}] {veg_str} {d['dish_name']} (Rs. {d['price']})")
                    print(f"    Restaurant: {d['restaurant_name']} ({d['locality']}) - {d['distance_km']} km away")
                    print(f"    Relevance: {d['relevance_score']} | Match: {d.get('match_confidence', 'N/A')} | Rating: {d['rating']} ★")
                    print(f"    Description: {d['description']}")

        except KeyboardInterrupt:
            print("\nExiting search engine.")
            break
        except Exception as e:
            print(f"Error processing query: {e}")

if __name__ == "__main__":
    main()

