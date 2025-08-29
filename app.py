import streamlit as st

exchange_rates = {
    "USD": {"rate": 1.0, "symbol": "$"},
    "EUR": {"rate": 0.92, "symbol": "€"},
    "GBP": {"rate": 0.79, "symbol": "£"},
    "JPY": {"rate": 145.3, "symbol": "¥"},
    "PKR": {"rate": 278.0, "symbol": "₨"},
}

def validate_input(amount, from_curr, to_curr):
    if amount is None:
        return False, "❌ Please enter a number."
    if amount < 0:
        return False, "❌ Amount cannot be negative."
    if from_curr == to_curr:
        return False, f"ℹ️ Same currency selected ({from_curr}). Result: {amount}"
    return True, None

def convert_currency(amount, from_curr, to_curr):
    amount_in_usd = amount / exchange_rates[from_curr]["rate"]
    converted = amount_in_usd * exchange_rates[to_curr]["rate"]
    return amount_in_usd, converted

st.title("💱 Simple Currency Converter")

amount = st.number_input("Enter Amount", min_value=0.0, value=1.0)
from_curr = st.selectbox("From Currency", list(exchange_rates.keys()), index=0)
to_curr = st.selectbox("To Currency", list(exchange_rates.keys()), index=4)
decimals = st.slider("Decimal Places", 0, 4, 2)

if st.button("🔄 Convert"):
    valid, error = validate_input(amount, from_curr, to_curr)
    if not valid:
        st.warning(error)
    else:
        amount_in_usd, converted = convert_currency(amount, from_curr, to_curr)
        rounded_value = round(converted, decimals)
        symbol_from = exchange_rates[from_curr]["symbol"]
        symbol_to = exchange_rates[to_curr]["symbol"]

        st.success(
            f"💱 Converted via USD:\n"
            f"{symbol_from}{amount} {from_curr} → "
            f"${amount_in_usd:.4f} USD → "
            f"{symbol_to}{converted:.4f} {to_curr}\n\n"
            f"Rounded ({decimals} dp): {symbol_to_

    reset_btn.click(reset_fields, outputs=[amount, from_curr, to_curr, decimals])

demo.launch()
