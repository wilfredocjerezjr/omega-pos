import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import datetime
import time
import random

# --- 1. GLOBAL EMPIRE CONFIGURATION ---
st.set_page_config(
    page_title="OMEGA EMPIRE",
    page_icon="Ω",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE 1 TRILLION WORKFORCE (SESSION STATE) ---
# Ito ang utak ng Trilyong Empleyado. Dito sila nagre-report.

if 'security_team' not in st.session_state: st.session_state.security_team = "ACTIVE (Level 5)"
if 'audit_team' not in st.session_state: st.session_state.audit_logs = []
if 'inventory_staff' not in st.session_state:
    # 7-Star Hotel Inventory Managed by Staff
    st.session_state.hotel_inventory = [
        {"id": 101, "name": "Presidential Suite", "price": 15000, "status": "Available", "stock": 2, "manager": "Team Alpha"},
        {"id": 102, "name": "Deluxe Ocean View", "price": 4500, "status": "Available", "stock": 10, "manager": "Team Beta"},
        {"id": 103, "name": "Standard Room", "price": 2500, "status": "Available", "stock": 25, "manager": "Team Charlie"}
    ]
if 'fintech_team' not in st.session_state:
    # Managed by Load Central / Bank Experts
    st.session_state.wallet_balance = 5000.00
    st.session_state.transactions = []

if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'role' not in st.session_state: st.session_state.role = None


# --- 3. WORKFORCE UTILITIES (TOOLS NG STAFF) ---
def audit_log(action):
    # Accounting Staff records everything
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.audit_logs.append(f"[{timestamp}] {action}")

def security_check():
    # Security Team verifies transaction
    with st.spinner("🔒 SECURITY TEAM: Verifying Biometrics & Encryption..."):
        time.sleep(1)
    return True

# ==========================================
# DIVISION A: BUSINESS OPERATING SYSTEM (SaaS)
# Managed by: Business Consultants & Managers
# ==========================================
def business_hq():
    st.markdown("## 🏢 OMEGA BUSINESS COMMAND CENTER")
    st.caption(f"System Status: {st.session_state.security_team} | Staff Active: 1,000,000+")
    
    # DEPARTMENT TABS
    dept = option_menu(None, ["Hotel Operations", "Inventory Control", "Financial Audit"], 
        icons=['building', 'box-seam', 'file-earmark-spreadsheet'], orientation="horizontal")

    # --- DEPT: HOTEL OPS ---
    if dept == "Hotel Operations":
        st.subheader("🏨 Room & Asset Management")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.info("👋 Manager on Duty: Mr. Smith")
            with st.form("add_asset"):
                st.write("### Add New Asset")
                name = st.text_input("Room/Item Name")
                price = st.number_input("Price (₱)", min_value=0)
                qty = st.number_input("Stock Qty", min_value=1)
                if st.form_submit_button("DEPLOY ASSET"):
                    st.session_state.hotel_inventory.append({
                        "id": random.randint(1000,9999), "name": name, "price": price, 
                        "status": "Available", "stock": qty, "manager": "Team Delta"
                    })
                    audit_log(f"BUSINESS: Added {name} to inventory.")
                    st.success("Asset Deployed Live.")
                    st.rerun()

        with col2:
            st.write("### 📡 Live Inventory Feed")
            df = pd.DataFrame(st.session_state.hotel_inventory)
            st.dataframe(df, use_container_width=True)

    # --- DEPT: FINANCIAL AUDIT ---
    elif dept == "Financial Audit":
        st.subheader("📜 Global Transaction Logs (Audit Team)")
        if st.session_state.audit_logs:
            for log in reversed(st.session_state.audit_logs):
                st.text(log)
        else:
            st.write("No transaction anomalies detected.")

# ==========================================
# DIVISION B: CONSUMER SUPER APP
# Managed by: Customer Service & UX Team
# ==========================================
def consumer_super_app():
    # SUPER APP NAVIGATION (ICONS GAYA NG GUSTO MO)
    selected = option_menu(None, ["Home", "E-Load", "Bills Pay", "Hotels", "Wallet"], 
        icons=['house', 'phone', 'receipt', 'buildings', 'wallet'], 
        menu_icon="cast", default_index=0, orientation="horizontal")

    # --- TAB 1: HOME ---
    if selected == "Home":
        st.write(f"### Welcome, {st.session_state.current_user}!")
        
        # DASHBOARD SUMMARY
        c1, c2, c3 = st.columns(3)
        c1.metric("e-Wallet", f"₱{st.session_state.wallet_balance:,.2f}")
        c2.metric("Points", "5,200 pts")
        c3.metric("Vouchers", "3 Active")
        
        st.divider()
        st.write("#### 🚀 Shortcuts")
        sc1, sc2, sc3, sc4 = st.columns(4)
        sc1.button("⚡ Buy Load", use_container_width=True)
        sc2.button("💧 Pay Water", use_container_width=True)
        sc3.button("✈️ Book Flight", use_container_width=True)
        sc4.button("🏨 Hotel", use_container_width=True)

    # --- TAB 2: E-LOAD (COMPLETE NETWORKS) ---
    elif selected == "E-Load":
        st.subheader("📱 TELECOM LOADING STATION")
        
        # STEP 1: CHOOSE NETWORK
        network = st.radio("Select Network", ["Globe", "Smart", "DITO", "TM", "TNT"], horizontal=True)
        
        # STEP 2: INPUT & PROMO
        col1, col2 = st.columns(2)
        with col1:
            mobile = st.text_input("Mobile Number", placeholder="09xxxxxxxxx")
        with col2:
            # DYNAMIC PROMOS (Managed by Loading Team)
            if network in ["Globe", "TM"]:
                promo = st.selectbox("Select Promo", ["Regular 10", "Go50 (5GB)", "Go90 (8GB)", "GoPlus99", "SuperXclusive"])
            elif network in ["Smart", "TNT"]:
                promo = st.selectbox("Select Promo", ["Regular 10", "GigaVideo 50", "UnliData 499", "MagicData 99"])
            else:
                promo = st.selectbox("Select Promo", ["Regular 10", "DITO 99", "DITO 199 Level Up"])

        # STEP 3: PAYMENT
        if st.button("BUY LOAD NOW", use_container_width=True):
            if security_check(): # Calls the 1 Trillion Security Team
                amt = 50 # Mock amount based on promo
                if st.session_state.wallet_balance >= amt:
                    st.session_state.wallet_balance -= amt
                    audit_log(f"CONSUMER: Bought {promo} for {mobile} ({network})")
                    st.success(f"SUCCESS! You bought {promo}. Ref: LD-{random.randint(10000,99999)}")
                else:
                    st.error("Insufficient Balance. Please Top-up.")

    # --- TAB 3: BILLS PAYMENT (BAYAD CENTER) ---
    elif selected == "Bills Pay":
        st.subheader("🧾 BILLS PAYMENT CENTER")
        
        category = st.selectbox("Category", ["Electric", "Water", "Internet", "Govt", "Loans", "Credit Card"])
        
        if category == "Electric":
            biller = st.selectbox("Biller", ["LEYECO II", "LEYECO III", "MERALCO", "VECO"])
        elif category == "Water":
            biller = st.selectbox("Biller", ["PRIMEWATER", "MAYNILAD", "MANILA WATER"])
        else:
            biller = st.selectbox("Biller", ["PLDT", "CONVERGE", "GLOBE FIBER", "SSS", "PAG-IBIG"])

        acct_num = st.text_input("Account Number")
        amount = st.number_input("Amount to Pay", min_value=0.0)
        
        if st.button("PAY BILL", use_container_width=True):
            if security_check():
                if st.session_state.wallet_balance >= amount:
                    st.session_state.wallet_balance -= amount
                    audit_log(f"CONSUMER: Paid ₱{amount} to {biller}")
                    st.balloons()
                    st.success(f"PAYMENT POSTED! {biller} confirmed receipt.")
                else:
                    st.error("Insufficient Funds.")

    # --- TAB 4: HOTELS (CONNECTED TO BUSINESS OPS) ---
    elif selected == "Hotels":
        st.subheader("🏨 BOOKING & ACCOMMODATION")
        
        # SEARCH BAR managed by Search Team
        with st.expander("🔍 Search & Filters", expanded=True):
            c1, c2, c3 = st.columns([2,1,1])
            c1.text_input("Location", "Palo, Leyte")
            c2.date_input("Dates")
            c3.number_input("Guests", 1)

        st.write("### Available Stays")
        
        # DYNAMIC LIST FROM INVENTORY
        for room in st.session_state.hotel_inventory:
            if room['stock'] > 0:
                with st.container(border=True):
                    rc1, rc2, rc3 = st.columns([1, 3, 1])
                    rc1.write("🛏️")
                    with rc2:
                        st.write(f"**{room['name']}**")
                        st.caption(f"Managed by: {room['manager']}")
                        st.write(f"Only {room['stock']} rooms left")
                    with rc3:
                        st.write(f"**₱{room['price']:,}**")
                        if st.button("BOOK", key=f"h_{room['id']}", use_container_width=True):
                            if st.session_state.wallet_balance >= room['price']:
                                # TRANSACTION EXECUTION
                                st.session_state.wallet_balance -= room['price']
                                room['stock'] -= 1 # Inventory Deduct
                                audit_log(f"CONSUMER: Booked {room['name']}")
                                st.success("BOOKING CONFIRMED! Voucher sent to email.")
                                st.rerun()
                            else:
                                st.error("Need Top-up.")
            else:
                st.warning(f"❌ {room['name']} - FULLY BOOKED")

    # --- TAB 5: WALLET ---
    elif selected == "Wallet":
        st.subheader("💰 MY OMEGA WALLET")
        st.write(f"Current Balance: **₱{st.session_state.wallet_balance:,.2f}**")
        st.button("➕ Cash In (Gcash/Bank)", use_container_width=True)
        
        st.write("### Transaction History")
        if st.session_state.audit_logs:
            for log in reversed(st.session_state.audit_logs):
                st.info(log)
        else:
            st.write("No recent activity.")


# ==========================================
# MAIN HQ GATEWAY (LOGIN)
# ==========================================
def main():
    # SIDEBAR: VISUALIZATION OF THE 1 TRILLION WORKFORCE
    with st.sidebar:
        st.title("Ω EMPIRE")
        st.markdown("---")
        st.caption("SYSTEM STATUS")
        st.success("🟢 1T+ Staff Online")
        st.caption("SECURITY LEVEL")
        st.error("🛡️ DEFCON 1 (Max)")
        st.markdown("---")
        
        if st.session_state.current_user:
            st.write(f"User: **{st.session_state.current_user.upper()}**")
            if st.button("LOGOUT"):
                st.session_state.current_user = None
                st.session_state.role = None
                st.rerun()
    
    # LOGIN LOGIC
    if st.session_state.current_user is None:
        st.markdown("<h1 style='text-align: center;'>Ω OMEGA EMPIRE LOGIN</h1>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1,2,1])
        with c2:
            with st.form("login_form"):
                user = st.text_input("Username")
                pw = st.text_input("Password", type="password")
                
                if st.form_submit_button("ACCESS SYSTEM", use_container_width=True):
                    if user == "owner" and pw == "123":
                        st.session_state.current_user = "Owner"
                        st.session_state.role = "Business"
                        st.rerun()
                    elif user == "juan" and pw == "123":
                        st.session_state.current_user = "Juan"
                        st.session_state.role = "Consumer"
                        st.rerun()
                    else:
                        st.error("❌ UNKNOWN IDENTITY. SECURITY ALERT TRIGGERED.")
            
            st.info("Try: 'owner' / '123' (Business) OR 'juan' / '123' (App)")

    # ROUTING
    elif st.session_state.role == "Business":
        business_hq()
    elif st.session_state.role == "Consumer":
        consumer_super_app()

if __name__ == "__main__":
    main()
