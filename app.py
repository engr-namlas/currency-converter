
"""
Currency Converter App (Gradio Version)

How to run in Google Colab / Hugging Face:
1. Install Gradio: pip install gradio
2. Run this script: python app.py
3. The app will launch and give you a public URL (share=True).
"""

import streamlit as gr

# Hardcoded example exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "PKR": 278.0,
    "GBP": 0.79,
    "INR": 83.0,
}

def convert(amount, from_currency, to_currency):
    try:
        amount = float(amount)
        if amount < 0:
            return "❌ Amount cannot be negative."
        if from_currency == to_currency:
            return "⚠️ Please select different currencies."
        # Convert to USD first, then to target
        usd_amount = amount / exchange_rates[from_currency]
        converted = usd_amount * exchange_rates[to_currency]
        return f"{amount} {from_currency} = {round(converted, 2)} {to_currency}"
    except Exception as e:
        return f"❌ Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("# 💱 Currency Converter\nSimple converter with fixed rates (USD, EUR, PKR, GBP, INR).")
    
    amount = gr.Number(value=1.0, label="Amount")
    from_currency = gr.Dropdown(list(exchange_rates.keys()), value="USD", label="From Currency")
    to_currency = gr.Dropdown(list(exchange_rates.keys()), value="PKR", label="To Currency")
    output = gr.Textbox(label="Converted Value")
    
    convert_btn = gr.Button("Convert")
    convert_btn.click(convert, inputs=[amount, from_currency, to_currency], outputs=output)

# Launch app with share=True for Hugging Face / Colab
demo.launch(share=True)
