"""
Query Understanding & Natural Language Search (NLS) Parser
Inspired by Zomato's Conversational Search Architecture:
- Dissects complex voice/text queries into semantic intents and entities
- Handles Hinglish colloquialisms ("ka", "k sath", "ke andar", "sabse sasta", "wala", "achcha")
- Classifies query patterns:
    1. Dish + Dish (e.g. 'chai and samosa', 'burger with cold drink', 'anda curry and roti')
    2. Restaurant + Dish (e.g. 'truffles ka burger', 'meghana chicken biryani')
    3. Dish/Restaurant + Constraints (e.g. 'pizza under 200', 'burger 150rs wala', 'non-veg near me')
"""

import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

@dataclass
class ParsedQuery:
    raw_query: str
    intent_type: str  # "MULTI_DISH", "RESTAURANT_DISH", "DISH_SEARCH", "RESTAURANT_SEARCH", "EXPLORATORY"
    target_restaurant: Optional[str] = None
    target_dishes: List[str] = field(default_factory=list)
    locality: Optional[str] = None
    max_price: Optional[float] = None
    min_price: Optional[float] = None
    is_veg: Optional[bool] = None
    spicy_preference: Optional[str] = None  # "Mild", "Spicy", "Extra Spicy"
    is_healthy: bool = False
    near_me: bool = False
    sort_by: Optional[str] = None  # "price_asc", "rating_desc", "distance_asc", "delivery_time_asc"
    clean_search_tokens: List[str] = field(default_factory=list)
    explanation: str = ""

