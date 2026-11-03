"""
Full dataset generation script:
Combines 100 curated restaurant profiles with cuisine catalogs, generating 20-30 authentic
menu items per restaurant with rich descriptions, dietary tags, spicy levels, ingredients,
calories, and customization options.
"""

import json
import random
import os
import re

import generate_dataset
import cuisine_catalogs_part1
import cuisine_catalogs_part2

CATALOGS = {
    "biryani_andhra": cuisine_catalogs_part1.BIRYANI_ANDHRA_DISHES,
    "north_indian": cuisine_catalogs_part1.NORTH_INDIAN_DISHES,
    "south_indian": cuisine_catalogs_part1.SOUTH_INDIAN_DISHES,
    "american_burgers": cuisine_catalogs_part1.AMERICAN_BURGERS_DISHES,
    "italian_pizza": cuisine_catalogs_part1.ITALIAN_PIZZA_DISHES,
    "pan_asian": cuisine_catalogs_part2.PAN_ASIAN_DISHES,
    "healthy_vegan": cuisine_catalogs_part2.HEALTHY_VEGAN_DISHES,
    "middle_eastern": cuisine_catalogs_part2.MIDDLE_EASTERN_DISHES,
    "desserts_ice_cream": cuisine_catalogs_part2.DESSERTS_ICE_CREAM_DISHES,
    "cafes_specialty": cuisine_catalogs_part2.CAFES_SPECIALTY_DISHES,
}

UNSPLASH_IMAGES = {
    "biryani_andhra": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800",
    "north_indian": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800",
    "south_indian": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=800",
    "american_burgers": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800",
    "italian_pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800",
    "pan_asian": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?w=800",
    "healthy_vegan": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800",
    "middle_eastern": "https://images.unsplash.com/photo-1541518763669-27fef04b14ea?w=800",
    "desserts_ice_cream": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800",
    "cafes_specialty": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800"
}

GENERIC_BEVERAGES = [
    {
        "name": "Fresh Lime Soda (Sweet & Salted)",
        "category": "Beverages",
        "description": "Fizzy effervescent club soda infused with freshly squeezed Kagzi lime juice, rock salt, and sugar syrup. Ultra refreshing.",
        "base_price": 80, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Club Soda", "Fresh Lime Juice", "Rock Salt", "Mint", "Sugar"],
        "tags": ["lime soda", "fresh lime", "cold beverage", "refreshing", "mocktail"],
        "calories_kcal": 65
    },
    {
        "name": "Iced Lemon Mint Green Tea (350ml)",
        "category": "Beverages",
        "description": "Chilled slow-steeped organic green tea infused with fresh mint leaves, lemon zest, and a hint of wild honey.",
        "base_price": 110, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Green Tea", "Fresh Mint", "Lemon Zest", "Honey", "Ice"],
        "tags": ["iced tea", "lemon tea", "green tea", "detox beverage", "summer cooler"],
        "calories_kcal": 45
    },
    {
        "name": "Classic Sweet Mango Lassi (400ml)",
        "category": "Beverages",
        "description": "Thick traditional churned yogurt blended with sweet Alphonso mango pulp, green cardamom, and garnished with roasted pistachios.",
        "base_price": 130, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Whole Milk Yogurt", "Alphonso Mango", "Cardamom", "Pistachios"],
        "tags": ["mango lassi", "lassi", "yogurt smoothie", "probiotic", "sweet drink"],
        "calories_kcal": 240
    }
]

GENERIC_DESSERTS = [
    {
        "name": "Warm Gulab Jamun in Rose Saffron Syrup (2 Pcs)",
        "category": "Desserts",
        "description": "Soft melt-in-mouth reduced milk khoya dumplings fried golden brown and soaked in fragrant rose and green cardamom scented sugar syrup.",
        "base_price": 95, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Khoya Mawa", "Sugar Syrup", "Cardamom", "Rose Water", "Pistachios"],
        "tags": ["gulab jamun", "indian sweet", "hot sweet", "dessert", "classic"],
        "calories_kcal": 310
    },
    {
        "name": "Kesar Rasmalai (2 Pcs)",
        "category": "Desserts",
        "description": "Delicate poached cottage cheese patties floating in chilled, saffron-scented reduced whole milk (angoor rabdi), studded with almonds and pistachios.",
        "base_price": 120, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Chenna Cottage Cheese", "Reduced Milk", "Saffron", "Pistachios", "Almonds"],
        "tags": ["rasmalai", "kesar rasmalai", "chilled sweet", "bengali sweet", "dessert"],
        "calories_kcal": 280
    }
]

