import streamlit as st
import pandas as pd
# This file handles all data connections. 
# We will use this to save your Profit Margins and Inventory.

def init_connection():
    # In the future, this will connect to your real Google Sheet
    # For now, it creates a local "Session Brain"
    if 'db_profit' not in st.session_state:
        st.session_state.db_profit = pd.DataFrame({
            "Product": ["Globe 100", "Smart Giga", "Hotel Room A"],
            "Supplier_Cost": [97.00, 48.00, 3500.00],
            "Markup": [3.00, 2.00, 500.00]
        })
    return st.session_state.db_profit

def save_profit_config(new_df):
    # This saves the data
    st.session_state.db_profit = new_df
    return True
  
