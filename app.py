"""
Simple Currency Converter (Streamlit)

How to run:
1. Install requirements: pip install -r requirements.txt
2. Run: streamlit run app.py
"""

import streamlit as st

# Hardcoded exchange rates (relative to USD)
exchange_rates = {
    "USD": {"rate": 1.0, "symbol": "$"},
    "EUR": {"rate": 0.92, "symbol": "€"},
    "GBP": {"rate": 0.79, "symbol": "£"},
    "JPY": {"rate": 145.3, "symbol": "¥"},
    "PKR": {"rate": 278.0, "symbol": "₨"},
}

def validate_input(amount, from_curr, to_curr):
    """Validate user inputs before conversion."""
    if amount is None:
        return False, "❌ Please enter a number."
    if amount < 0:
        return False, "❌ Amount cannot be negative."
    if from_curr == to_curr:
        return False, f"ℹ️ Same currency selected ({from_curr}). Result: {amount}"
    return True, None

def convert_currency(amount, from_curr, to_curr):
    """Convert amount via USD as intermediate currency."""
    amount_in_usd = amount / exchange_rates[from_curr]["rate"]
    converted = amount_in_usd * exchange_rates[to_curr]["rate"]
    return amount_in_usd, converted

# Streamlit UI
st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")
st.title("💱 Simple Currency")
