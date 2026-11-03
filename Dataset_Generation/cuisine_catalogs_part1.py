"""
Cuisine Catalogs - Part 1:
1. biryani_andhra
2. north_indian
3. south_indian
4. american_burgers
5. italian_pizza
"""

BIRYANI_ANDHRA_DISHES = [
    # Starters
    {
        "name": "Andhra Chilli Chicken Dry",
        "category": "Starters",
        "description": "Bite-sized chicken chunks sautéed with fiery slit green chillies, curry leaves, and secret Andhra spices. Crisp on the outside and juicy within.",
        "base_price": 290, "is_veg": False, "spicy_level": "Extra Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Chicken Chunks", "Green Chillies", "Curry Leaves", "Ginger Garlic Paste", "Soy & Andhra Spices"],
        "tags": ["andhra", "chilli chicken", "spicy starter", "dry chicken", "crispy", "appetizer"],
        "calories_kcal": 420
    },
    {
        "name": "Boneless Chicken 65",
        "category": "Starters",
        "description": "Crisp deep-fried boneless chicken marinated in spiced yogurt, red chilli powder, crushed black pepper, and fresh curry leaves.",
        "base_price": 310, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Boneless Chicken", "Yogurt", "Kashmiri Red Chilli", "Curry Leaves", "Cornstarch"],
        "tags": ["chicken 65", "crispy", "snack", "starter", "fried chicken", "bestseller"],
        "calories_kcal": 450
    },
    {
        "name": "Apollo Fish Fry",
        "category": "Starters",
        "description": "Tender boneless fish fillets tossed in a fiery Hyderabadi temper of tempered curd, crushed coriander seeds, and sliced green chillies.",
        "base_price": 360, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein", "Pescatarian"],
        "ingredients": ["Boneless Fish Fillet", "Curd", "Curry Leaves", "Lemon Juice", "Hyderabadi Spices"],
        "tags": ["apollo fish", "seafood", "fish fry", "hyderabadi", "starter"],
        "calories_kcal": 380
    },
    {
        "name": "Guntur Chicken Dry",
        "category": "Starters",
        "description": "Signature Andhra chicken dry preparation coated in pungent roasted Guntur red chillies and caramelized onions.",
        "base_price": 320, "is_veg": False, "spicy_level": "Extra Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Country Chicken", "Guntur Red Chillies", "Onions", "Ghee", "Curry Leaves"],
        "tags": ["guntur chicken", "extra spicy", "andhra special", "chicken fry", "starter"],
        "calories_kcal": 440
    },
    {
        "name": "Chicken Sholay Kebab",
        "category": "Starters",
        "description": "Crunchy boneless chicken morsels batter-fried with crushed black pepper, tossed with whisked egg white and fresh cilantro.",
        "base_price": 330, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Chicken Breast", "Egg White", "Crushed Peppercorns", "Green Herbs", "Lemon"],
        "tags": ["sholay kebab", "boneless kebab", "crisp chicken", "starters"],
        "calories_kcal": 410
    },
    {
        "name": "Paneer 65 Crisp Bites",
        "category": "Starters",
        "description": "Golden crispy malai paneer cubes tossed in spiced yogurt temper, green chillies, and aromatic curry leaves.",
        "base_price": 270, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Fresh Paneer", "Spiced Curd", "Curry Leaves", "Kashmiri Chilli", "Ginger"],
        "tags": ["paneer 65", "veg starter", "crispy paneer", "cottage cheese"],
        "calories_kcal": 390
    },
    {
        "name": "Baby Corn Manchurian Dry",
        "category": "Starters",
        "description": "Tender crunchy baby corn spears tossed in dark soya glaze, spring onions, chopped garlic, and crushed red chillies.",
        "base_price": 240, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Baby Corn", "Spring Onions", "Garlic", "Soy Sauce", "Green Chillies"],
        "tags": ["baby corn", "crispy", "veg manchurian", "indo chinese", "starter"],
        "calories_kcal": 310
    },
    {
        "name": "Mutton Sukka Fry",
        "category": "Starters",
        "description": "Slow-braised tender baby mutton roasted dry with grated coconut, peppercorns, fennel seeds, and caramelized shallots.",
        "base_price": 420, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Baby Goat Mutton", "Grated Coconut", "Fennel Seeds", "Black Pepper", "Shallots"],
        "tags": ["mutton sukka", "mutton fry", "cheft special", "spicy mutton"],
        "calories_kcal": 510
    },

    # Biryanis & Rice Mains
    {
        "name": "Meghana Special Chicken Biryani",
        "category": "Biryani & Rice",
        "description": "Layers of fragrant long-grain basmati rice served with specially spiced boneless chicken gravy, fried onions, and boiled egg. Served with mirchi ka salan and cooling raita.",
        "base_price": 340, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Aged Basmati Rice", "Boneless Chicken", "Brown Onions", "Ghee", "Boiled Egg", "Mint"],
        "tags": ["biryani", "chicken biryani", "meghana special", "bestseller", "dum biryani", "spicy rice"],
        "calories_kcal": 720
    },
    {
        "name": "Hyderabadi Mutton Dum Biryani",
        "category": "Biryani & Rice",
        "description": "Authentic Kachhi style dum biryani made with juicy marinated mutton cuts, saffron-infused aged basmati rice, slow-cooked on charcoal 'dum'.",
        "base_price": 390, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Goat Mutton", "Basmati Rice", "Pure Saffron", "Ghee", "Mint Leaves", "Yogurt"],
        "tags": ["mutton biryani", "hyderabadi biryani", "dum biryani", "royal feast", "lunch", "dinner"],
        "calories_kcal": 780
    },
    {
        "name": "Paneer Dum Biryani",
        "category": "Biryani & Rice",
        "description": "Fresh soft cottage cheese cubes layered with fragrant saffron basmati rice, caramelized onions, fresh mint, and whole garam masala.",
        "base_price": 280, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Fresh Paneer", "Basmati Rice", "Saffron Milk", "Caramelized Onions", "Ghee", "Cardamom"],
        "tags": ["paneer biryani", "veg biryani", "dum biryani", "vegetarian main"],
        "calories_kcal": 590
    },
    {
        "name": "Raju Gari Kodi Pulao",
        "category": "Biryani & Rice",
        "description": "Rustic Bhimavaram style chicken pulao made with short-grain Chittimutyalu rice, fresh mint, green chillies, and country chicken cooked in desi ghee.",
        "base_price": 330, "is_veg": False, "spicy_level": "Extra Spicy",
        "dietary_tags": ["Halal"],
        "ingredients": ["Chittimutyalu Rice", "Chicken", "Desi Ghee", "Green Chillies", "Mint", "Coriander"],
        "tags": ["kodi pulao", "andhra pulao", "raju gari", "traditional rice"],
        "calories_kcal": 680
    },
    {
        "name": "Prawns Fry Biryani",
        "category": "Biryani & Rice",
        "description": "Plump coastal tiger prawns shallow fried in Andhra masalas and layered over steaming aromatic biryani rice. Served with spicy gravy and raita.",
        "base_price": 390, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "Pescatarian", "High-Protein"],
        "ingredients": ["Tiger Prawns", "Basmati Rice", "Andhra Spice Paste", "Fried Onions", "Curd"],
        "tags": ["prawn biryani", "seafood", "prawns fry", "coastal biryani"],
        "calories_kcal": 640
    },
    {
        "name": "Egg Dum Biryani",
        "category": "Biryani & Rice",
        "description": "Roasted boiled eggs coated in thick spicy masala gravy, tucked into long-grain basmati biryani rice with caramelized shallots.",
        "base_price": 240, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal"],
        "ingredients": ["Farm Eggs", "Basmati Rice", "Brown Onions", "Ghee", "Biryani Masala"],
        "tags": ["egg biryani", "egg dum biryani", "budget biryani", "protein"],
        "calories_kcal": 560
    },
    {
        "name": "Ghee Rice with Dal & Sambar",
        "category": "Biryani & Rice",
        "description": "Fragrant steamed Jeerakasala rice tempered in rich cow ghee, whole cashews, cloves, and bay leaf. Served with thick Andhra dal.",
        "base_price": 210, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Jeera Rice", "Pure Cow Ghee", "Cashew Nuts", "Cloves", "Bay Leaf"],
        "tags": ["ghee rice", "comfort food", "south indian rice", "mild rice"],
        "calories_kcal": 510
    },
    {
        "name": "Andhra Curd Rice (Bagala Bath)",
        "category": "Biryani & Rice",
        "description": "Cooling home-style curd rice mashed with fresh milk, tempered with mustard seeds, ginger, green chillies, curry leaves, and pomegranate pearls.",
        "base_price": 160, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Cooked Rice", "Fresh Curd", "Mustard Seeds", "Curry Leaves", "Pomegranate"],
        "tags": ["curd rice", "bagala bath", "cooling", "digestive", "comfort food"],
        "calories_kcal": 320
    },

    # Main Course Curries & Meals
    {
        "name": "Natu Kodi Pulusu (Country Chicken Curry)",
        "category": "Main Course",
        "description": "Traditional spicy Andhra country chicken curry simmered in poppy seeds, roasted coriander, tamarind, and hot red chillies.",
        "base_price": 360, "is_veg": False, "spicy_level": "Extra Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Country Chicken", "Poppy Seeds", "Tamarind", "Red Chilli Powder", "Shallots"],
        "tags": ["natu kodi", "chicken curry", "andhra pulusu", "spicy curry"],
        "calories_kcal": 520
    },
    {
        "name": "Gongura Mutton Curry",
        "category": "Main Course",
        "description": "Succulent chunks of bone-in mutton cooked with tangy sorrel (gongura) leaves, garlic, and coarse ground Andhra masala.",
        "base_price": 430, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Mutton Chunks", "Gongura Sorrel Leaves", "Garlic", "Coriander", "Ghee"],
        "tags": ["gongura mutton", "tangy mutton", "andhra specialty", "traditional curry"],
        "calories_kcal": 580
    },
    {
        "name": "Nagarjuna Andhra Meal Combo",
        "category": "Main Course",
        "description": "Full traditional banana-leaf style Andhra meal with unlimited rice, Pappu (dal), Sambar, Rasam, Majjiga Pulusu, Gunpowder (Podi) with Pure Ghee, and Curd.",
        "base_price": 280, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Steamed Sona Masoori Rice", "Toor Dal Pappu", "Sambar", "Rasam", "Kandi Podi", "Desi Ghee"],
        "tags": ["andhra meal", "thali", "veg thali", "pappu", "ghee podi", "bestseller"],
        "calories_kcal": 750
    },
    {
        "name": "Butter Chicken Empire Style",
        "category": "Main Course",
        "description": "Shredded tandoori chicken simmered in rich buttery tomato sauce, scented with dried fenugreek leaves (kasuri methi) and fresh cream.",
        "base_price": 340, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal"],
        "ingredients": ["Tandoori Chicken", "Tomatoes", "Butter", "Fresh Cream", "Kasuri Methi"],
        "tags": ["butter chicken", "creamy curry", "empire special", "murgh makhani"],
        "calories_kcal": 610
    },
    {
        "name": "Tomato Pappu (Andhra Dal)",
        "category": "Main Course",
        "description": "Slow cooked yellow toor lentils simmered with country tomatoes, tempered in ghee with mustard seeds, cumin, garlic, and dry red chillies.",
        "base_price": 190, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Toor Dal", "Country Tomatoes", "Ghee", "Garlic", "Mustard Seeds", "Dry Chillies"],
        "tags": ["tomato pappu", "andhra dal", "lentil curry", "homestyle"],
        "calories_kcal": 290
    },

    # Breads
    {
        "name": "Coin Parotta (3 Pcs)",
        "category": "Breads",
        "description": "Flaky, multi-layered miniature Malabar style parottas kneaded with pure ghee and crushed on the tawa for maximum crispness.",
        "base_price": 90, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Refined Flour", "Ghee", "Milk", "Salt"],
        "tags": ["coin parotta", "parotta", "malabar bread", "flaky"],
        "calories_kcal": 340
    },
    {
        "name": "Butter Garlic Naan",
        "category": "Breads",
        "description": "Tandoor baked leavened bread brushed generously with salted butter and topped with roasted minced garlic and coriander.",
        "base_price": 85, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Wheat Flour", "Garlic", "Butter", "Coriander", "Yeast"],
        "tags": ["garlic naan", "butter naan", "tandoori bread"],
        "calories_kcal": 280
    },
    {
        "name": "Roomali Roti",
        "category": "Breads",
        "description": "Handkerchief-thin soft unleavened bread stretched and tossed over an inverted domed iron griddle (kadai).",
        "base_price": 60, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Wheat & Refined Flour", "Water", "Salt"],
        "tags": ["roomali roti", "thin bread", "soft roti"],
        "calories_kcal": 180
    },

    # Desserts & Beverages
    {
        "name": "Double Ka Meetha",
        "category": "Desserts",
        "description": "Hyderabadi royal dessert of crisp fried bread triangles soaked in reduced saffron cardamom rabdi, garnished with slivered pistachios and almonds.",
        "base_price": 160, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Bread", "Whole Milk", "Saffron", "Cardamom", "Pistachios", "Ghee"],
        "tags": ["double ka meetha", "hyderabadi sweet", "shahi tukda", "dessert"],
        "calories_kcal": 410
    },
    {
        "name": "Matka Phirni",
        "category": "Desserts",
        "description": "Slow-chilled ground basmati rice pudding cooked with sweet condensed milk, scented with kewra water and green cardamom, served in clay earthen pots.",
        "base_price": 140, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Ground Rice", "Full Cream Milk", "Sugar", "Kewra", "Cardamom", "Almonds"],
        "tags": ["phirni", "matka phirni", "kheer", "sweet", "dessert"],
        "calories_kcal": 310
    },
    {
        "name": "Spiced Masala Buttermilk (Chaas)",
        "category": "Beverages",
        "description": "Refreshing churned yogurt cooler infused with crushed ginger, green chilli, fresh curry leaves, coriander, and black rock salt.",
        "base_price": 70, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Churned Curd", "Ginger", "Curry Leaves", "Green Chilli", "Black Salt"],
        "tags": ["buttermilk", "chaas", "cooler", "probiotic", "beverage"],
        "calories_kcal": 80
    }
]


