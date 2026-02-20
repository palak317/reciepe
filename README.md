# 🥗 Smart Recipe Planner (Zero-Waste Edition)
**An AI-powered kitchen assistant that transforms your current inventory into delicious, sustainable meals.**

## 📌 Project Overview
Food waste is a significant global issue. This application helps users reduce their environmental footprint by suggesting recipes based on what is *already* in their pantry. It specifically prioritizes **vegetarian, simple Indian, and bread-free** options to cater to healthy, fast-paced lifestyles.

### 🚀 Key Features
- **Inventory-Driven Suggestions:** Uses a multi-select interface to input ingredients like Paneer, Palak, or Dal.
- **Zero-Waste Logic:** The AI prioritizes recipes that use up "near-expiry" items.
- **Waste-Saver Tips:** Every recipe includes a specific tip on how to repurpose leftovers or minimize scraps.
- **Dietary Personalization:** Built-in filters for vegetarian and bread-free Indian meals.

---

## 🛠️ Tech Stack
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **AI Engine:** [Google Gemini API](https://aistudio.google.com/) (Model: `gemini-3-flash-preview`)
- **Language:** Python 3.10+

---

## 🏗️ How it Works
1. **Input Inventory:** Users select ingredients from a predefined list or type in specific items.
2. **AI Analysis:** The **Gemini 3 Flash** model analyzes the flavor profiles and waste-reduction potential of the ingredients.
3. **Recipe Generation:** The app generates three distinct recipes with step-by-step instructions and a sustainability score.

---

## 🏃 Installation & Setup

### 1. Clone & Environment
```bash
git clone [https://github.com/palak317/smart-recipe-planner.git](https://github.com/palak317/smart-recipe-planner.git)
cd smart-recipe-planner
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
