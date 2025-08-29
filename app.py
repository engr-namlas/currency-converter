import streamlit as gr

# Hardcoded exchange rates (relative to USD)
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

def format_output(amount, from_curr, to_curr, decimals):
    valid, error = validate_input(amount, from_curr, to_curr)
    if not valid:
        return error
    
    amount_in_usd, converted = convert_currency(amount, from_curr, to_curr)
    rounded_value = round(converted, decimals)

    symbol_from = exchange_rates[from_curr]["symbol"]
    symbol_to = exchange_rates[to_curr]["symbol"]

    return (
        f"💱 Converted via USD:\n"
        f"{symbol_from}{amount} {from_curr} → "
        f"${amount_in_usd:.4f} USD → "
        f"{symbol_to}{converted:.4f} {to_curr}\n\n"
        f"Rounded ({decimals} dp): {symbol_to}{rounded_value}"
    )

def reset_fields():
    return 1.0, "USD", "PKR", 2

with gr.Blocks() as demo:
    gr.Markdown("## 💱 Simple Currency Converter\nEnter an amount, choose currencies, and convert instantly.")
    
    with gr.Row():
        amount = gr.Number(label="Amount", value=1.0)
        decimals = gr.Slider(0, 4, value=2, step=1, label="Decimal Places")
    
    with gr.Row():
        from_curr = gr.Dropdown(list(exchange_rates.keys()), label="From", value="USD")
        to_curr = gr.Dropdown(list(exchange_rates.keys()), label="To", value="PKR")
    
    with gr.Row():
        convert_btn = gr.Button("🔄 Convert")
        reset_btn = gr.Button("♻️ Reset")
    
    output = gr.Textbox(label="Result", lines=5)

    convert_btn.click(format_output, [amount, from_curr, to_curr, decimals], output)
    reset_btn.click(reset_fields, outputs=[amount, from_curr, to_curr, decimals])

demo.launch()