NORTH_INDIAN_DISHES = [
    # Starters
    {
        "name": "Murgh Malai Tikka",
        "category": "Starters",
        "description": "Melt-in-mouth chicken supreme cubes steeped in rich cream cheese marinade, scented with green cardamom, mace, and roasted in clay tandoor.",
        "base_price": 380, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein", "Keto-Friendly"],
        "ingredients": ["Chicken Breast", "Cream Cheese", "Heavy Cream", "Cardamom", "Cashew Paste"],
        "tags": ["malai tikka", "creamy kebab", "tandoori chicken", "starter", "bestseller"],
        "calories_kcal": 460
    },
    {
        "name": "Tandoori Murgh (Half)",
        "category": "Starters",
        "description": "Whole chicken bone-in legs and breasts marinated in strained yogurt, mustard oil, Degi red chilli, and roasted tandoori garam masala.",
        "base_price": 360, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein", "Keto-Friendly"],
        "ingredients": ["Chicken Bone-in", "Hung Curd", "Mustard Oil", "Kashmiri Mirch", "Tandoori Spices"],
        "tags": ["tandoori chicken", "roast chicken", "tandoor", "classic starter"],
        "calories_kcal": 510
    },
    {
        "name": "Galouti Kebab with Mini Mughlai Paratha",
        "category": "Starters",
        "description": "Fine minced lamb patties infused with raw papaya, rose petals, and 32 Awadhi potli spices, pan-seared in desi ghee on a mahi tawa.",
        "base_price": 460, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Minced Lamb", "Raw Papaya", "Desi Ghee", "Potli Spices", "Saffron"],
        "tags": ["galouti kebab", "lucknowi", "melt in mouth", "lamb kebab", "signature"],
        "calories_kcal": 480
    },
    {
        "name": "Mutton Seekh Kebab",
        "category": "Starters",
        "description": "Succulent spiced minced mutton skewered on iron rods and charred over glowing charcoal embers, garnished with onion rings and lemon.",
        "base_price": 420, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein", "Keto-Friendly"],
        "ingredients": ["Minced Mutton", "Ginger", "Garlic", "Coriander", "Cumin", "Mint"],
        "tags": ["seekh kebab", "mutton kebab", "bbq", "tandoor starter"],
        "calories_kcal": 440
    },
    {
        "name": "Dhungar Paneer Tikka",
        "category": "Starters",
        "description": "Thick slabs of malai paneer layered with bell peppers and onions, marinated in smoked ajwain and curd, roasted in clay oven with charcoal smoke.",
        "base_price": 320, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Malai Paneer", "Hung Curd", "Ajwain", "Bell Peppers", "Mustard Oil"],
        "tags": ["paneer tikka", "dhungar", "smoked paneer", "veg starter", "tandoori"],
        "calories_kcal": 420
    },
    {
        "name": "Dahi Ke Kebab",
        "category": "Starters",
        "description": "Crisp golden croquettes filled with velvety hung yogurt, crushed green chillies, cracked coriander seeds, and fresh mint.",
        "base_price": 290, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Hung Curd", "Paneer", "Roasted Gram Flour", "Green Chillies", "Mint"],
        "tags": ["dahi ke kebab", "soft kebab", "vegetarian starter", "delicacy"],
        "calories_kcal": 350
    },
    {
        "name": "Amritsari Fish Fry",
        "category": "Starters",
        "description": "Sole fish fillets battered in coarse carom-seed spiced gram flour, deep fried until crackling crisp, dusted with tangy chaat masala.",
        "base_price": 410, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "Pescatarian", "High-Protein"],
        "ingredients": ["Sole Fish", "Besan (Gram Flour)", "Ajwain (Carom Seeds)", "Chilli Powder", "Lemon"],
        "tags": ["amritsari fish", "fish fry", "punjabi fish", "crispy starter"],
        "calories_kcal": 390
    },
    {
        "name": "Crispy Cajun Spiced Potatoes",
        "category": "Starters",
        "description": "Crispy pressed baby potatoes drizzled with smoky Cajun spiced mayonnaise dressing, fresh herbs, and chopped spring onions.",
        "base_price": 260, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Baby Potatoes", "Cajun Seasoning", "Mayonnaise", "Paprika", "Spring Onions"],
        "tags": ["cajun potatoes", "crispy potatoes", "barbeque nation style", "snack"],
        "calories_kcal": 380
    },

    # Mains
    {
        "name": "Classic Butter Chicken 1947",
        "category": "Main Course",
        "description": "The quintessential North Indian curry: Charred tandoori chicken cooked in velvety sun-ripened tomato sauce with loads of butter, cream, and aromatic fenugreek.",
        "base_price": 380, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal"],
        "ingredients": ["Tandoori Chicken Chunks", "Tomatoes", "White Butter", "Heavy Cream", "Kasuri Methi"],
        "tags": ["butter chicken", "murgh makhani", "delhi style", "creamy chicken", "bestseller"],
        "calories_kcal": 650
    },
    {
        "name": "Slow-Simmered Dal Makhani",
        "category": "Main Course",
        "description": "Whole black urad lentils and kidney beans simmered overnight for 16 hours over low charcoal embers with butter, cream, and ripe tomatoes.",
        "base_price": 290, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Black Urad Dal", "Rajma", "Butter", "Fresh Cream", "Tomato Puree", "Ginger"],
        "tags": ["dal makhani", "dal bukhara", "creamy dal", "punjabi dal", "bestseller"],
        "calories_kcal": 490
    },
    {
        "name": "Paneer Lababdar",
        "category": "Main Course",
        "description": "Fresh cottage cheese cubes in rich onion-tomato gravy with grated paneer, toasted cashews, and sweet aromatic whole spices.",
        "base_price": 320, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Malai Paneer", "Tomatoes", "Onions", "Cashews", "Butter", "Kasuri Methi"],
        "tags": ["paneer lababdar", "rich paneer", "cottage cheese curry", "veg main course"],
        "calories_kcal": 530
    },
    {
        "name": "Kadhai Paneer Punjabi",
        "category": "Main Course",
        "description": "Cubes of paneer stir fried in an iron wok with bell peppers, onion petals, fresh ginger juliennes, and coarsely crushed coriander and dry chillies.",
        "base_price": 310, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Paneer", "Capsicum", "Onions", "Coriander Seeds", "Kashmiri Chilli", "Tomatoes"],
        "tags": ["kadhai paneer", "spicy paneer", "capsicum", "punjabi sabzi"],
        "calories_kcal": 460
    },
    {
        "name": "Raan-e-Sikandari (Braised Lamb Leg)",
        "category": "Main Course",
        "description": "Whole leg of spring lamb marinated for 24 hours in malt vinegar, dark rum, and spices, slow braised until meltingly tender and succulent.",
        "base_price": 890, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Lamb Leg", "Malt Vinegar", "Ghee", "Potli Masala", "Cinnamon", "Saffron"],
        "tags": ["raan", "sikandari raan", "royal lamb", "luxury dining"],
        "calories_kcal": 820
    },
    {
        "name": "Highway Dhaba Murgh Curry",
        "category": "Main Course",
        "description": "Homestyle rustic bone-in chicken curry cooked in cold pressed mustard oil, coarse crushed onion, garlic, and freshly pounded garam masala.",
        "base_price": 350, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Bone-in Chicken", "Mustard Oil", "Pounded Garam Masala", "Tomatoes", "Garlic"],
        "tags": ["dhaba chicken", "highway chicken", "spicy chicken curry", "homestyle"],
        "calories_kcal": 540
    },
    {
        "name": "Amritsari Chole with 2 Bhature",
        "category": "Main Course",
        "description": "Dark spicy Amritsari chickpeas brewed with tea leaves and dried anardana (pomegranate seeds), served with two ballooning fluffy bhaturas and pickles.",
        "base_price": 260, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Kabuli Chana", "Anardana", "Black Tea Decoction", "Refined Flour", "Pickled Green Chillies"],
        "tags": ["chole bhature", "amritsari chole", "punjabi breakfast", "bestseller"],
        "calories_kcal": 780
    },
    {
        "name": "Sarson Da Saag & 2 Makki Di Roti",
        "category": "Main Course",
        "description": "Winter delicacy: fresh mustard greens, spinach, and bathua slow cooked in earthen handi, served with yellow cornmeal flatbreads and white butter with jaggery.",
        "base_price": 280, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Mustard Greens", "Spinach", "Corn Flour", "White Butter (Makhan)", "Jaggery", "Garlic"],
        "tags": ["sarson saag", "makki roti", "punjabi winter feast", "authentic"],
        "calories_kcal": 520
    },

    # Rice, Breads & Accompaniments
    {
        "name": "Amritsari Aloo Pyaaz Kulcha",
        "category": "Breads",
        "description": "Layered crisp tandoori flatbread stuffed with spiced crushed potatoes, onions, coriander seeds, and dry mango powder, topped with butter.",
        "base_price": 120, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Refined Flour", "Potatoes", "Onions", "Butter", "Amchur", "Coriander"],
        "tags": ["amritsari kulcha", "stuffed kulcha", "tandoori bread"],
        "calories_kcal": 360
    },
    {
        "name": "Cheese Garlic Naan",
        "category": "Breads",
        "description": "Oven baked leavened bread stuffed with melted mozzarella and cheddar cheese, sprinkled with chopped garlic and green chillies.",
        "base_price": 130, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Flour", "Mozzarella Cheese", "Cheddar", "Roasted Garlic", "Butter"],
        "tags": ["cheese naan", "garlic naan", "cheesy bread", "indulgent"],
        "calories_kcal": 390
    },
    {
        "name": "Desi Ghee Rajma Chawal Bowl",
        "category": "Biryani & Rice",
        "description": "Slow cooked Jammu rajma in aromatic homestyle gravy served over steaming basmati rice, topped with a dollop of pure desi ghee and onion salad.",
        "base_price": 220, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Red Kidney Beans", "Basmati Rice", "Desi Ghee", "Tomatoes", "Ginger"],
        "tags": ["rajma chawal", "comfort bowl", "homestyle punjabi", "healthy meal"],
        "calories_kcal": 510
    },
    {
        "name": "Lucknowi Murgh Dum Biryani",
        "category": "Biryani & Rice",
        "description": "Awadhi style perfumed biryani cooked with chicken in sealed handi, scented with kewra, ittr, saffron, and sweet spices.",
        "base_price": 360, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal"],
        "ingredients": ["Basmati Rice", "Tender Chicken", "Saffron", "Kewra", "Ghee", "Milk"],
        "tags": ["lucknowi biryani", "awadhi biryani", "mild biryani", "perfumed rice"],
        "calories_kcal": 670
    },

    # Desserts & Beverages
    {
        "name": "Moong Dal Halwa Desi Ghee",
        "category": "Desserts",
        "description": "Rich golden yellow split lentil pudding roasted patiently in desi ghee, blended with mawa, cardamom, and toasted cashew nuts.",
        "base_price": 170, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Yellow Moong Dal", "Desi Ghee", "Khoya (Mawa)", "Sugar", "Cardamom", "Cashews"],
        "tags": ["moong dal halwa", "desi ghee sweet", "punjabi halwa", "dessert"],
        "calories_kcal": 470
    },
    {
        "name": "Angoori Gulab Jamun with Rabdi",
        "category": "Desserts",
        "description": "Miniature deep-fried milk dumplings soaked in rose sugar syrup, served swimming in chilled thick cardamom and saffron rabdi.",
        "base_price": 160, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Mawa Khoya", "Reduced Milk Rabdi", "Rose Water", "Cardamom", "Saffron"],
        "tags": ["gulab jamun", "rabdi", "angoori jamun", "indian dessert"],
        "calories_kcal": 420
    },
    {
        "name": "Patiala Malai Lassi (500ml)",
        "category": "Beverages",
        "description": "Thick sweet yogurt whipped to creamy perfection, served in an earthen clay kulhad with a dollop of fresh clotted cream (malai) and pistachios.",
        "base_price": 130, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Full Cream Curd", "Sugar", "Malai Clotted Cream", "Pistachios", "Cardamom"],
        "tags": ["patiala lassi", "sweet lassi", "kulhad lassi", "punjabi drink"],
        "calories_kcal": 380
    }
]