def generate_customizations(dish_name, category, is_veg):
    customizations = []
    cat_lower = category.lower()
    
    # Portion size
    if any(k in cat_lower for k in ["biryani", "rice", "curry", "main", "bowls", "noodles"]):
        customizations.append({
            "name": "Portion Size",
            "options": ["Regular", "Large (Serves 2) (+₹120)"]
        })
    elif "pizza" in cat_lower:
        customizations.append({
            "name": "Crust Type",
            "options": ["Hand-Tossed Sourdough (Standard)", "Cheese Burst Crust (+₹90)", "Thin & Crispy"]
        })
    elif "burger" in cat_lower:
        customizations.append({
            "name": "Add-ons",
            "options": ["Extra Cheddar Cheese (+₹40)", "Crispy Bacon / Fried Egg (+₹60)", "No Add-ons"]
        })
    elif "beverage" in cat_lower or "coffee" in cat_lower or "tea" in cat_lower:
        customizations.append({
            "name": "Sugar Level",
            "options": ["Regular Sweetness", "Less Sugar", "Sugar-Free (Stevia)", "No Sugar"]
        })

    # Spice level customization for savory items
    if not any(k in cat_lower for k in ["dessert", "sweet", "beverage", "shake", "coffee"]):
        customizations.append({
            "name": "Preparation Preference",
            "options": ["Standard Chef Style", "Less Spicy / Mild", "Extra Spicy (+₹20)"]
        })

    return customizations

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def build_restaurant_menu(rest):
    family = rest["cuisine_family"]
    catalog = CATALOGS.get(family, cuisine_catalogs_part1.BIRYANI_ANDHRA_DISHES)
    is_rest_pure_veg = rest["is_pure_veg"]
    price_range = rest["price_range"]
    multiplier = 0.85 if price_range == 1 else (1.0 if price_range == 2 else (1.25 if price_range == 3 else 1.55))

    menu_items = []
    dish_idx = 1

    # 1. Add all items from the cuisine catalog matching vegetarian constraints
    for item in catalog:
        if is_rest_pure_veg and not item["is_veg"]:
            continue  # Pure veg restaurant cannot have non-veg dishes

        # Check if dish matches signature
        is_sig = any(sig.lower() in item["name"].lower() or item["name"].lower() in sig.lower() for sig in rest["signature_dishes"])

        price = int(round(item["base_price"] * multiplier / 10) * 10)
        dish_id = f"dish_{rest['id'][5:]}_{dish_idx:02d}"
        
        # Rating and bestsellers
        rating = round(random.uniform(4.2, 4.9), 1) if is_sig else round(random.uniform(3.9, 4.7), 1)
        rating_count = random.randint(450, 4800) if is_sig else random.randint(40, 850)
        is_bestseller = True if is_sig else (random.random() < 0.25)
        prep_time = random.randint(18, 35)

        # Build comprehensive dish object
        dish_obj = {
            "dish_id": dish_id,
            "name": item["name"],
            "category": item["category"],
            "description": item["description"],
            "price": price,
            "is_veg": item["is_veg"],
            "spicy_level": item["spicy_level"],
            "dietary_tags": list(item["dietary_tags"]),
            "is_bestseller": is_bestseller,
            "rating": rating,
            "rating_count": rating_count,
            "preparation_time_mins": prep_time,
            "calories_kcal": item.get("calories_kcal", random.randint(250, 650)),
            "tags": list(item["tags"]) + [rest["locality"].split()[0].lower(), rest["cuisines"][0].lower()],
            "ingredients": list(item["ingredients"]),
            "customization_options": generate_customizations(item["name"], item["category"], item["is_veg"])
        }
        menu_items.append(dish_obj)
        dish_idx += 1

    # 2. Add signature dishes that may not have been in the master catalog yet
    for sig_name in rest["signature_dishes"]:
        # If not already present
        if not any(d["name"].lower() == sig_name.lower() for d in menu_items):
            dish_id = f"dish_{rest['id'][5:]}_{dish_idx:02d}"
            # Guess veg status:
            non_veg_keywords = ["chicken", "mutton", "fish", "prawn", "beef", "duck", "bacon", "salmon", "meat", "pork", "egg", "shrimp", "seafood"]
            is_veg = not any(w in sig_name.lower() for w in non_veg_keywords)
            if is_rest_pure_veg:
                is_veg = True

            cat = "Signature Main Course"
            if any(k in sig_name.lower() for k in ["biryani", "pulao", "rice"]):
                cat = "Biryani & Rice"
            elif any(k in sig_name.lower() for k in ["kebab", "fry", "tikka", "roll", "65", "wings"]):
                cat = "Starters"
            elif any(k in sig_name.lower() for k in ["burger", "sandwich"]):
                cat = "Burgers"
            elif any(k in sig_name.lower() for k in ["pizza"]):
                cat = "Pizzas"
            elif any(k in sig_name.lower() for k in ["dosa", "idli", "vada", "bath"]):
                cat = "Breakfast & Tiffin"
            elif any(k in sig_name.lower() for k in ["coffee", "tea", "chai", "lassi", "shake"]):
                cat = "Beverages"
            elif any(k in sig_name.lower() for k in ["halwa", "cake", "pudding", "sundae", "ice cream", "sweet"]):
                cat = "Desserts"

            desc = f"{rest['name']}'s acclaimed chef-special {sig_name}, prepared with authentic spices, fresh local ingredients, and traditional culinary finesse. A patron-favourite specialty dish."
            base_p = 320 if "biryani" in sig_name.lower() or "mutton" in sig_name.lower() else (140 if is_veg else 280)
            price = int(round(base_p * multiplier / 10) * 10)

            diet_tags = ["Vegetarian"] if is_veg else ["Halal", "High-Protein"]

            dish_obj = {
                "dish_id": dish_id,
                "name": sig_name,
                "category": cat,
                "description": desc,
                "price": price,
                "is_veg": is_veg,
                "spicy_level": "Medium" if is_veg else "Spicy",
                "dietary_tags": diet_tags,
                "is_bestseller": True,
                "rating": round(random.uniform(4.5, 4.9), 1),
                "rating_count": random.randint(1200, 5600),
                "preparation_time_mins": random.randint(20, 35),
                "calories_kcal": random.randint(350, 720),
                "tags": [slugify(sig_name), "signature", "chef special", "bestseller", rest["name"].lower()],
                "ingredients": ["Signature House Spices", "Fresh Ingredients", "Desi Ghee / Olive Oil"],
                "customization_options": generate_customizations(sig_name, cat, is_veg)
            }
            menu_items.append(dish_obj)
            dish_idx += 1

    # 3. Add Restaurant Signature Combo Box
    combo_id = f"dish_{rest['id'][5:]}_{dish_idx:02d}"
    combo_name = f"{rest['name']} Signature Special Platter / Meal Box"
    combo_price = int(round((rest['cost_for_two'] * 0.55) / 10) * 10)
    combo_is_veg = is_rest_pure_veg or (random.random() < 0.4)
    menu_items.append({
        "dish_id": combo_id,
        "name": combo_name,
        "category": "Combos & Value Meals",
        "description": f"Curated single-diner feast featuring {rest['name']}'s signature main, choice of hot bread/aromatic rice, house starter, fresh salad, and sweet dessert.",
        "price": combo_price,
        "is_veg": combo_is_veg,
        "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"] if combo_is_veg else ["High-Protein", "Halal"],
        "is_bestseller": True,
        "rating": round(random.uniform(4.4, 4.8), 1),
        "rating_count": random.randint(600, 2900),
        "preparation_time_mins": 30,
        "calories_kcal": random.randint(650, 890),
        "tags": ["combo", "meal box", "thali", "value meal", "complete meal", rest["name"].lower()],
        "ingredients": ["Chef Curated Starter", "Signature Main", "Rice / Bread", "House Dessert"],
        "customization_options": [
            {"name": "Choice of Beverage", "options": ["Fresh Lime Soda", "Masala Buttermilk", "Soft Drink (300ml)", "No Drink"]}
        ]
    })
    dish_idx += 1

    # 4. Complementary Desserts and Beverages to ensure rich complete menu (>= 22 items)
    for b in GENERIC_BEVERAGES:
        if not any(d["name"].lower() == b["name"].lower() for d in menu_items):
            b_id = f"dish_{rest['id'][5:]}_{dish_idx:02d}"
            menu_items.append({
                "dish_id": b_id,
                "name": b["name"],
                "category": b["category"],
                "description": b["description"],
                "price": int(round(b["base_price"] * multiplier / 10) * 10),
                "is_veg": b["is_veg"],
                "spicy_level": b["spicy_level"],
                "dietary_tags": list(b["dietary_tags"]),
                "is_bestseller": False,
                "rating": round(random.uniform(4.1, 4.6), 1),
                "rating_count": random.randint(100, 600),
                "preparation_time_mins": 10,
                "calories_kcal": b["calories_kcal"],
                "tags": list(b["tags"]),
                "ingredients": list(b["ingredients"]),
                "customization_options": generate_customizations(b["name"], b["category"], True)
            })
            dish_idx += 1

    for d in GENERIC_DESSERTS:
        if not any(item["name"].lower() == d["name"].lower() for item in menu_items):
            d_id = f"dish_{rest['id'][5:]}_{dish_idx:02d}"
            menu_items.append({
                "dish_id": d_id,
                "name": d["name"],
                "category": d["category"],
                "description": d["description"],
                "price": int(round(d["base_price"] * multiplier / 10) * 10),
                "is_veg": d["is_veg"],
                "spicy_level": d["spicy_level"],
                "dietary_tags": list(d["dietary_tags"]),
                "is_bestseller": False,
                "rating": round(random.uniform(4.3, 4.8), 1),
                "rating_count": random.randint(150, 950),
                "preparation_time_mins": 12,
                "calories_kcal": d["calories_kcal"],
                "tags": list(d["tags"]),
                "ingredients": list(d["ingredients"]),
                "customization_options": generate_customizations(d["name"], d["category"], True)
            })
            dish_idx += 1

    # 5. Guarantee at least 22 items per restaurant
    if len(menu_items) < 22:
        extra_items = [
            {
                "name": f"{rest['name']} Chef's Tasting Appetizer Platter",
                "category": "Starters & Small Plates",
                "description": f"Artisanal sampler plate featuring three bite-sized chef special appetizers from {rest['name']}, served with house dips and seasoned crisps.",
                "base_price": 240, "is_veg": is_rest_pure_veg,
                "spicy_level": "Medium",
                "dietary_tags": ["Vegetarian"] if is_rest_pure_veg else ["High-Protein"],
                "ingredients": ["Chef's Daily Fresh Harvest", "House Spices", "Dipping Sauces"],
                "tags": ["platter", "sampler", "tasting plate", "starter", rest["name"].lower()],
                "calories_kcal": 360
            },
            {
                "name": f"{rest['name']} House Handcrafted Brewed Beverage",
                "category": "Beverages",
                "description": f"Chilled house special brewed beverage prepared with crushed seasonal fruit pulp, fresh herbs, and sparkling water.",
                "base_price": 120, "is_veg": True,
                "spicy_level": "None",
                "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
                "ingredients": ["Seasonal Fruit Extract", "Herb Infusion", "Sparkling Water"],
                "tags": ["house beverage", "specialty drink", "cooler", rest["name"].lower()],
                "calories_kcal": 110
            },
            {
                "name": f"{rest['name']} Seasonal Artisanal Dessert",
                "category": "Desserts",
                "description": f"Delightful house special dessert crafted daily by {rest['name']}'s pastry chef using organic unrefined sweetness and fresh dairy.",
                "base_price": 160, "is_veg": True,
                "spicy_level": "None",
                "dietary_tags": ["Vegetarian"],
                "ingredients": ["Whole Milk Cream", "Organic Raw Sweetener", "Pistachio Praline"],
                "tags": ["house dessert", "pastry", "sweet treat", rest["name"].lower()],
                "calories_kcal": 310
            },
            {
                "name": f"{rest['name']} Crispy Herb Fries / Finger Chips",
                "category": "Sides & Accompaniments",
                "description": f"Golden crispy potato batons tossed in rosemary sea salt, garlic herbs, and served with house dips.",
                "base_price": 140, "is_veg": True,
                "spicy_level": "Mild",
                "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
                "ingredients": ["Potatoes", "Rosemary Salt", "Garlic Powder", "Cold-Pressed Oil"],
                "tags": ["fries", "finger chips", "crispy side", "snack"],
                "calories_kcal": 340
            }
        ]
        for extra in extra_items:
            if len(menu_items) >= 22:
                break
            if not any(item["name"].lower() == extra["name"].lower() for item in menu_items):
                e_id = f"dish_{rest['id'][5:]}_{dish_idx:02d}"
                menu_items.append({
                    "dish_id": e_id,
                    "name": extra["name"],
                    "category": extra["category"],
                    "description": extra["description"],
                    "price": int(round(extra["base_price"] * multiplier / 10) * 10),
                    "is_veg": extra["is_veg"],
                    "spicy_level": extra["spicy_level"],
                    "dietary_tags": list(extra["dietary_tags"]),
                    "is_bestseller": False,
                    "rating": round(random.uniform(4.2, 4.7), 1),
                    "rating_count": random.randint(120, 500),
                    "preparation_time_mins": 15,
                    "calories_kcal": extra["calories_kcal"],
                    "tags": list(extra["tags"]),
                    "ingredients": list(extra["ingredients"]),
                    "customization_options": generate_customizations(extra["name"], extra["category"], extra["is_veg"])
                })
                dish_idx += 1

    return menu_items

