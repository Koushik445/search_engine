"""
Cuisine Catalogs - Part 2:
6. pan_asian
7. healthy_vegan
8. middle_eastern
9. desserts_ice_cream
10. cafes_specialty
"""

PAN_ASIAN_DISHES = [
    # Dim Sum & Baos
    {
        "name": "Steamed Chicken & Prawn Siu Mai",
        "category": "Dim Sum & Baos",
        "description": "Open-faced Cantonese steamed dumplings filled with succulent minced chicken, chopped prawns, shiitake mushrooms, crowned with flying fish roe.",
        "base_price": 340, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Minced Chicken", "Tiger Prawns", "Shiitake Mushrooms", "Sesame Oil", "Wonton Wrapper"],
        "tags": ["siu mai", "dim sum", "dumplings", "mainland china", "cantonese"],
        "calories_kcal": 280
    },
    {
        "name": "Crystal Vegetable Truffle Dumplings",
        "category": "Dim Sum & Baos",
        "description": "Translucent steamed starch dumplings stuffed with water chestnuts, lotus root, asparagus, and a delicate hint of black truffle essence.",
        "base_price": 320, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Water Chestnuts", "Asparagus", "Lotus Root", "Truffle Oil", "Tapioca Wrapper"],
        "tags": ["crystal dim sum", "truffle dumplings", "veg dim sum", "healthy"],
        "calories_kcal": 220
    },
    {
        "name": "Braised Pork Belly Bao with Green Apple",
        "category": "Dim Sum & Baos",
        "description": "Pillowy steamed open lotus buns stuffed with melt-in-mouth braised pork belly, hoisin sauce, crisp green apple slaw, and crushed roasted peanuts.",
        "base_price": 390, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Steamed Bao Buns", "Braised Pork Belly", "Hoisin Glaze", "Green Apple Slaw", "Peanuts"],
        "tags": ["bao", "pork belly bao", "fatty bao", "taiwanese bao", "bestseller"],
        "calories_kcal": 490
    },
    {
        "name": "Crispy Teriyaki Tofu Steamed Bao (2 Pcs)",
        "category": "Dim Sum & Baos",
        "description": "Fluffy steamed Asian buns packed with panko-crusted crispy silken tofu, sriracha vegan mayo, cucumber ribbons, and toasted sesame.",
        "base_price": 290, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Bao Buns", "Crispy Silken Tofu", "Teriyaki Sauce", "Sriracha Vegan Mayo", "Cucumber"],
        "tags": ["tofu bao", "veg bao", "crispy tofu", "asian buns"],
        "calories_kcal": 360
    },

    # Sushi & Appetizers
    {
        "name": "Dragon Prawn Tempura Roll (8 Pcs)",
        "category": "Sushi & Starters",
        "description": "Uramaki sushi roll packed with crunchy prawn tempura, cucumber, wrapped with avocado and spicy tobiko mayo, drizzled with sweet unagi sauce.",
        "base_price": 490, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Pescatarian", "High-Protein"],
        "ingredients": ["Sushi Rice", "Prawn Tempura", "Avocado", "Nori Seaweed", "Tobiko Mayo", "Unagi Sauce"],
        "tags": ["sushi", "dragon roll", "prawn tempura", "japanese", "bestseller"],
        "calories_kcal": 420
    },
    {
        "name": "Spicy Salmon Maki Roll (8 Pcs)",
        "category": "Sushi & Starters",
        "description": "Fresh Atlantic sashimi-grade salmon diced with Japanese spicy mayo, spring onions, and toasted sesame seeds, rolled in seasoned sushi rice.",
        "base_price": 520, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Pescatarian", "High-Protein", "Gluten-Free"],
        "ingredients": ["Fresh Salmon", "Sushi Rice", "Spicy Mayo", "Spring Onions", "Nori"],
        "tags": ["salmon sushi", "spicy maki", "japanese roll", "harima"],
        "calories_kcal": 390
    },
    {
        "name": "Avocado & Cream Cheese Veg Roll (8 Pcs)",
        "category": "Sushi & Starters",
        "description": "Creamy Hass avocado paired with Philadelphia cream cheese, pickled cucumber, and toasted white sesame in vinegared sushi rice.",
        "base_price": 410, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Hass Avocado", "Cream Cheese", "Cucumber", "Sushi Rice", "Toasted Sesame"],
        "tags": ["veg sushi", "avocado roll", "california veg", "healthy sushi"],
        "calories_kcal": 340
    },
    {
        "name": "Crispy Honey Chilli Lotus Stem",
        "category": "Sushi & Starters",
        "description": "Thin sliced crunchy lotus stem chips tossed with roasted crushed garlic, mild red chillies, honey, and scallions in a sticky wok glaze.",
        "base_price": 280, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Lotus Stem", "Honey", "Red Chilli Paste", "Garlic", "Spring Onions"],
        "tags": ["lotus stem", "crispy starter", "honey chilli", "mamagoto"],
        "calories_kcal": 310
    },
    {
        "name": "Chargrilled Chicken Satay with Peanut Dip",
        "category": "Sushi & Starters",
        "description": "Skewered tender chicken breast strips marinated in lemongrass, turmeric, and coconut milk, flame grilled and served with rich peanut sauce.",
        "base_price": 330, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein", "Gluten-Free"],
        "ingredients": ["Chicken Breast Skewers", "Lemongrass", "Coconut Milk", "Peanut Dip", "Cucumber Relish"],
        "tags": ["chicken satay", "peanut sauce", "malaysian", "nasi and mee"],
        "calories_kcal": 390
    },

    # Noodles, Ramen & Mains
    {
        "name": "Chashu Tonkotsu Ramen Bowl",
        "category": "Noodles & Bowls",
        "description": "Rich 16-hour simmered savory bone broth with handmade ramen noodles, tender chashu pork, seasoned soft-boiled ramen egg (ajitsuke tamago), bamboo shoots, and nori.",
        "base_price": 490, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Ramen Noodles", "Pork Chashu", "Tonkotsu Broth", "Nitmag Tamago Egg", "Menma Bamboo", "Nori"],
        "tags": ["ramen", "tonkotsu ramen", "noodle soup", "fatty bao", "japanese comfort"],
        "calories_kcal": 680
    },
    {
        "name": "Penang Mee Goreng Mamak",
        "category": "Noodles & Bowls",
        "description": "Spicy Malaysian hawker style egg noodles wok tossed with prawns, shredded chicken, crispy tofu cubes, bean sprouts, and dark sweet spicy sambal.",
        "base_price": 380, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal"],
        "ingredients": ["Egg Noodles", "Prawns & Chicken", "Bean Sprouts", "Tofu Puffs", "Sambal Chilli Paste"],
        "tags": ["mee goreng", "malaysian noodles", "hawker noodles", "nasi and mee"],
        "calories_kcal": 620
    },
    {
        "name": "Thai Green Chicken Curry with Jasmine Rice",
        "category": "Noodles & Bowls",
        "description": "Aromatic central Thai curry crafted from fresh green bird's eye chillies, Thai basil, galangal, kaffir lime leaves, and thick coconut milk. Served with steamed jasmine rice.",
        "base_price": 420, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "Gluten-Free"],
        "ingredients": ["Chicken Breast", "Green Curry Paste", "Coconut Milk", "Thai Eggplant", "Jasmine Rice"],
        "tags": ["thai green curry", "jasmine rice", "coconut curry", "thai chimney"],
        "calories_kcal": 590
    },
    {
        "name": "Classic Pad Thai Street Noodles",
        "category": "Noodles & Bowls",
        "description": "Wok tossed flat rice noodles with egg, tofu, tamarind pulp, palm sugar, fish/soya sauce, crowned with crushed roasted peanuts and fresh lime wedge.",
        "base_price": 360, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Flat Rice Noodles", "Firm Tofu", "Tamarind Pulp", "Bean Sprouts", "Peanuts", "Lime"],
        "tags": ["pad thai", "thai noodles", "street food", "rice noodles"],
        "calories_kcal": 540
    },
    {
        "name": "Chilli Garlic Schezwan Noodles",
        "category": "Noodles & Bowls",
        "description": "Desi Indo-Chinese wok fried noodles tossed with shredded cabbage, bell peppers, carrots, fiery roasted Sichuan red pepper oil, and charred garlic.",
        "base_price": 260, "is_veg": True, "spicy_level": "Extra Spicy",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Hakka Noodles", "Schezwan Sauce", "Minced Garlic", "Bell Peppers", "Spring Onions"],
        "tags": ["schezwan noodles", "chilli garlic noodles", "indo chinese", "chung wah"],
        "calories_kcal": 480
    },
    {
        "name": "General Tso's Sweet & Spicy Crispy Chicken",
        "category": "Mains & Curries",
        "description": "Crisp battered chicken chunks tossed in tangy, sweet, and pungent ginger-garlic sauce with whole dried red chillies and steamed broccoli florets.",
        "base_price": 360, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Crispy Chicken", "General Tso Glaze", "Ginger", "Garlic", "Dried Red Chillies", "Broccoli"],
        "tags": ["general tso", "chinese chicken", "sweet and spicy", "mainland china"],
        "calories_kcal": 540
    },

    # Desserts
    {
        "name": "Mango Sticky Rice with Sweet Coconut Cream",
        "category": "Desserts",
        "description": "Steamed Thai sweet glutinous rice infused with coconut milk and pandan, served with ripe honey-sweet mango slices and toasted sesame.",
        "base_price": 260, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Glutinous Sticky Rice", "Ripe Mango", "Coconut Milk", "Palm Sugar", "Sesame"],
        "tags": ["mango sticky rice", "thai dessert", "coconut dessert", "sweet"],
        "calories_kcal": 410
    }
]


