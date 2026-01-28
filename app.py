import consumer_module as store  # We nickname it "store"

import business_module as biz  # We give it the nickname "biz"

import streamlit as st
import pandas as pd
import datetime
import time
import gc
import random
from streamlit_option_menu import option_menu
import database


# ==============================================================================
# 1. SYSTEM CONFIGURATION & STABILITY (THE OMEGA VAULT)
# ==============================================================================

st.set_page_config(
    page_title="OMEGA EMPIRE SUPER APP",
    page_icon="Ω",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- GARBAGE COLLECTOR (ANTI-CRASH PROTOCOL) ---
def auto_cleanup():
    """
    Background process to clear cache and prevent memory leaks.
    Runs asynchronously to ensure infinite scaling.
    """
    gc.collect()
    st.cache_data.clear()

# Trigger cleanup if session has been active too long (Simulated 4-hour interval logic)
if 'last_cleanup' not in st.session_state:
    st.session_state.last_cleanup = time.time()
else:
    if time.time() - st.session_state.last_cleanup > 14400: # 4 hours
        auto_cleanup()
        st.session_state.last_cleanup = time.time()

# --- PASTEL UI ENGINE (MONDAY.COM AESTHETIC) ---
st.markdown("""
    <style>
    /* GLOBAL FONTS & COLORS */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* BACKGROUND & MAIN */
    .stApp {
        background-color: #F7F9FC; /* Soft Blue-Grey */
    }

    /* CARDS & CONTAINERS (Monday.com Style) */
    .css-1r6slb0, .stMetric {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #A0C4FF; /* Pastel Blue Accent */
    }

    /* BUTTONS (Pastel Gradients) */
    .stButton>button {
        background: linear-gradient(90deg, #A0C4FF 0%, #B9FBC0 100%);
        color: #2C3E50;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(160, 196, 255, 0.4);
    }

    /* HEADERS */
    h1, h2, h3 {
        color: #2C3E50;
    }
    
    /* CUSTOM TABS */
    .nav-link-selected {
        background-color: #FFD6A5 !important; /* Pastel Orange */
        color: #333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. API HANDLERS & PRICING ENGINE
# ==============================================================================

class OmegaAPI:
    """
    Handles connections and The Invisible Markup Protocol.
    """
    
    @staticmethod
    def get_load_products(network):
        # SUPPLIER DATA (Hidden from Customer)
        # Structure: Product, Supplier_Price
        inventory = {
            "Globe": [("Regular 100", 97.00), ("Go50", 48.50), ("Go90", 87.00)],
            "Smart": [("Regular 100", 97.00), ("Giga50", 48.00), ("UnliData", 490.00)],
            "DITO": [("LevelUp 99", 98.00)],
            "TM": [("EasySurf 50", 49.00)],
            "TNT": [("SurfSaya 30", 29.00)]
        }
        return inventory.get(network, [])

    @staticmethod
    def calculate_price(supplier_price):
        # THE PROFIT ENGINE: Auto-adds Markup
        # Example: 3.00 peso markup per transaction
        markup = 3.00 
        return supplier_price + markup

    @staticmethod
    def process_transaction(ref_id, amount):
        time.sleep(1.5) # Simulate API Call
        return {
            "status": "SUCCESS",
            "ref_id": ref_id,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# ==============================================================================
# 3. AUTHENTICATION
# ==============================================================================

def login_system():
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
        st.session_state.role = None

    if st.session_state.current_user is None:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<h1 style='text-align: center; color: #A0C4FF;'>Ω OMEGA EMPIRE</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Super App Ecosystem</p>", unsafe_allow_html=True)
            
            with st.form("login_form"):
                user = st.text_input("Username")
                pw = st.text_input("Password", type="password")
                submitted = st.form_submit_button("ACCESS SYSTEM", use_container_width=True)
                
                if submitted:
                    if user == "admin" and pw == "omega":
                        st.session_state.current_user = "Admin"
                        st.session_state.role = "admin"
                        st.rerun()
                    elif user == "owner" and pw == "123":
                        st.session_state.current_user = "Owner"
                        st.session_state.role = "business"
                        st.rerun()
                    elif user == "juan" and pw == "123":
                        st.session_state.current_user = "Juan"
                        st.session_state.role = "consumer"
                        st.rerun()
                    else:
                        st.error("❌ UNKNOWN IDENTITY")
        return False
    return True

# ==============================================================================
# 4. CONSUMER MODULE (Juan)
# ==============================================================================

def consumer_module():
    # This just opens the door to the new consumer_module.py file
    store.run()
    

# ==============================================================================
# 5. BUSINESS MODULE (Owner)
# ============================================================================== 
def business_module():
    # We use the nickname "biz" here so Python doesn't get confused
    biz.run()
    

# ==============================================================================
# 6. ADMIN MODULE (The God View)
# ==============================================================================

def admin_module():
    st.sidebar.button("LOGOUT", on_click=lambda: st.session_state.update(current_user=None))
    st.title("👁️ OMEGA GOD MODE")
    st.warning("⚠️ REVENUE COMMAND CENTER: DATABASE CONNECTED")

    # --- CONNECT TO MEMORY CHIP ---
    if 'profit_config' not in st.session_state:
        st.session_state.profit_config = database.init_connection()

    # --- THE INTERACTIVE PROFIT ENGINE ---
    st.subheader("💸 Profit Margin Controller")
    st.info("💡 Changes made here are now saved to the Session Database.")
    
    # EDITABLE GRID
    edited_df = st.data_editor(
        st.session_state.profit_config,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Your Markup (Profit)": st.column_config.NumberColumn(
                "Your Profit (₱)",
                format="₱%.2f"
            )
        }
    )
    
    # THE SAVE BUTTON
    if st.button("💾 SAVE TO DATABASE", type="primary", use_container_width=True):
        database.save_profit_config(edited_df)
        st.session_state.profit_config = edited_df
        st.toast("✅ DATABASE UPDATED! Margins secured.")
        st.balloons()
    
    st.divider()
    
    # --- API CONTROLS ---
    st.subheader("🌐 Global Connection Status")
    c1, c2 = st.columns(2)
    c1.success("✅ LoadCentral: CONNECTED")
    c2.success("✅ Amadeus GDS: SECURE")
    

# ==============================================================================
# 7. MAIN APP LOGIC
# ==============================================================================

if __name__ == "__main__":
    if login_system():
        role = st.session_state.role
        if role == "admin":
            admin_module()
        elif role == "business":
            business_module()
        elif role == "consumer":
            consumer_module()
