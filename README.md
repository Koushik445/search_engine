# 🍔 Conversational Food Delivery Search Engine

A production-grade, conversational Natural Language Search (NLS) engine for food delivery apps, inspired by **Zomato's Data Science search architecture**.

Built on a dataset of **100 curated restaurants** and **2,731 dishes**, this search engine moves beyond single-keyword matching to handle complex, multi-intent, voice-like, and colloquial queries (including Hinglish and price-sensitive constraints).

---

## 🚀 Key Features

- **Multi-Dish Search & Single-Cart Bundling**:
  - e.g. *"Chai and samosa"*, *"Burger with cold drink"*
  - Discovers single restaurant outlets that serve both items and bundles them with combined pricing.
- **Restaurant + Dish Search**:
  - e.g. *"Truffles ka burger"*, *"Meghana special chicken biryani"*
  - Resolves target restaurant entities with prepositions (`ka`, `from`, `at`) and ranks the restaurant's menu items.
- **Price-Sensitive & Extreme Budget Queries**:
  - e.g. *"pizza under 250"*, *"burger 150rs wala"*, *"sabse sasta pizza"*
  - Extracts strict budget bounds and sorts by price ascending where appropriate.
- **Geo-Proximity & Outlet Discovery**:
  - e.g. *"pizza outlets near me"*, *"restaurants in Koramangala"*
  - Computes Haversine distance from user coordinates and applies distance decay.
- **Hybrid Retrieval (Dense + Sparse)**:
  - **Dense Vectors**: 384-dimensional embeddings generated with `all-MiniLM-L6-v2`.
  - **Sparse Lexical**: Okapi BM25 inverted index for exact keyword and token matching.
  - **Multi-Factor Re-Ranking**: Combining relevance score, distance decay, restaurant rating, and bestseller priority.

---

## 📁 Repository Structure

```
Search_Engine/
├── app.py                             # Streamlit Web Application UI
├── search_engine.py                   # Core 2-Step Search Engine
├── query_parser.py                    # Conversational NLS Intent & Entity Parser
├── bm25.py                            # BM25 Inverted Index Implementation
├── indexer.py                         # Generates Hybrid Index & Vector Embeddings
├── cli_search.py                      # Interactive Terminal CLI
├── test_zomato_cases.py               # Automated test suite for Zomato query patterns
├── food_delivery_search_dataset_100.json # 100-Restaurant, 2,731-Dish Dataset
├── dish_embeddings.npy                # Pre-computed 384-d Dense Vector Embeddings
├── search_index.pkl                   # Serialized BM25 Index & Catalogs
├── requirements.txt                   # Project Dependencies
├── Dataset_Generation/                # Data generators & validation scripts
└── .gitignore                         # Git ignore configuration
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Koushik445/search_engine.git
   cd search_engine
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running the Search Engine

### 1. Interactive Web UI (Streamlit)
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`. Features interactive query chips, location simulation, and visual combo cards.

### 2. Terminal CLI
```bash
python cli_search.py
```

### 3. Run Test Suite
```bash
python test_zomato_cases.py
```

---

## 📊 Dataset Metrics

- **Total Restaurants**: 100
- **Total Menu Items**: 2,731 (averaging 27.3 dishes per restaurant)
- **Cuisine Families**: 10 (Biryani/Andhra, North Indian, South Indian/Coastal, American Burgers, Italian Pizzas/Pastas, Pan-Asian/Sushi, Healthy/Vegan Bowls, Middle Eastern/Lebanese, Desserts/Gelato, Specialty Cafes & Street Food)
- **Categories**: 44 distinct dish categories
- **Dietary Tags**: `Vegetarian`, `Vegan`, `Gluten-Free`, `Halal`, `High-Protein`, `Keto-Friendly`, `Pescatarian`