HEALTHY_VEGAN_DISHES = [
    # Bowls & Salads
    {
        "name": "Mediterranean Roast Chicken Quinoa Bowl",
        "category": "Superfood Bowls",
        "description": "Herb marinated roast chicken breast, tri-color organic quinoa, Kalamata olives, Persian cucumbers, cherry tomatoes, and creamy feta cheese drizzled with lemon oregano vinaigrette.",
        "base_price": 360, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein", "Gluten-Free"],
        "ingredients": ["Roast Chicken Breast", "Organic Quinoa", "Feta Cheese", "Kalamata Olives", "Lemon Vinaigrette"],
        "tags": ["quinoa bowl", "salad days", "healthy bowl", "high protein", "mediterranean"],
        "calories_kcal": 440
    },
    {
        "name": "Sourdough Smashed Avocado Toast",
        "category": "Toasts & Starters",
        "description": "Thick artisanal rustic sourdough slice toasted crisp, topped with hand-mashed Hass avocado, cold pressed extra virgin olive oil, toasted pumpkin seeds, and chilli flakes.",
        "base_price": 310, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Artisanal Sourdough Bread", "Hass Avocado", "Pumpkin Seeds", "Extra Virgin Olive Oil", "Sea Salt"],
        "tags": ["avocado toast", "sourdough", "green theory", "vegan breakfast", "bestseller"],
        "calories_kcal": 360
    },
    {
        "name": "High Protein Teriyaki Tofu Brown Rice Bowl",
        "category": "Superfood Bowls",
        "description": "Pan-seared non-GMO organic tofu glazed in low-sodium ginger teriyaki sauce, served over steamed brown rice with edamame, sautéed broccoli, and sesame.",
        "base_price": 320, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free", "High-Protein"],
        "ingredients": ["Organic Tofu", "Steamed Brown Rice", "Edamame", "Broccoli", "Ginger Teriyaki"],
        "tags": ["tofu bowl", "brown rice", "eatfit", "vegan protein", "healthy dinner"],
        "calories_kcal": 410
    },
    {
        "name": "Classic Caesar Chicken Salad with Herb Croutons",
        "category": "Salads",
        "description": "Crisp romaine lettuce leaves, grilled herb chicken strips, shaved 24-month Grana Padano, whole grain herb croutons, tossed in light Caesar garlic dressing.",
        "base_price": 340, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Romaine Lettuce", "Grilled Chicken", "Parmesan Shavings", "Herb Croutons", "Caesar Dressing"],
        "tags": ["caesar salad", "chicken salad", "healthy salad", "low carb"],
        "calories_kcal": 380
    },
    {
        "name": "Raw Pad Thai Zucchini Ribbon Salad",
        "category": "Salads",
        "description": "Spiralized zucchini noodles (zoodles) and crunchy carrot ribbons tossed with fresh coriander, purple cabbage, bean sprouts, and spicy Thai peanut almond dressing.",
        "base_price": 280, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free", "Keto-Friendly"],
        "ingredients": ["Zucchini Ribbons", "Carrots", "Purple Cabbage", "Peanut Almond Dressing", "Coriander"],
        "tags": ["zucchini salad", "zoodles", "keto salad", "copper and cloves", "raw vegan"],
        "calories_kcal": 260
    },
    {
        "name": "Hawaiian Ahi Tuna Poke Bowl",
        "category": "Superfood Bowls",
        "description": "Sashimi-grade diced yellowfin tuna tossed in sesame shoyu dressing, served on a bed of warm sushi rice with edamame, seaweed salad, diced mango, and wasabi mayo.",
        "base_price": 460, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Pescatarian", "High-Protein"],
        "ingredients": ["Ahi Tuna Sashimi", "Sushi Rice", "Wakame Seaweed", "Edamame", "Wasabi Mayo", "Mango"],
        "tags": ["poke bowl", "ahi tuna", "poke story", "hawaiian bowl", "fresh seafood"],
        "calories_kcal": 470
    },
    {
        "name": "Ayurvedic Healing Moong Dal Kitchari",
        "category": "Wholesome Warmers",
        "description": "Traditional tridoshic sattvic preparation of split yellow moong lentils and aged red rice cooked with fresh ginger, turmeric root, cumin, and a spoonful of A2 Gir cow ghee.",
        "base_price": 240, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Split Yellow Moong", "Red Rice", "A2 Gir Cow Ghee", "Fresh Turmeric", "Cumin Seeds"],
        "tags": ["kitchari", "ayurvedic", "yogisthaan", "sattvic", "healing", "digestive"],
        "calories_kcal": 330
    },
    {
        "name": "Farm Fresh Ragi Crust Margherita Pizza",
        "category": "Guilt-Free Pizza & Mains",
        "description": "Gluten-free organic finger millet (ragi) sourdough base topped with slow roasted tomato concassé, vegan cashew mozzarella, and sweet fresh basil leaves.",
        "base_price": 390, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Ragi Flour Crust", "Roasted Tomatoes", "Cashew Cheese", "Fresh Basil", "Cold Pressed Olive Oil"],
        "tags": ["ragi pizza", "gluten free pizza", "sante spa", "vegan pizza"],
        "calories_kcal": 420
    },
    {
        "name": "Keto Cheesy Cauliflower & Broccoli Bake",
        "category": "Guilt-Free Pizza & Mains",
        "description": "Fresh tender cauliflower and broccoli florets baked in rich almond flour béchamel sauce, smothered under melted sharp cheddar and herbs.",
        "base_price": 310, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Keto-Friendly", "Gluten-Free"],
        "ingredients": ["Broccoli", "Cauliflower", "Sharp Cheddar", "Almond Flour Cream", "Herbs"],
        "tags": ["keto bake", "low carb", "cheesy broccoli", "freshmenu"],
        "calories_kcal": 380
    },

    # Juices, Smoothies & Treats
    {
        "name": "Cold-Pressed Detox Green Juice (300ml)",
        "category": "Juices & Elixirs",
        "description": "Pure unpasteurized juice extracted from organic celery, cucumber, green apple, kale, baby spinach, ginger, and lemon. No added water or sugar.",
        "base_price": 160, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Organic Celery", "Cucumber", "Green Apple", "Kale", "Spinach", "Lemon", "Ginger"],
        "tags": ["green juice", "detox juice", "cold pressed", "healthy beverage"],
        "calories_kcal": 90
    },
    {
        "name": "Detox Spirulina & Berry Smoothie Bowl",
        "category": "Juices & Elixirs",
        "description": "Thick smoothie blend of frozen wild blueberries, banana, coconut milk, and blue spirulina, topped with chia seeds, toasted coconut flakes, and raw cacao nibs.",
        "base_price": 280, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Wild Blueberries", "Spirulina", "Coconut Milk", "Chia Seeds", "Cacao Nibs"],
        "tags": ["smoothie bowl", "spirulina", "superfood", "vegan breakfast"],
        "calories_kcal": 310
    },
    {
        "name": "Raw Avocado & Key Lime Tart",
        "category": "Guilt-Free Treats",
        "description": "No-bake raw vegan dessert: creamy lime zest and Hass avocado ganache set on a crust made of crushed Medjool dates, almonds, and walnuts.",
        "base_price": 240, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Hass Avocado", "Key Lime Juice", "Medjool Dates", "Almonds", "Coconut Oil"],
        "tags": ["raw tart", "vegan dessert", "key lime", "sugar free"],
        "calories_kcal": 280
    },
    {
        "name": "Moroccan Spiced Chickpea & Spinach Stew",
        "category": "Wholesome Warmers",
        "description": "Hearty slow-simmered stew of organic Kabuli chickpeas, tender baby spinach, roasted sweet potatoes, and warming Ras el Hanout Moroccan spices. Served with brown rice.",
        "base_price": 290, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free", "High-Protein"],
        "ingredients": ["Kabuli Chickpeas", "Baby Spinach", "Sweet Potatoes", "Ras el Hanout", "Brown Rice"],
        "tags": ["chickpea stew", "moroccan stew", "vegan protein", "healthy dinner"],
        "calories_kcal": 390
    },
    {
        "name": "Crispy Baked Falafel Superfood Salad",
        "category": "Salads",
        "description": "Oven-baked herbed falafel patties served over mixed mesclun greens, cherry tomatoes, cucumbers, shredded purple cabbage, and tahini drizzle.",
        "base_price": 310, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free", "High-Protein"],
        "ingredients": ["Baked Falafel", "Mesclun Greens", "Cherry Tomatoes", "Cucumber", "Tahini Dressing"],
        "tags": ["falafel salad", "baked falafel", "superfood salad", "clean eating"],
        "calories_kcal": 360
    },
    {
        "name": "Vegan Mac & Creamy Cashew Cheese Bake",
        "category": "Guilt-Free Pizza & Mains",
        "description": "Whole wheat elbow macaroni baked in rich velvety nutritional yeast and cashew cream sauce, topped with herbed almond crumb.",
        "base_price": 330, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Whole Wheat Macaroni", "Cashew Cream", "Nutritional Yeast", "Almond Crumb", "Garlic"],
        "tags": ["vegan mac and cheese", "cashew cheese", "plant based", "comfort food"],
        "calories_kcal": 420
    },
    {
        "name": "Warm Golden Turmeric Almond Milk Latte",
        "category": "Juices & Elixirs",
        "description": "Soothing organic turmeric root simmered with cold pressed almond milk, black pepper, Ceylon cinnamon, and wild forest honey.",
        "base_price": 170, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Organic Turmeric", "Almond Milk", "Black Pepper", "Cinnamon", "Honey"],
        "tags": ["turmeric latte", "golden milk", "immunity booster", "hot beverage"],
        "calories_kcal": 130
    },
    {
        "name": "Coconut Chia Seed Mango Parfait",
        "category": "Guilt-Free Treats",
        "description": "Layered overnight pudding of organic black chia seeds soaked in fresh coconut milk, layered with crushed Alphonso mango puree and toasted almonds.",
        "base_price": 220, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Chia Seeds", "Coconut Milk", "Alphonso Mango", "Toasted Almonds"],
        "tags": ["chia pudding", "mango parfait", "healthy dessert", "gluten free"],
        "calories_kcal": 260
    }
]


