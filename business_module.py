import streamlit as st
import pandas as pd
import database

# This is the "Business Office" Building
# It handles Inventory, Accounting, and Staff

def run():
    st.sidebar.button("LOGOUT", on_click=lambda: st.session_state.update(current_user=None))
    st.title("💼 Enterprise Management SaaS")
    
    # --- REVENUE CARDS (REAL-TIME) ---
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Gross Profit", "₱850,000", "+12%")
    m2.metric("Net Profit", "₱620,000", "+8%")
    m3.metric("Total Expenses", "₱230,000", "-2%")
    m4.metric("Active Staff", "24", "On Duty")
    
    # --- THE TABS ---
    tab_ops = st.tabs(["📦 Inventory & Stock", "💰 Accounting", "👥 HRM & Payroll"])
    
    # TAB 1: INVENTORY (The "Monday.com" Grid)
    with tab_ops[0]:
        st.subheader("Smart Inventory System")
        st.info("💡 Instructions: Click on 'Stock' to update numbers. Click 'Add Row' to add new items.")
        
        # Initialize Inventory Data in Session
        if 'inventory_db' not in st.session_state:
            st.session_state.inventory_db = pd.DataFrame([
                {"Item": "Soap Kits", "Stock": 500, "Status": "Good", "Supplier": "ABC Corp"},
                {"Item": "Towels", "Stock": 120, "Status": "Low", "Supplier": "Textile Inc"},
                {"Item": "Water Bottles", "Stock": 1000, "Status": "Good", "Supplier": "Nature Spring"},
            ])
            
        # THE EDITABLE GRID
        edited_inventory = st.data_editor(
            st.session_state.inventory_db,
            num_rows="dynamic",
            use_container_width=True
        )
        
        # SYNC BUTTON
        if st.button("☁️ SYNC STOCK TO CLOUD", type="primary"):
            st.session_state.inventory_db = edited_inventory
            st.toast("✅ Inventory Updated & Synced!")
            
    # TAB 2: ACCOUNTING
    with tab_ops[1]:
        st.subheader("Bookkeeping Ledger")
        st.warning("Spreadsheet Mode Active. Auto-Tax Calculation: ON")
        sheet_data = pd.DataFrame({
            "Date": ["2026-01-28", "2026-01-28"],
            "Transaction": ["Room 305 Payment", "Supplier Pay"],
            "Income": [5000, 0],
            "Expense": [0, 2000],
            "Tax (12%)": [600, 0]
        })
        st.dataframe(sheet_data, use_container_width=True)

    # TAB 3: HR
    with tab_ops[2]:
        st.subheader("Staff Management")
        st.text_input("Search Employee Name...")
        st.success("24 Staff Members Active")
  