class ConversationalQueryParser:
    def __init__(self, known_restaurants: List[str], known_localities: List[str]):
        # Lowercase set of known restaurant names
        self.known_restaurants = {r.lower(): r for r in known_restaurants}
        self.known_localities = {loc.lower(): loc for loc in known_localities}

        # Multi-dish connectors (English & Hinglish)
        self.multi_dish_splitters = [
            r"\band\b", r"\bwith\b", r"\baur\b", r"\bk\s*sath\b", r"\bke\s*sath\b",
            r"\bplus\b", r"\b\+\b", r"\bva\b"
        ]

        # Restaurant possession keywords ("Meghana ka burger", "from Truffles", "at Toit")
        self.restaurant_connectors = [
            r"\bka\b", r"\bke\b", r"\bki\b", r"\bfrom\b", r"\bat\b", r"\bby\b", r"\boutlet\b"
        ]

    def parse(self, query: str) -> ParsedQuery:
        raw = query.strip()
        q = raw.lower()

        parsed = ParsedQuery(raw_query=raw, intent_type="DISH_SEARCH")
        explanations = []

        # 1. Price constraint detection
        # e.g., "under 200", "below 300", "under inr 200", "hundred ke andar", "200 ke range mein", "150rs wala", "less than 250"
        price_patterns = [
            (r"(?:under|below|less\s+than|upto|within|ke\s*andar)\s*(?:inr|rs\.?|₹)?\s*(\d+)", "max_price"),
            (r"(\d+)\s*(?:rs|rupees|inr|₹)?\s*(?:ke\s*andar|wala|se\s*kam|range\s*mein)", "max_price"),
            (r"(?:hundred|ek\s*sau)\s*(?:ke\s*andar|wala)", 100),
            (r"(?:two\s*hundred|do\s*sau)\s*(?:ke\s*andar|wala)", 200),
            (r"(?:three\s*hundred|teen\s*sau)\s*(?:ke\s*andar|wala)", 300),
            (r"(?:five\s*hundred|paanch\s*sau)\s*(?:ke\s*andar|wala)", 500),
        ]
        
        for pat, key in price_patterns:
            if isinstance(key, int):
                if re.search(pat, q):
                    parsed.max_price = float(key)
                    q = re.sub(pat, " ", q)
                    explanations.append(f"budget <= Rs.{key}")
                    break
            else:
                m = re.search(pat, q)
                if m:
                    val = float(m.group(1))
                    parsed.max_price = val
                    q = re.sub(pat, " ", q)
                    explanations.append(f"budget <= Rs.{int(val)}")
                    break

        # Cheapest / Sabse sasta
        if re.search(r"\b(sabse\s*sasta|cheapest|low\s*cost|budget\s*friendly|pocket\s*friendly)\b", q):
            parsed.sort_by = "price_asc"
            q = re.sub(r"\b(sabse\s*sasta|cheapest|low\s*cost|budget\s*friendly|pocket\s*friendly)\b", " ", q)
            explanations.append("sort by lowest price")

        # Top rated / Best / Sabse achha
        if re.search(r"\b(best|sabse\s*achha|top\s*rated|famous|popular|koi\s*achcha\s*sa)\b", q):
            if not parsed.sort_by:
                parsed.sort_by = "rating_desc"
            q = re.sub(r"\b(best|sabse\s*achha|top\s*rated|famous|popular|koi\s*achcha\s*sa)\b", " ", q)
            explanations.append("prioritizing highest rated")

        # Check if query is looking for restaurant outlets / places (e.g. "pizza outlets near me", "chinese restaurants near me")
        is_outlet_query = False
        if re.search(r"\b(outlets|outlet|restaurants|restaurant|places|place|cafes|cafe|dhabas|dhaba|shops|shop|bakeries|bakery)\b", q):
            is_outlet_query = True
            q = re.sub(r"\b(outlets|outlet|restaurants|restaurant|places|place|cafes|cafe|dhabas|dhaba|shops|shop|bakeries|bakery)\b", " ", q)
            explanations.append("looking for restaurant outlets")
        if re.search(r"\b(near\s*me|pass\s*me|nearby|closest|fastest|quick\s*delivery)\b", q):
            parsed.near_me = True
            parsed.sort_by = parsed.sort_by or "distance_asc"
            q = re.sub(r"\b(near\s*me|pass\s*me|nearby|closest|fastest|quick\s*delivery)\b", " ", q)
            explanations.append("filtered for closest distance")

        # Check for specific locality (e.g. "in Koramangala", "Indiranagar", "Whitefield", "Jayanagar", "HSR")
        for loc_key, loc_name in self.known_localities.items():
            pattern = rf"\b(?:in|at|near)?\s*{re.escape(loc_key)}\b"
            if re.search(pattern, q):
                parsed.locality = loc_name
                q = re.sub(pattern, " ", q)
                explanations.append(f"locality: {loc_name}")
                break

        # 3. Dietary preferences (Veg / Non-veg / Vegan / Healthy)
        if re.search(r"\b(pure\s*veg|shakahari|only\s*veg)\b", q):
            parsed.is_veg = True
            q = re.sub(r"\b(pure\s*veg|shakahari|only\s*veg)\b", " ", q)
            explanations.append("pure vegetarian only")
        elif re.search(r"\b(non\s*veg|nonveg|mansahari|chicken|mutton|fish|meat)\b", q) and not re.search(r"\bno\s+non\s*veg\b", q):
            if not re.search(r"\b(chicken|mutton|fish)\b", q):
                parsed.is_veg = False
                q = re.sub(r"\b(non\s*veg|nonveg|mansahari)\b", " ", q)
                explanations.append("non-vegetarian")
        elif re.search(r"\b(veg|vegetarian)\b", q):
            parsed.is_veg = True
            q = re.sub(r"\b(veg|vegetarian)\b", " ", q)
            explanations.append("vegetarian")

        if re.search(r"\b(healthy|diet|keto|salad|low\s*calorie|guilt\s*free)\b", q):
            parsed.is_healthy = True
            explanations.append("healthy eating focus")

        if re.search(r"\b(extra\s*spicy|bohat\s*teekha|fiery)\b", q):
            parsed.spicy_preference = "Extra Spicy"
        elif re.search(r"\b(spicy|teekha|masaledar)\b", q):
            parsed.spicy_preference = "Spicy"
        elif re.search(r"\b(mild|less\s*spicy|sweet|kam\s*teekha)\b", q):
            parsed.spicy_preference = "Mild"

        # 4. Target Restaurant Detection ("XYZ ka burger", "Meghana chicken biryani", "Truffles burger")
        found_restaurant = None
        for r_key, r_name in self.known_restaurants.items():
            # Check for exact name or key phrase
            pat = rf"\b{re.escape(r_key)}\b"
            if re.search(pat, q):
                found_restaurant = r_name
                q = re.sub(pat, " ", q)
                break
        
        # Clean connectors (e.g. "ka", "ke", "ki", "from", "at", "wala", "wali", "wale")
        q = re.sub(r"\b(ka|ke|ki|from|at|wala|wali|wale|outlet|outlets|batao|chahiye|mangwao)\b", " ", q)

        # 5. Multi-Dish Detection ("Chai and Samosa", "Burger with cold drink")
        dish_parts = [q]
        for splitter in self.multi_dish_splitters:
            if re.search(splitter, q):
                dish_parts = [part.strip() for part in re.split(splitter, q) if part.strip()]
                break

        # Filter out empty or filler tokens
        fillers = {"a", "an", "the", "some", "any", "good", "me", "in", "to", "for", "please", "karo", "bhi", "ek", "do"}
        clean_dishes = []
        for dp in dish_parts:
            tokens = [w for w in re.split(r"\s+", dp) if w and w not in fillers]
            if tokens:
                clean_dishes.append(" ".join(tokens))

        if found_restaurant and clean_dishes:
            if is_outlet_query:
                parsed.intent_type = "RESTAURANT_SEARCH"
                parsed.target_restaurant = found_restaurant
                explanations.append(f"restaurant outlet lookup: '{found_restaurant}'")
            else:
                parsed.intent_type = "RESTAURANT_DISH"
                parsed.target_restaurant = found_restaurant
                parsed.target_dishes = clean_dishes
                explanations.append(f"dish from specific restaurant: '{found_restaurant}'")
        elif found_restaurant and not clean_dishes:
            parsed.intent_type = "RESTAURANT_SEARCH"
            parsed.target_restaurant = found_restaurant
            explanations.append(f"restaurant lookup: '{found_restaurant}'")
        elif is_outlet_query and clean_dishes:
            parsed.intent_type = "RESTAURANT_CUISINE_SEARCH"
            parsed.target_dishes = clean_dishes
            explanations.append(f"finding outlets/places serving: '{clean_dishes[0]}'")
        elif len(clean_dishes) >= 2:
            parsed.intent_type = "MULTI_DISH"
            parsed.target_dishes = clean_dishes
            explanations.append(f"multi-dish combo search: {clean_dishes}")
        elif len(clean_dishes) == 1:
            parsed.intent_type = "DISH_SEARCH"
            parsed.target_dishes = clean_dishes
        else:
            parsed.intent_type = "EXPLORATORY"

        # Final clean tokens for vector/BM25 retrieval
        clean_text = " ".join(clean_dishes)
        parsed.clean_search_tokens = [w for w in re.split(r"[^\w]+", clean_text) if len(w) > 1]
        parsed.explanation = " | ".join(explanations)

        return parsed