MIDDLE_EASTERN_DISHES = [
    # Platters & Dips
    {
        "name": "Grand Mediterranean Mezze Platter",
        "category": "Mezze & Dips",
        "description": "Festive spread of creamy tahini hummus, smoky baba ganoush, fresh parsley tabbouleh, stuffed vine leaves, pickled turnips, and warm fluffy pita pockets.",
        "base_price": 450, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Chickpea Hummus", "Charred Eggplant Baba Ganoush", "Tabbouleh", "Pita Bread", "Pickles"],
        "tags": ["mezze", "hummus", "baba ganoush", "byblos", "olive beach", "bestseller"],
        "calories_kcal": 580
    },
    {
        "name": "Creamy Hummus with Extra Virgin Olive Oil & Warm Pita",
        "category": "Mezze & Dips",
        "description": "Ultra smooth velvety dip of slow boiled chickpeas blended with stoneground Lebanese tahini, lemon juice, garlic, topped with paprika and Palestinian extra virgin olive oil.",
        "base_price": 240, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Boiled Chickpeas", "Lebanese Tahini", "Garlic", "Lemon Juice", "Cold Pressed Olive Oil", "Pita"],
        "tags": ["hummus", "pita bread", "habibi falafel", "vegan dip"],
        "calories_kcal": 380
    },
    {
        "name": "Smoky Baba Ganoush Eggplant Dip",
        "category": "Mezze & Dips",
        "description": "Open-flame charred eggplants mashed with sesame tahini, crushed garlic, pomegranate seeds, and drizzled with fragrant green olive oil.",
        "base_price": 260, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Charred Eggplant", "Tahini Paste", "Garlic", "Pomegranate Seeds", "Olive Oil"],
        "tags": ["baba ganoush", "eggplant dip", "lebanese dip", "mezze"],
        "calories_kcal": 260
    },

    # Falafel, Shawarma & Grills
    {
        "name": "Crispy Falafel Pita Pocket Sandwich",
        "category": "Shawarma & Falafel",
        "description": "Golden fried herbed chickpea falafel croquettes stuffed inside warm pocket pita with diced tomatoes, cucumbers, tangy tahini sauce, and spicy shatta relish.",
        "base_price": 190, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Ground Chickpeas & Herbs", "Pita Pocket", "Tahini Dressing", "Pickled Cucumbers", "Shatta Chilli"],
        "tags": ["falafel pita", "habibi falafel", "vegan sandwich", "bestseller"],
        "calories_kcal": 420
    },
    {
        "name": "Batata Harra Fiery Lebanese Potatoes",
        "category": "Mezze & Dips",
        "description": "Golden roasted potato cubes tossed in olive oil with minced garlic, fresh coriander, crushed red chilli flakes, and fresh lemon juice.",
        "base_price": 210, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Potatoes", "Garlic", "Coriander", "Chilli Flakes", "Lemon Juice", "Olive Oil"],
        "tags": ["batata harra", "spicy potatoes", "lebanese appetizer", "vegan starter"],
        "calories_kcal": 310
    },
    {
        "name": "Za'atar & Olive Oil Stonebaked Flatbread",
        "category": "Shawarma & Falafel",
        "description": "Traditional Lebanese manousheh flatbread baked over stone hearth, brushed generously with aromatic wild thyme (za'atar), toasted sesame, sumac, and extra virgin olive oil.",
        "base_price": 180, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Manousheh Dough", "Za'atar Wild Thyme", "Toasted Sesame", "Sumac", "Extra Virgin Olive Oil"],
        "tags": ["zaatar flatbread", "manousheh", "lebanese bread", "vegan bakery"],
        "calories_kcal": 340
    },
    {
        "name": "Fresh Arabic Fattoush Salad with Crispy Pita",
        "category": "Mezze & Dips",
        "description": "Crisp mixed garden greens, Persian cucumbers, radishes, and tomatoes tossed with tart pomegranate molasses vinaigrette and golden fried pita chips.",
        "base_price": 220, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Romaine Lettuce", "Persian Cucumber", "Radishes", "Crispy Pita Chips", "Pomegranate Molasses", "Sumac"],
        "tags": ["fattoush salad", "arabic salad", "crispy pita", "vegan salad"],
        "calories_kcal": 240
    },
    {
        "name": "Warm Spiced Lentil Soup (Shorbat Adas)",
        "category": "Mezze & Dips",
        "description": "Comforting Middle Eastern red lentil soup gently spiced with cumin, caramelized onions, and lemon, served with crispy fried pita croutons.",
        "base_price": 160, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Red Lentils", "Cumin", "Onions", "Carrots", "Lemon", "Olive Oil"],
        "tags": ["lentil soup", "shorbat adas", "arabic soup", "comfort food", "healthy"],
        "calories_kcal": 210
    },
    {
        "name": "Classic Chicken Shawarma Roll in Rumali",
        "category": "Shawarma & Falafel",
        "description": "Spit-roasted slow revolving chicken shavings rolled in soft rumali roti with thick garlic toum, French fries, pickled cucumbers, and tahini.",
        "base_price": 180, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Slow Roasted Chicken", "Garlic Toum Mayo", "Pickled Cucumber", "French Fries", "Rumali Roti"],
        "tags": ["shawarma roll", "chicken shawarma", "al amanah", "shawarma king", "bestseller"],
        "calories_kcal": 490
    },
    {
        "name": "Open Plate Chicken Shawarma with Garlic Toum",
        "category": "Shawarma & Falafel",
        "description": "Heaped platter of juicy spiced chicken shawarma slices served with two khuboos flatbreads, extra creamy Lebanese garlic toum, pickles, and crispy salted fries.",
        "base_price": 260, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Chicken Shawarma Meat", "Garlic Toum", "Khuboos Bread", "Pickles", "Fries"],
        "tags": ["open shawarma", "shawarma plate", "garlic dip", "filling meal"],
        "calories_kcal": 610
    },
    {
        "name": "Juicy Shish Tawook Skewers Platter",
        "category": "Grills & Kebabs",
        "description": "Cubes of chicken breast steeped in garlic, lemon, sumac, and tomato yogurt marinade, grilled on skewers over red hot coals, served with saffron rice and toum.",
        "base_price": 380, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein", "Gluten-Free"],
        "ingredients": ["Chicken Breast", "Garlic Marinade", "Sumac", "Lemon", "Toum Garlic Dip", "Saffron Rice"],
        "tags": ["shish tawook", "lebanese grill", "chicken skewers", "byblos"],
        "calories_kcal": 480
    },
    {
        "name": "Chelo Kabab Koobideh with Saffron Rice",
        "category": "Grills & Kebabs",
        "description": "National dish of Iran: two long skewers of minced spiced lamb and onion kebabs grilled over open charcoal fire, served on fluffy buttery saffron basmati rice with charred tomato.",
        "base_price": 540, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Minced Lamb Koobideh", "Saffron Rice", "Grilled Tomato", "Butter Slab", "Sumac Powder"],
        "tags": ["chelo kabab", "koobideh", "persian terrace", "iranian kebab", "saffron rice"],
        "calories_kcal": 720
    },
    {
        "name": "Yemeni Mutton Mandi Rice Platter",
        "category": "Grills & Kebabs",
        "description": "Tender braised mutton shank cooked low and slow with whole Yemeni spices, served atop smoked long-grain mandi rice with spicy tomato daqqoos sauce.",
        "base_price": 490, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Mutton Shank", "Smoked Mandi Rice", "Hawaij Spice Blend", "Daqqoos Salsa", "Roasted Almonds"],
        "tags": ["mandi", "mutton mandi", "yemeni rice", "levant kitchen", "arabian feast"],
        "calories_kcal": 810
    },

    # Desserts
    {
        "name": "Authentic Turkish Cheese Kunafa",
        "category": "Desserts",
        "description": "Crisp spun shredded filo pastry (kataifi) soaked in sweet orange blossom syrup, layered over stretchy sweet Akkawi/mozzarella cheese, topped with crushed pistachio dust.",
        "base_price": 280, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Kataifi Pastry", "Sweet Stretchy Cheese", "Sugar Rose Syrup", "Crushed Pistachios"],
        "tags": ["kunafa", "knafeh", "turkish sweet", "pistachio kunafa", "dessert"],
        "calories_kcal": 520
    },
    {
        "name": "Pistachio Honey Baklava (4 Pcs)",
        "category": "Desserts",
        "description": "Golden crisp layered filo pastry sheets brushed with clarified butter, filled with coarsely chopped pistachios and sweetened with pure honey syrup.",
        "base_price": 220, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Filo Pastry", "Pistachios", "Honey Syrup", "Clarified Butter"],
        "tags": ["baklava", "middle eastern sweet", "honey pastry"],
        "calories_kcal": 360
    }
]


