"""
Currency Converter App (Streamlit Version)

How to run locally:
1. Install requirements: pip install -r requirements.txt
2. Run the app: streamlit run app.py
"""

import streamlit as st

# Hardcoded example exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "PKR": 278.0,
    "GBP": 0.79,
    "INR": 83.0,
}

st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

st.title("💱 Currency Converter")

# Input fields
amount = st.number_input("Enter amount:", min_value=0.000, value=1.000, step=0.100)
from_currency = st.selectbox("From Currency", list(exchange_rates.keys()))
to_currency = st.selectbox("To Currency", list(exchange_rates.keys()))

if st.button("Convert"):
    if from_currency == to_currency:
        st.warning("Please select different currencies.")
    else:
        # Convert using relative exchange rates
        usd_amount = amount / exchange_rates[from_currency]
        converted = usd_amount * exchange_rates[to_currency]
        st.success(f"{amount} {from_currency} = {round(converted, 2)} {to_currency}")