def generate_full_dataset():
    restaurants = []
    total_dishes = 0

    for r_meta in generate_dataset.RESTAURANTS_METADATA:
        r_id = r_meta["id"]
        r_name = r_meta["name"]
        slug = f"{slugify(r_name)}-{slugify(r_meta['locality'])}"
        menu = build_restaurant_menu(r_meta)
        total_dishes += len(menu)

        search_keywords = [
            slugify(r_name),
            r_name.lower(),
            r_meta["locality"].lower(),
            slugify(r_meta["locality"]),
            r_meta["city"].lower(),
        ] + [c.lower() for c in r_meta["cuisines"]] + [slugify(sig) for sig in r_meta["signature_dishes"][:3]]

        price_symbols = {1: "₹", 2: "₹₹", 3: "₹₹₹", 4: "₹₹₹₹"}

        restaurant_obj = {
            "id": r_id,
            "restaurant_name": r_name,
            "slug": slug,
            "locality": r_meta["locality"],
            "city": r_meta["city"],
            "address": r_meta["address"],
            "coordinates": r_meta["coordinates"],
            "cuisines": r_meta["cuisines"],
            "cuisine_family": r_meta["cuisine_family"],
            "average_cost_for_two": r_meta["cost_for_two"],
            "price_range": r_meta["price_range"],
            "price_tier_symbol": price_symbols.get(r_meta["price_range"], "₹₹"),
            "aggregate_rating": r_meta["rating"],
            "popularity_votes": r_meta["rating_count"],
            "delivery_time_mins": r_meta["delivery_time_mins"],
            "distance_km": r_meta["distance_km"],
            "is_pure_veg": r_meta["is_pure_veg"],
            "has_online_delivery": True,
            "has_table_booking": r_meta["price_range"] >= 3,
            "is_open_now": True,
            "opening_hours": "10:30 AM - 11:30 PM",
            "featured_image": UNSPLASH_IMAGES.get(r_meta["cuisine_family"], "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800"),
            "discount_offer": r_meta["discount_offer"],
            "search_keywords": list(set(search_keywords)),
            "total_dishes_count": len(menu),
            "menu_items": menu
        }
        restaurants.append(restaurant_obj)

    return restaurants, total_dishes

if __name__ == "__main__":
    print("Generating complete 100-restaurant dataset...")
    dataset, dish_count = generate_full_dataset()
    print(f"Total Restaurants: {len(dataset)}")
    print(f"Total Dishes: {dish_count}")
    print(f"Average dishes per restaurant: {dish_count / len(dataset):.1f}")

    # Output to food_delivery_search_dataset_100.json
    out_file = r"d:\Search_Engine\food_delivery_search_dataset_100.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved to {out_file} (Size: {os.path.getsize(out_file) / (1024*1024):.2f} MB)")

    # Also update golden_search_dataset.json so that any existing scripts/benchmarks have the full dataset
    golden_file = r"d:\Search_Engine\golden_search_dataset.json"
    # First create backup of the 10-item starter
    backup_file = r"d:\Search_Engine\golden_search_dataset_starter_10.json"
    if not os.path.exists(backup_file):
        with open(golden_file, "r", encoding="utf-8") as f:
            old_data = f.read()
        with open(backup_file, "w", encoding="utf-8") as f:
            f.write(old_data)
        print(f"Preserved original 10-restaurant starter to {backup_file}")

    with open(golden_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"Updated {golden_file} with full 100-restaurant dataset.")