DESSERTS_ICE_CREAM_DISHES = [
    # Sundaes & Ice Cream
    {
        "name": "Death By Chocolate (DBC) Legendary Sundae",
        "category": "Ice Cream Sundaes",
        "description": "The undisputed king of desserts: warm rich chocolate cake smothered in two scoops of vanilla bean ice cream, hot chocolate fudge, roasted almonds, and topped with honey and cream.",
        "base_price": 240, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Rich Chocolate Cake", "Vanilla Ice Cream", "Hot Chocolate Fudge", "Roasted Almonds", "Fresh Cream", "Honey"],
        "tags": ["dbc", "death by chocolate", "corner house", "legendary sundae", "bestseller", "chocolate"],
        "calories_kcal": 680
    },
    {
        "name": "Hot Chocolate Fudge Sundae",
        "category": "Ice Cream Sundaes",
        "description": "Two generous scoops of creamy vanilla ice cream drenched in thick bubbling hot dark chocolate fudge sauce, topped with crunchy roasted cashews.",
        "base_price": 190, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Vanilla Ice Cream", "Hot Dark Fudge Sauce", "Toasted Cashew Nuts"],
        "tags": ["hot chocolate fudge", "hcf", "corner house", "classic sundae"],
        "calories_kcal": 510
    },
    {
        "name": "Tender Coconut Fresh Ice Cream (500ml Tub)",
        "category": "Real Fruit Ice Creams",
        "description": "Naturals iconic recipe made with just three ingredients: fresh creamy milk, pure sugar, and tender young coconut pulp (malai). No artificial flavours or preservatives.",
        "base_price": 290, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Pure Cow Milk", "Fresh Tender Coconut Malai", "Sugar"],
        "tags": ["tender coconut", "naturals ice cream", "fresh fruit ice cream", "bestseller"],
        "calories_kcal": 410
    },
    {
        "name": "Alphonso Fresh Mango Ice Cream Tub (500ml)",
        "category": "Real Fruit Ice Creams",
        "description": "Rich artisanal ice cream churned with the pure pulp of Ratnagiri Alphonso mangoes and whole milk.",
        "base_price": 290, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Alphonso Mango Pulp", "Whole Milk", "Sugar"],
        "tags": ["mango ice cream", "alphonso", "naturals", "fruit scoop"],
        "calories_kcal": 430
    },
    {
        "name": "Italian Gianduja Hazelnut Gelato Scoop",
        "category": "Artisan Gelato",
        "description": "Velvety smooth authentic Italian artisan gelato crafted from roasted Piedmont hazelnuts and rich milk chocolate.",
        "base_price": 160, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Piedmont Hazelnuts", "Milk Chocolate", "Whole Milk Gelato Base"],
        "tags": ["gelato", "gianduja", "hazelnut gelato", "milano ice cream"],
        "calories_kcal": 280
    },
    {
        "name": "Royal Gudbud Ice Cream Sundae",
        "category": "Ice Cream Sundaes",
        "description": "Mangalore style tall glass sundae layering strawberry, vanilla, and mango ice creams with fresh fruits, candied tutty-fruity, jelly, and dry fruits.",
        "base_price": 220, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Trio Ice Cream Scoops", "Fresh Fruits", "Jelly Cubes", "Tutty Fruity", "Dry Fruits"],
        "tags": ["gudbud", "polar bear", "fruit sundae", "classic sundae"],
        "calories_kcal": 480
    },

    # Cakes, Brownies & Waffles
    {
        "name": "World Famous Classic Banana Pudding (Jar)",
        "category": "Cakes & Puddings",
        "description": "Magnolia Bakery's legendary recipe: layers of sweet vanilla pudding, ripe fresh banana slices, and softened Nilla vanilla wafers.",
        "base_price": 280, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Vanilla Custard Pudding", "Fresh Bananas", "Nilla Wafers", "Whipped Cream"],
        "tags": ["banana pudding", "magnolia bakery", "new york pudding", "bestseller"],
        "calories_kcal": 490
    },
    {
        "name": "Overload Chocolate Fudgy Brownie",
        "category": "Cakes & Brownies",
        "description": "Theobroma's signature ultra-dense, intensely fudgy dark chocolate brownie packed with melted dark chocolate chips and crackly top.",
        "base_price": 130, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Dark Cocoa", "Dark Chocolate Chunks", "Pure Butter", "Sugar", "Flour"],
        "tags": ["theobroma", "overload brownie", "fudge brownie", "chocolate"],
        "calories_kcal": 380
    },
    {
        "name": "Triple Chocolate Crispy Waffle",
        "category": "Waffles & Crepes",
        "description": "Freshly baked warm chocolate waffle loaded with dark chocolate sauce, milk chocolate spread, and white chocolate chips.",
        "base_price": 180, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Chocolate Waffle Batter", "Dark Chocolate Sauce", "Milk Chocolate", "White Chocolate Chips"],
        "tags": ["waffle", "triple chocolate", "belgian waffle co", "crispy waffle"],
        "calories_kcal": 520
    },
    {
        "name": "Red Velvet Cream Cheese Layer Cake Slice",
        "category": "Cakes & Brownies",
        "description": "Moist, cocoa-hinted scarlet sponge layered with tangy whipped vanilla cream cheese frosting.",
        "base_price": 240, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Red Velvet Sponge", "Philadelphia Cream Cheese Frosting", "Vanilla Bean"],
        "tags": ["red velvet cake", "cream cheese", "cake slice", "magnolia bakery"],
        "calories_kcal": 460
    },
    {
        "name": "Hot Spanish Churros with Warm Belgian Milk Chocolate",
        "category": "Waffles & Crepes",
        "description": "Five golden ridged Spanish churros fried crisp, rolled in fragrant cinnamon sugar, served with a pot of warm Belgian milk chocolate dip.",
        "base_price": 210, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Churro Dough", "Cinnamon Sugar", "Belgian Milk Chocolate"],
        "tags": ["churros", "art of delight", "cinnamon sugar", "chocolate dip"],
        "calories_kcal": 440
    },
    {
        "name": "Assorted Luxury French Macarons Box (6 Pcs)",
        "category": "Cakes & Chocolates",
        "description": "Delicate almond meringue shells with chewy centres and rich ganache fillings: Pistachio, Dark Chocolate, Salted Caramel, Raspberry, and Passionfruit.",
        "base_price": 380, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["Gluten-Free"],
        "ingredients": ["Almond Flour", "Egg Whites", "Chocolate Ganache", "Fruit Purees"],
        "tags": ["macarons", "smoor", "french dessert", "luxury gift"],
        "calories_kcal": 360
    },
    {
        "name": "Classic Thick Butterscotch Milkshake (Glass Bottle)",
        "category": "Beverages",
        "description": "Keventers signature cold milkshake blended thick with caramelized butterscotch syrup and crunchy praline bits in a vintage keepsake glass bottle.",
        "base_price": 190, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Full Cream Milk", "Butterscotch Syrup", "Praline Crunch", "Vanilla Ice Cream"],
        "tags": ["keventers", "butterscotch shake", "thickshake", "glass bottle"],
        "calories_kcal": 440
    }
]


