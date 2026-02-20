import streamlit as st
import google.generativeai as genai
#
# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Eco-Chef Planner", page_icon="🥗")
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("🥗 Smart Recipe Planner")
st.write("Reduce food waste by cooking with what you already have!")

# --- 2. INVENTORY INPUT ---
# Using a multi-select for common items, plus a text input for others
common_items = ["Paneer", "Palak", "Potato", "Tomato", "Rice", "Dal", "Curd", "Coriander"]
inventory = st.multiselect("Select ingredients in your kitchen:", common_items)
extra_items = st.text_input("Anything else? (e.g., specific spices, leftover veggies)")

all_ingredients = ", ".join(inventory) + (f", {extra_items}" if extra_items else "")

def get_recipes(ingredients):
    model = genai.GenerativeModel('gemini-3-flash-preview')
    # Customizing the prompt for your preferences (Veg, Indian, Bread-free)
    prompt = f"""
    You are a zero-waste chef. Based on these ingredients: {ingredients}, 
    suggest 3 vegetarian Indian recipes. 
    Requirements:
    - Avoid recipes that require bread/roti.
    - Focus on 'Simple' and 'Fast-food' styles where possible.
    - For each recipe, list the 'Waste Saver' tip (how it uses up old ingredients).
    - Provide a brief 'How-to' for each.
    """
    response = model.generate_content(prompt)
    return response.text

# --- 3. UI LOGIC ---
if st.button("Generate Zero-Waste Recipes"):
    if all_ingredients.strip():
        with st.spinner("Finding the perfect vegetarian match..."):
            recipes = get_recipes(all_ingredients)
            st.subheader("👨‍🍳 Your Personalized Meal Plan")
            st.markdown(recipes)
            st.balloons()
    else:
        st.warning("Please add at least one ingredient!")