SOUTH_INDIAN_DISHES = [
    # Breakfast & Tiffin
    {
        "name": "Crispy Benne Masala Dosa",
        "category": "Breakfast & Tiffin",
        "description": "Golden crisp roasted crepe slathered with freshly churned white butter, smeared with spicy red garlic chutney, filled with mashed spiced potatoes.",
        "base_price": 130, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Fermented Rice & Urad Dal Batter", "White Butter (Benne)", "Spiced Potato Mash", "Red Garlic Chutney"],
        "tags": ["masala dosa", "benne dosa", "ctr style", "vidyarthi bhavan", "bestseller", "crispy"],
        "calories_kcal": 480
    },
    {
        "name": "Steamed Thatte Idli with Pure Ghee",
        "category": "Breakfast & Tiffin",
        "description": "Plate-sized ultra soft and fluffy steamed rice cake drenched in steaming homemade cow ghee, served with spicy gun powder and fresh coconut chutney.",
        "base_price": 85, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Rice Rava", "Urad Dal", "Pure Cow Ghee", "Chutney Pudi", "Coconut Chutney"],
        "tags": ["thatte idli", "steamed idli", "brahmins style", "healthy breakfast", "soft idli"],
        "calories_kcal": 320
    },
    {
        "name": "Crisp Golden Medu Vada (2 Pcs)",
        "category": "Breakfast & Tiffin",
        "description": "Crispy fried lentil fritters crunchy on the outside and airy inside, seasoned with crushed black pepper, fresh ginger, and curry leaves. Served with hot sambar.",
        "base_price": 80, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Urad Dal", "Crushed Black Pepper", "Ginger", "Curry Leaves", "Coconut Chutney"],
        "tags": ["medu vada", "vada sambar", "crispy vada", "breakfast snack"],
        "calories_kcal": 340
    },
    {
        "name": "Chow Chow Bath (Khara & Kesari)",
        "category": "Breakfast & Tiffin",
        "description": "The classic Karnataka pairing: one scoop of spicy vegetable semolina upma (Khara Bath) paired with one scoop of rich pineapple saffron halwa (Kesari Bath).",
        "base_price": 110, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Roasted Semolina", "Ghee", "Pineapple", "Mixed Vegetables", "Cashews", "Mustard Seeds"],
        "tags": ["chow chow bath", "khara bath", "kesari bath", "taaza thindi", "karnataka breakfast"],
        "calories_kcal": 450
    },
    {
        "name": "Original Rava Idli with Potato Sagoo",
        "category": "Breakfast & Tiffin",
        "description": "MTR's world famous steamed semolina cake tempered in ghee with mustard, green chillies, ginger, grated carrots, and whole roasted cashews. Served with sagoo.",
        "base_price": 95, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Semolina (Rava)", "Curd", "Ghee", "Cashew Nuts", "Carrots", "Potato Sagoo"],
        "tags": ["rava idli", "mtr special", "heritage breakfast", "healthy"],
        "calories_kcal": 310
    },
    {
        "name": "Open Butter Masala Dosa",
        "category": "Breakfast & Tiffin",
        "description": "Thick spongy dosa roasted open with generous dollops of butter, sprinkled generously with spicy gunpowder (chutney podi) and topped with potato palya.",
        "base_price": 140, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Dosa Batter", "Pure Butter", "Kandi Podi", "Potato Mash", "Coriander"],
        "tags": ["open dosa", "butter podi dosa", "bangalore tiffin"],
        "calories_kcal": 510
    },
    {
        "name": "Poori Saagu (3 Pcs)",
        "category": "Breakfast & Tiffin",
        "description": "Golden puffed whole wheat pooris served with mild vegetable coconut gravy (Bombay Saagu) spiced with green chillies, cloves, and cinnamon.",
        "base_price": 100, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Whole Wheat Flour", "Potatoes", "Mixed Veggies", "Coconut Milk", "Spices"],
        "tags": ["poori saagu", "puffed poori", "morning breakfast"],
        "calories_kcal": 460
    },
    {
        "name": "Ghee Paper Roast Dosa",
        "category": "Breakfast & Tiffin",
        "description": "Extra thin, wafer-like, two-feet long conical dosa crisped to golden perfection with pure clarified ghee. Served with three types of chutneys and sambar.",
        "base_price": 150, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Rice Batter", "Desi Ghee", "Coconut Chutney", "Tomato Chutney", "Sambar"],
        "tags": ["paper roast", "ghee dosa", "a2b special", "crispy"],
        "calories_kcal": 420
    },

    # Coastal & Regional Specialties
    {
        "name": "Mangalorean Chicken Ghee Roast",
        "category": "Coastal & Regional",
        "description": "Tender chicken morsels slow-roasted in copious amounts of country ghee with freshly ground Byadgi chilli paste, coriander, cumin, and fenugreek.",
        "base_price": 380, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein", "Gluten-Free"],
        "ingredients": ["Chicken Chunks", "Desi Ghee", "Byadgi Red Chillies", "Tamarind", "Peppercorns", "Garlic"],
        "tags": ["ghee roast", "chicken ghee roast", "mangalorean", "kudla", "bestseller", "signature"],
        "calories_kcal": 590
    },
    {
        "name": "Anjal (Seer Fish) Tawa Fry",
        "category": "Coastal & Regional",
        "description": "Thick cut King Fish (Surmai/Anjal) steak coated in fiery red Mangalorean spice paste and shallow fried on iron tawa with curry leaves.",
        "base_price": 480, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Pescatarian", "High-Protein", "Gluten-Free"],
        "ingredients": ["Seer Fish (Surmai)", "Red Chilli Paste", "Tamarind", "Ginger Garlic", "Curry Leaves"],
        "tags": ["anjal fry", "seer fish", "surmai fry", "seafood", "mangalorean"],
        "calories_kcal": 420
    },
    {
        "name": "Prawns Ghee Roast",
        "category": "Coastal & Regional",
        "description": "Fresh sea prawns tossed in roasted ground masala and bubbling pure cow ghee until deeply caramelized and aromatic.",
        "base_price": 440, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Pescatarian", "High-Protein", "Gluten-Free"],
        "ingredients": ["Tiger Prawns", "Cow Ghee", "Byadgi Chillies", "Curry Leaves", "Garlic"],
        "tags": ["prawns ghee roast", "coastal prawns", "seafood special"],
        "calories_kcal": 510
    },
    {
        "name": "Kori Rotti Mangalore Feast",
        "category": "Coastal & Regional",
        "description": "Crisp sun-dried rice wafers (rotti) served with rich, spicy Mangalorean red chicken curry infused with fresh coconut milk.",
        "base_price": 330, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "Gluten-Free"],
        "ingredients": ["Crispy Rice Rotti", "Country Chicken", "Fresh Coconut Milk", "Byadgi Masala"],
        "tags": ["kori rotti", "mangalorean classic", "chicken curry", "crunchy"],
        "calories_kcal": 610
    },
    {
        "name": "Soft Neer Dosa (3 Pcs)",
        "category": "Coastal & Regional",
        "description": "Delicate, feather-light, lacy water crepes prepared from ground raw rice. Served with spicy chutney or coconut jaggery mixture.",
        "base_price": 110, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Vegan", "Gluten-Free"],
        "ingredients": ["Raw Rice", "Water", "Salt", "Grated Coconut"],
        "tags": ["neer dosa", "mangalore dosa", "soft crepe", "light dinner"],
        "calories_kcal": 240
    },
    {
        "name": "North Karnataka Jolada Roti Oota",
        "category": "Coastal & Regional",
        "description": "Healthy North Karnataka meal: 2 crisp Jowar (Sorghum) rotis served with Ennegayi (stuffed brinjal), Shenga (peanut) chutney pudi, sprouts curry, and curd.",
        "base_price": 240, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Jowar Flour", "Small Brinjals", "Roasted Peanuts", "Garlic", "Sprouted Moong"],
        "tags": ["jolada roti", "ennegayi", "north karnataka", "healthy thali", "gluten free"],
        "calories_kcal": 540
    },

    # Rice, Meals & Sweets
    {
        "name": "Bisi Bele Bath with Boondi",
        "category": "Rice & Meals",
        "description": "Traditional Karnataka one-pot rice and lentil dish cooked with vegetables, tamarind, nutmeg, and aromatic Bisi Bele Bath masala, topped with ghee and boondi.",
        "base_price": 140, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Rice", "Toor Dal", "Carrots & Beans", "Desi Ghee", "Tamarind", "Khara Boondi"],
        "tags": ["bisi bele bath", "karnataka rice", "spicy sambar rice", "comfort meal"],
        "calories_kcal": 460
    },
    {
        "name": "Special South Indian Meals (Silver Thali)",
        "category": "Rice & Meals",
        "description": "Grand festive platter with sweet payasam, poori, steamed rice, sambar, rasam, palya (dry veg), kootu, curd, appalam, and pickle.",
        "base_price": 250, "is_veg": True, "spicy_level": "Medium",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Sona Masoori Rice", "Udupi Sambar", "Pepper Rasam", "Vegetable Poriyal", "Curd", "Payasam"],
        "tags": ["south indian meals", "thali", "udupi meals", "full lunch"],
        "calories_kcal": 780
    },
    {
        "name": "Badam Halwa Pure Ghee",
        "category": "Desserts",
        "description": "Decadent royal sweet made from blanched California almonds ground into paste, roasted slowly in desi cow ghee, scented with saffron and cardamom.",
        "base_price": 180, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Almonds (Badam)", "Desi Cow Ghee", "Sugar", "Saffron", "Cardamom"],
        "tags": ["badam halwa", "almond halwa", "mtr sweet", "rich dessert"],
        "calories_kcal": 420
    },
    {
        "name": "Ghee Mysore Pak",
        "category": "Desserts",
        "description": "Traditional melt-in-the-mouth sweet created for the Maharaja of Mysore, prepared from roasted gram flour, sugar syrup, and clarified butter.",
        "base_price": 120, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Besan (Gram Flour)", "Pure Cow Ghee", "Sugar"],
        "tags": ["mysore pak", "ghee sweet", "traditional sweet"],
        "calories_kcal": 380
    },
    {
        "name": "Traditional South Indian Filter Kaapi",
        "category": "Beverages",
        "description": "Freshly brewed dark decoction of 80:20 chicory-blend plantation beans frothed with boiled full cream milk in a brass dabarah and tumbler.",
        "base_price": 50, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Filter Coffee Decoction", "Boiled Full Cream Milk", "Sugar"],
        "tags": ["filter coffee", "filter kaapi", "dabarah coffee", "iconic drink"],
        "calories_kcal": 110
    }
]


