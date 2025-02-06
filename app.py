import streamlit as st

def calculate_profit_loss(dividend_per_stock, buy_price, quantity, sell_price):
    dividend_income = dividend_per_stock * quantity
    stock_pnl = (sell_price - buy_price) * quantity
    total_pnl = dividend_income + stock_pnl
    return dividend_income, stock_pnl, total_pnl

def calculate_breakeven_price(dividend_per_stock, buy_price, quantity):
    breakeven_price = buy_price - (dividend_per_stock * quantity) / quantity
    return breakeven_price

# Streamlit App
st.title("Dividend & Stock Profit Calculator")

# User Inputs
dividend_per_stock = st.number_input("Dividend per Stock (₹)", min_value=0.0, format="%.2f")
buy_price = st.number_input("Buying Price (₹)", min_value=0.0, format="%.2f")
quantity = st.number_input("Quantity of Shares", min_value=1, step=1)
sell_price = st.number_input("Selling Price (₹)", min_value=0.0, format="%.2f")

if st.button("Calculate"):
    dividend_income, stock_pnl, total_pnl = calculate_profit_loss(dividend_per_stock, buy_price, quantity, sell_price)
    breakeven_price = calculate_breakeven_price(dividend_per_stock, buy_price, quantity)
    
    st.subheader("Results:")
    st.write(f"📈 **Dividend Income:** ₹{dividend_income:.2f}")
    st.write(f"📊 **Stock Profit/Loss:** ₹{stock_pnl:.2f}")
    st.write(f"💰 **Total Profit/Loss (Including Dividends):** ₹{total_pnl:.2f}")
    st.write(f"⚖️ **Breakeven Price:** ₹{breakeven_price:.2f}")