CAFES_SPECIALTY_DISHES = [
    # Coffee & Hot Beverages
    {
        "name": "Attikan Estate Pour Over Cold Brew (300ml)",
        "category": "Specialty Coffee",
        "description": "Single-origin Arabica from Biligirirangana Hills steeped cold for 18 hours. Delivers tasting notes of dark chocolate, sweet figs, and roasted almonds.",
        "base_price": 210, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Single Origin 100% Arabica", "Purified Water"],
        "tags": ["cold brew", "blue tokai", "black coffee", "specialty coffee", "artisanal"],
        "calories_kcal": 5
    },
    {
        "name": "Sea Salt Caramel Mocha Frappe",
        "category": "Specialty Coffee",
        "description": "Double espresso shot blended with rich dark cocoa, homemade salted caramel syrup, full cream milk, and crushed ice, topped with whipped cream.",
        "base_price": 260, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Espresso Shot", "Dark Cocoa", "Salted Caramel", "Milk", "Whipped Cream"],
        "tags": ["frappe", "sea salt mocha", "third wave coffee", "iced coffee"],
        "calories_kcal": 380
    },
    {
        "name": "Ginger Elaichi Desi Chai Flask (500ml)",
        "category": "Tea & Chai",
        "description": "Hot Assam tea leaves slow-simmered with crushed fresh ginger root and green cardamom pods in full cream milk. Delivered piping hot in a 5-layer thermal flask.",
        "base_price": 150, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Assam Tea Leaves", "Fresh Ginger", "Green Cardamom", "Milk", "Sugar"],
        "tags": ["chai flask", "adrak elaichi chai", "chai point", "tea", "hot chai"],
        "calories_kcal": 180
    },
    {
        "name": "Kulhad Masala Chai & Maska Bun",
        "category": "Tea & Chai",
        "description": "Steaming hot spiced milk tea served with a warm, soft sweet bun slathered with salted Amul butter.",
        "base_price": 140, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Spiced Tea", "Sweet Bun", "Amul Butter", "Cardamom & Cinnamon"],
        "tags": ["bun maska", "chaayos", "masala chai", "breakfast"],
        "calories_kcal": 340
    },

    # Breakfast & Bakery
    {
        "name": "Farmer's All Day English Breakfast Platter",
        "category": "Breakfast & Brunch",
        "description": "Two fried eggs sunny-side up, grilled chicken sausages, crispy bacon rashers, baked Heinz beans, grilled tomato halves, sautéed button mushrooms, and buttered toast.",
        "base_price": 380, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Farm Eggs", "Chicken Sausages", "Bacon", "Baked Beans", "Mushrooms", "Sourdough Toast"],
        "tags": ["english breakfast", "all day breakfast", "hole in the wall", "bestseller", "brunch"],
        "calories_kcal": 720
    },
    {
        "name": "Fluffy Blueberry Pancakes with Maple Syrup (3 Pcs)",
        "category": "Breakfast & Brunch",
        "description": "Golden stack of buttermilk pancakes bursting with juicy wild blueberries, served with whipped butter and 100% pure maple syrup.",
        "base_price": 270, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Buttermilk", "Flour", "Wild Blueberries", "Maple Syrup", "Whipped Butter"],
        "tags": ["pancakes", "blueberry pancakes", "sweet breakfast", "hole in the wall"],
        "calories_kcal": 490
    },
    {
        "name": "Toasted Sesame Bagel with Herb Cream Cheese",
        "category": "Breakfast & Brunch",
        "description": "New York style boiled and baked bagel loaded with toasted sesame seeds, served warm with garlic chive cream cheese spread.",
        "base_price": 210, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Sesame Bagel", "Philadelphia Cream Cheese", "Chives", "Garlic"],
        "tags": ["bagel", "cream cheese", "third wave", "breakfast"],
        "calories_kcal": 380
    },
    {
        "name": "Almond Frangipane Flaky Butter Croissant",
        "category": "Breakfast & Brunch",
        "description": "Twice-baked French butter croissant filled with rich almond frangipane cream, topped with toasted sliced almonds and powdered sugar.",
        "base_price": 190, "is_veg": False, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["French Butter Laminated Dough", "Almond Cream", "Flaked Almonds"],
        "tags": ["croissant", "almond croissant", "blue tokai", "french bakery"],
        "calories_kcal": 420
    },

    # Pub Bites, Regional & Street Food
    {
        "name": "Woodfired BBQ Smoked Chicken Pizza",
        "category": "Pub Food & Specialties",
        "description": "Toit's classic: thin crust pizza topped with tangy smoky BBQ sauce, shredded smoked chicken, sliced red onions, fresh coriander, and gouda mozzarella blend.",
        "base_price": 460, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal"],
        "ingredients": ["Pizza Dough", "BBQ Chicken", "Gouda & Mozzarella", "Red Onions", "Coriander"],
        "tags": ["toit", "bbq pizza", "pub pizza", "brewpub special"],
        "calories_kcal": 690
    },
    {
        "name": "Baked Cheesy Nachos with Guacamole",
        "category": "Pub Food & Specialties",
        "description": "Crisp corn tortilla chips piled high with melted cheddar, jalapeños, refried beans, pico de gallo, fresh smashed avocado guacamole, and sour cream.",
        "base_price": 320, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Corn Tortilla Chips", "Cheddar Cheese", "Guacamole", "Sour Cream", "Pico de Gallo"],
        "tags": ["nachos", "loaded nachos", "toit bites", "appetizer"],
        "calories_kcal": 560
    },
    {
        "name": "Crispy Calamari Golden Rings with Tartar",
        "category": "Pub Food & Specialties",
        "description": "Tender squid rings dipped in light seasoned flour, flashed fried until golden crisp, served with homemade caper tartar dip and lemon.",
        "base_price": 360, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Pescatarian", "High-Protein"],
        "ingredients": ["Squid Calamari", "Seasoned Flour", "Tartar Sauce", "Lemon"],
        "tags": ["calamari", "squid rings", "seafood starter", "pub food"],
        "calories_kcal": 380
    },
    {
        "name": "Special Amul Butter Pav Bhaji",
        "category": "Pub Food & Specialties",
        "description": "Mumbai Chowpatty style mashed vegetable curry infused with special pav bhaji spices and lots of yellow Amul butter. Served with 2 soft butter toasted pavs.",
        "base_price": 180, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Potatoes & Peas Mash", "Amul Butter", "Pav Bhaji Masala", "Soft Pav Buns", "Lemon & Onions"],
        "tags": ["pav bhaji", "butter pav bhaji", "shiv sagar", "mumbai street food", "bestseller"],
        "calories_kcal": 540
    },
    {
        "name": "Bombay Grilled Triple Decker Cheese Sandwich",
        "category": "Pub Food & Specialties",
        "description": "Three layers of crustless white bread slathered with spicy mint chutney, stuffed with sliced boiled potatoes, beetroot, cucumber, tomato, and molten Amul cheese, grilled to crisp perfection.",
        "base_price": 160, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["White Bread", "Mint Chutney", "Boiled Potatoes", "Beetroot", "Amul Cheese"],
        "tags": ["bombay sandwich", "grilled sandwich", "street food", "cheese sandwich"],
        "calories_kcal": 420
    },
    {
        "name": "Alleppey Fish Curry with Raw Mango",
        "category": "Pub Food & Specialties",
        "description": "Karavalli's coastal masterpiece: tender seer fish steaks poached gently in mildly spiced coconut milk gravy with sour green raw mango slices, ginger, and curry leaves.",
        "base_price": 540, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Pescatarian", "High-Protein", "Gluten-Free"],
        "ingredients": ["Seer Fish (Surmai)", "Coconut Milk", "Raw Mango Slices", "Curry Leaves", "Shallots"],
        "tags": ["alleppey fish curry", "karavalli", "kerala fish curry", "coastal luxury"],
        "calories_kcal": 460
    },
    {
        "name": "Thalappakatti Seeraga Samba Mutton Biryani",
        "category": "Pub Food & Specialties",
        "description": "Authentic Dindigul biryani cooked with tiny aromatic Seeraga Samba rice, tender bone-in mutton pieces, and proprietary Tamil Nadu hill country spices.",
        "base_price": 380, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Seeraga Samba Rice", "Country Mutton", "Ghee", "Shallots", "Secret Thalappakatti Spices"],
        "tags": ["thalappakatti", "seeraga samba", "dindigul biryani", "mutton biryani", "tamil nadu"],
        "calories_kcal": 740
    }
]

print("Cuisine Catalogs Part 2 loaded successfully.")