AMERICAN_BURGERS_DISHES = [
    # Burgers
    {
        "name": "All American Cheese Burger",
        "category": "Burgers",
        "description": "Juicy grilled beef or chicken patty topped with melted American cheddar, crisp lettuce, gherkins, caramelized onions, and house secret burger relish on toasted brioche.",
        "base_price": 270, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Seasoned Patty", "Cheddar Cheese", "Brioche Bun", "Lettuce", "Gherkins", "Secret Sauce"],
        "tags": ["cheeseburger", "truffles", "american burger", "bestseller", "classic burger"],
        "calories_kcal": 680
    },
    {
        "name": "Sloppy Joe BBQ Burger",
        "category": "Burgers",
        "description": "Savory minced chicken or tender beef simmered in sweet smoky barbecue tomato glaze, spilling out of a buttered sesame bun with melted cheese.",
        "base_price": 290, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Minced Chicken/Beef", "BBQ Sauce", "Sesame Bun", "Melted Cheese", "Jalapenos"],
        "tags": ["sloppy joe", "bbq burger", "juicy burger", "comfort food"],
        "calories_kcal": 640
    },
    {
        "name": "Crispy Zinger Chicken Fillet Burger",
        "category": "Burgers",
        "description": "Double-dredged extra crispy fried chicken breast fillet topped with creamy iceberg slaw and spicy pepper mayo in a toasted potato bun.",
        "base_price": 250, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Crispy Chicken Breast", "Iceberg Slaw", "Black Pepper Mayo", "Potato Bun"],
        "tags": ["zinger", "crispy chicken burger", "fried chicken", "bestseller"],
        "calories_kcal": 620
    },
    {
        "name": "Juicy Lucy Molten Cheese Burger",
        "category": "Burgers",
        "description": "Minneapolis style stuffed burger: premium meat patty stuffed inside with a core of molten cheddar that oozes out upon the first bite.",
        "base_price": 360, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Stuffed Beef/Lamb Patty", "Molten Cheddar Core", "Caramelized Onions", "Brioche Bun"],
        "tags": ["juicy lucy", "molten cheese", "stuffed burger", "plan b"],
        "calories_kcal": 780
    },
    {
        "name": "Lucien Portobello Veg Burger",
        "category": "Burgers",
        "description": "Gourmet thick-cut Portobello mushroom cap crumb-fried with French herbs, topped with aged provolone, sun-dried tomatoes, and truffle emulsion.",
        "base_price": 340, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Portobello Mushroom", "Provolone Cheese", "Sun-dried Tomatoes", "Truffle Mayo", "Brioche Bun"],
        "tags": ["portobello burger", "veg burger", "gourmet burger", "burger seigneur"],
        "calories_kcal": 530
    },
    {
        "name": "Baconator Supreme Burger",
        "category": "Burgers",
        "description": "Two quarter-pound beef patties, multiple strips of crispy smoked bacon, two slices of American cheese, mayonnaise, and ketchup on a toasted bun.",
        "base_price": 380, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Double Beef Patty", "Smoked Bacon Strips", "American Cheese", "Mayo", "Toasted Bun"],
        "tags": ["baconator", "wendys", "bacon burger", "heavy burger"],
        "calories_kcal": 890
    },
    {
        "name": "Spicy Bean & Jalapeno Veggie Burger",
        "category": "Burgers",
        "description": "Hearty patty made from black beans, sweet corn, and quinoa, topped with fiery jalapenos, Monterey Jack cheese, and chipotle mayo.",
        "base_price": 220, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Black Bean Corn Patty", "Pickled Jalapenos", "Monterey Jack", "Chipotle Mayo"],
        "tags": ["veggie burger", "spicy bean burger", "vegetarian"],
        "calories_kcal": 470
    },

    # Wings & Fried Chicken
    {
        "name": "Fiery Buffalo Chicken Wings (8 Pcs)",
        "category": "Wings & Chicken",
        "description": "Crispy fried chicken wings tossed in tangy cayenne pepper Frank's RedHot sauce and butter, served with crisp celery sticks and blue cheese dip.",
        "base_price": 320, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Chicken Wings", "Buffalo Hot Sauce", "Butter", "Blue Cheese Dressing", "Celery"],
        "tags": ["buffalo wings", "hot wings", "plan b", "spicy wings", "starter"],
        "calories_kcal": 560
    },
    {
        "name": "Smoky Honey BBQ Wings (8 Pcs)",
        "category": "Wings & Chicken",
        "description": "Tender chicken wings slow-baked and glazed with rich smoked hickory BBQ sauce, pure honey, and toasted white sesame seeds.",
        "base_price": 320, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Chicken Wings", "Smoky Hickory BBQ Sauce", "Honey", "Sesame Seeds"],
        "tags": ["bbq wings", "honey bbq", "sweet wings", "appetizer"],
        "calories_kcal": 530
    },
    {
        "name": "Louisiana Cajun Fried Chicken (4 Pcs)",
        "category": "Wings & Chicken",
        "description": "Authentic Louisiana bone-in chicken marinated for 12 hours in spicy buttermilk brine, tossed in seasoned flour and fried to super crunchy crispiness.",
        "base_price": 340, "is_veg": False, "spicy_level": "Medium",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Bone-in Chicken", "Buttermilk Brine", "Cajun Seasoning", "Crispy Batter"],
        "tags": ["popeyes", "fried chicken", "cajun chicken", "crispy chicken"],
        "calories_kcal": 670
    },
    {
        "name": "Crispy Chicken Tenders with Honey Mustard",
        "category": "Wings & Chicken",
        "description": "Whole tender chicken breast strips seasoned, crumb-coated, and fried to golden perfection. Served with creamy honey Dijon dip.",
        "base_price": 270, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Chicken Tenders", "Panko Crumbs", "Honey Mustard Sauce"],
        "tags": ["chicken tenders", "chicken strips", "finger food", "kids favorite"],
        "calories_kcal": 440
    },

    # Sides & Fries
    {
        "name": "Peri Peri Melted Cheese Fries",
        "category": "Sides & Fries",
        "description": "Golden skin-on potato fries dusted with spicy African bird's eye peri-peri spice mix, smothered under warm melted cheddar cheese sauce.",
        "base_price": 190, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Potato Fries", "Peri Peri Seasoning", "Warm Cheddar Sauce", "Jalapenos"],
        "tags": ["peri peri fries", "cheese fries", "loaded fries", "truffles style"],
        "calories_kcal": 490
    },
    {
        "name": "Beer Battered Onion Rings",
        "category": "Sides & Fries",
        "description": "Colossal white onion rings dipped in craft beer batter and flash-fried until crackling crisp. Served with garlic herb ranch.",
        "base_price": 170, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["White Onions", "Craft Beer Batter", "Ranch Dip", "Sea Salt"],
        "tags": ["onion rings", "beer batter", "crispy rings", "bar snack"],
        "calories_kcal": 360
    },
    {
        "name": "Macaroni & Four Cheese Bake",
        "category": "Sides & Fries",
        "description": "Elbow macaroni enveloped in velvety roux of cheddar, mozzarella, parmesan, and Monterey Jack, topped with toasted herb panko crust.",
        "base_price": 280, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Macaroni", "Cheddar", "Parmesan", "Mozzarella", "Panko Crumbs"],
        "tags": ["mac and cheese", "four cheese", "baked pasta", "comfort food"],
        "calories_kcal": 590
    },

    # Desserts & Shakes
    {
        "name": "Warm Molten Skillet Brownie",
        "category": "Desserts",
        "description": "Decadent dark chocolate fudge brownie baked fresh in cast iron skillet, topped with rich hot chocolate fudge sauce and vanilla bean ice cream scoop.",
        "base_price": 220, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Dark Cocoa", "Fudge Brownie", "Vanilla Ice Cream", "Hot Chocolate Fudge"],
        "tags": ["skillet brownie", "hot fudge", "chilis style", "chocolate dessert"],
        "calories_kcal": 580
    },
    {
        "name": "Thick Chocolate Oreo Milkshake",
        "category": "Beverages",
        "description": "Ultra thick hand-spun shake made with rich Belgian chocolate ice cream, crushed Oreo cookies, and topped with whipped cream and chocolate drizzle.",
        "base_price": 180, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Chocolate Ice Cream", "Oreo Biscuits", "Whole Milk", "Whipped Cream"],
        "tags": ["oreo shake", "thickshake", "chocolate shake", "beverage"],
        "calories_kcal": 510
    }
]


