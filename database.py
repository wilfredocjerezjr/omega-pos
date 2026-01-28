import streamlit as st
import pandas as pd
import datetime
import random

# ==============================================================================
# THE OMEGA VAULT (MEMORY CHIP)
# Handles all Data, Sales, and Profit Calculations
# ==============================================================================

# --- 1. CONFIGURATION (Markup & Prices) ---
def init_connection():
    if 'profit_config' not in st.session_state:
        st.session_state.profit_config = pd.DataFrame({
            "Product": ["Globe 100", "Smart Giga", "Hotel Room A"],
            "Supplier_Cost": [97.00, 48.00, 3500.00],
            "Markup": [3.00, 2.00, 500.00]
        })
    return st.session_state.profit_config

def save_profit_config(new_df):
    st.session_state.profit_config = new_df

# --- 2. THE LEDGER (Sales History) ---
def init_ledger():
    if 'sales_ledger' not in st.session_state:
        # This is the "Digital Logbook" for every cent entering the system
        st.session_state.sales_ledger = pd.DataFrame(columns=["Timestamp", "Item", "Amount", "Profit", "Ref_ID"])
    return st.session_state.sales_ledger

def record_sale(item, amount, profit):
    """
    Saves a transaction to the permanent record.
    """
    df = init_ledger()
    
    new_row = {
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Item": item,
        "Amount": float(amount),
        "Profit": float(profit),
        "Ref_ID": f"TRX-{random.randint(10000, 99999)}"
    }
    
    # Append the new sale to the ledger
    st.session_state.sales_ledger = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return new_row["Ref_ID"]

# --- 3. THE CALCULATOR (For Business Dashboard) ---
def get_financials():
    """
    Calculates Real-Time Income for the Owner.
    """
    df = init_ledger()
    
    if df.empty:
        return 0, 0, 0 # No sales yet
        
    total_sales = df["Amount"].sum()
    total_profit = df["Profit"].sum()
    transaction_count = len(df)
    
    return total_sales, total_profit, transaction_count
    