ITALIAN_PIZZA_DISHES = [
    # Pizzas
    {
        "name": "Woodfired Margherita Verace Pizza",
        "category": "Pizzas",
        "description": "Authentic Neapolitan 11-inch sourdough pizza topped with crushed San Marzano tomato sauce, fresh buffalo mozzarella, aromatic sweet basil leaves, and extra virgin olive oil.",
        "base_price": 420, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Slow-fermented Sourdough", "San Marzano Tomatoes", "Fior di Latte Mozzarella", "Fresh Basil", "Extra Virgin Olive Oil"],
        "tags": ["margherita", "woodfired pizza", "neapolitan pizza", "sourdough", "bestseller", "classic italian"],
        "calories_kcal": 680
    },
    {
        "name": "Diavola Pepperoni Sourdough Pizza",
        "category": "Pizzas",
        "description": "Blistered crust pizza topped with spicy pork or chicken pepperoni, pickled jalapeño peppers, crushed red chillies, and creamy mozzarella.",
        "base_price": 540, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Sourdough Base", "Spicy Pepperoni Slices", "Tomato Sauce", "Mozzarella", "Jalapenos"],
        "tags": ["pepperoni pizza", "diavola", "spicy pizza", "brik oven", "meat pizza"],
        "calories_kcal": 760
    },
    {
        "name": "Tartufo Wild Mushroom & Truffle Pizza",
        "category": "Pizzas",
        "description": "White base pizza (Bianca) with sautéed wild porcini and button mushrooms, roasted garlic, smoked scamorza cheese, and aromatic Italian black truffle oil drizzle.",
        "base_price": 580, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Sourdough", "Wild Porcini Mushrooms", "Smoked Scamorza", "Black Truffle Oil", "Fior di Latte"],
        "tags": ["truffle pizza", "mushroom pizza", "white pizza", "gourmet", "chianti"],
        "calories_kcal": 690
    },
    {
        "name": "Burrata & Spiced Pesto Sourdough Pizza",
        "category": "Pizzas",
        "description": "Wood-fired crust topped with house basil walnut pesto, cherry confit tomatoes, and crowned with a fresh, creamy ball of torn Pugliese burrata.",
        "base_price": 560, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Burrata Cheese", "Genovese Pesto", "Cherry Tomatoes", "Sourdough Crust", "Pine Nuts"],
        "tags": ["burrata pizza", "pesto pizza", "artisanal", "fresh burrata"],
        "calories_kcal": 710
    },
    {
        "name": "Quattro Formaggi (Four Cheese) Pizza",
        "category": "Pizzas",
        "description": "Decadent four-cheese blend of aged gorgonzola blue cheese, fior di latte mozzarella, fontina, and shaved 24-month Parmigiano-Reggiano.",
        "base_price": 510, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Mozzarella", "Gorgonzola", "Parmigiano-Reggiano", "Fontina", "Olive Oil"],
        "tags": ["four cheese", "quattro formaggi", "cheesy pizza", "gourmet"],
        "calories_kcal": 750
    },
    {
        "name": "Peri Peri Grilled Chicken Pizza",
        "category": "Pizzas",
        "description": "Thin crispy crust topped with spicy peri-peri marinated grilled chicken chunks, roasted bell peppers, sliced red onions, and mozzarella.",
        "base_price": 460, "is_veg": False, "spicy_level": "Spicy",
        "dietary_tags": ["Halal", "High-Protein"],
        "ingredients": ["Peri Peri Chicken", "Bell Peppers", "Red Onions", "Tomato Pomodoro", "Mozzarella"],
        "tags": ["peri peri chicken pizza", "spicy pizza", "tossin style"],
        "calories_kcal": 720
    },

    # Pastas
    {
        "name": "Smoked Chicken Fettuccine Carbonara",
        "category": "Pastas",
        "description": "Al dente hand-rolled fettuccine ribbons tossed in velvety emulsion of egg yolks, crispy bacon or smoked chicken, freshly cracked tellicherry pepper, and pecorino romano.",
        "base_price": 440, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Fettuccine Pasta", "Egg Yolks", "Pecorino Romano", "Smoked Chicken/Bacon", "Black Pepper"],
        "tags": ["carbonara", "fettuccine", "creamy pasta", "smoke house deli"],
        "calories_kcal": 660
    },
    {
        "name": "Handmade Gnocchi Quattro Formaggi",
        "category": "Pastas",
        "description": "Pillow-soft handmade potato gnocchi dumplings sautéed in creamy four cheese reduction, garnished with toasted walnuts and fresh sage.",
        "base_price": 420, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Potato Gnocchi", "Cheddar & Fontina", "Cream", "Walnuts", "Fresh Sage"],
        "tags": ["gnocchi", "handmade pasta", "four cheese gnocchi", "italian classic"],
        "calories_kcal": 590
    },
    {
        "name": "Fiery Penne All'Arrabbiata",
        "category": "Pastas",
        "description": "Tubular penne pasta tossed in spicy slow-cooked Roman tomato sauce made with garlic, crushed red pepper flakes, fresh parsley, and extra virgin olive oil.",
        "base_price": 340, "is_veg": True, "spicy_level": "Spicy",
        "dietary_tags": ["Vegetarian", "Vegan"],
        "ingredients": ["Penne Rigate", "Plum Tomatoes", "Garlic", "Chilli Flakes", "Fresh Parsley", "Olive Oil"],
        "tags": ["arrabbiata", "spicy pasta", "red sauce pasta", "vegan pasta"],
        "calories_kcal": 440
    },
    {
        "name": "Classic Lasagna Bolognese Tradizionale",
        "category": "Pastas",
        "description": "Layers of fresh egg pasta sheets baked with slow-simmered minced meat bolognese ragù, silky béchamel sauce, and bubbling parmigiano crust.",
        "base_price": 480, "is_veg": False, "spicy_level": "Mild",
        "dietary_tags": ["High-Protein"],
        "ingredients": ["Fresh Pasta Sheets", "Minced Meat Ragù", "Bechamel Sauce", "Parmigiano-Reggiano", "Tomato"],
        "tags": ["lasagna", "bolognese", "baked pasta", "chianti special", "bestseller"],
        "calories_kcal": 740
    },
    {
        "name": "Wild Basil Pesto Genovese Fusilli",
        "category": "Pastas",
        "description": "Spiral fusilli pasta coated in aromatic Ligurian green sauce pounded with fresh Genovese basil, toasted pine nuts, garlic, pecorino, and olive oil.",
        "base_price": 380, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Fusilli", "Fresh Basil", "Pine Nuts", "Garlic", "Parmesan Cheese", "Olive Oil"],
        "tags": ["pesto pasta", "fusilli", "green pasta", "genovese"],
        "calories_kcal": 520
    },

    # Starters & Bread
    {
        "name": "Signature Stuffed Garlic Bread with Mozzarella",
        "category": "Starters & Bread",
        "description": "Freshly baked artisan baguette stuffed with roasted garlic butter, molten mozzarella cheese, sweet corn, and pickled jalapenos.",
        "base_price": 220, "is_veg": True, "spicy_level": "Mild",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Baguette Dough", "Garlic Butter", "Mozzarella", "Sweet Corn", "Jalapenos"],
        "tags": ["garlic bread", "stuffed garlic bread", "cheesy bread", "pizza bakery"],
        "calories_kcal": 410
    },
    {
        "name": "Fresh Burrata Caprese Salad",
        "category": "Starters & Bread",
        "description": "Whole ball of creamy burrata served with ripe heirloom tomatoes, wild arugula rocket leaves, aged balsamic reduction, and basil oil.",
        "base_price": 380, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian", "Gluten-Free"],
        "ingredients": ["Burrata Cheese", "Heirloom Tomatoes", "Arugula", "Balsamic Glaze", "Basil Oil"],
        "tags": ["burrata", "caprese salad", "healthy starter", "gourmet salad"],
        "calories_kcal": 340
    },

    # Desserts
    {
        "name": "Classic Italian Tiramisu Tradizionale",
        "category": "Desserts",
        "description": "Savoiardi ladyfingers soaked in dark espresso and marsala, layered with whipped mascarpone zabaione cream and dusted with bitter Valrhona cocoa.",
        "base_price": 280, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Mascarpone Cheese", "Savoiardi Ladyfingers", "Espresso Coffee", "Marsala", "Valrhona Cocoa"],
        "tags": ["tiramisu", "italian dessert", "coffee dessert", "bestseller"],
        "calories_kcal": 440
    },
    {
        "name": "Warm Nutella Calzone with Ricotta",
        "category": "Desserts",
        "description": "Woodfired folded sourdough pocket oozing with melted Nutella hazelnut spread, sweet ricotta cheese, and sprinkled with powdered sugar.",
        "base_price": 260, "is_veg": True, "spicy_level": "None",
        "dietary_tags": ["Vegetarian"],
        "ingredients": ["Sourdough", "Nutella", "Sweet Ricotta", "Powdered Sugar"],
        "tags": ["nutella calzone", "sweet calzone", "dessert pizza", "brik oven"],
        "calories_kcal": 510
    }
]

print("Cuisine Catalogs Part 1 loaded successfully.")

