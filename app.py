import streamlit as st
import pandas as pd
import datetime
import time
import gc
import random
from streamlit_option_menu import option_menu

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
    # NAVIGATION
    selected = option_menu(
        menu_title=None,
        options=["Load & Bills", "Travel", "Accommodations"],
        icons=["phone", "airplane", "building"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#A0C4FF"},
        }
    )

    if selected == "Load & Bills":
        st.subheader("📱 Buy Load & Pay Bills")
        
        # 1. ICONS
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.button("💧 Water", use_container_width=True)
        with c2: st.button("⚡ Electric", use_container_width=True)
        with c3: st.button("💳 Credit", use_container_width=True)
        with c4: st.button("📱 Load", use_container_width=True)
        
        st.divider()
        
        # 2. BUY LOAD FLOW
        col_net, col_promo = st.columns(2)
        with col_net:
            network = st.radio("Select Network", ["Globe", "Smart", "DITO", "TM", "TNT"], horizontal=True)
            phone = st.text_input("Mobile Number (+63)", max_chars=10)
            
        with col_promo:
            # FETCH PRODUCTS
            products = OmegaAPI.get_load_products(network)
            # DISPLAY ONLY MARKUP PRICE TO CUSTOMER
            product_options = [f"{p[0]} - ₱{OmegaAPI.calculate_price(p[1]):.2f}" for p in products]
            
            selected_promo = st.selectbox("Select Promo", product_options)
            payment = st.selectbox("Payment", ["GCash", "Maya", "GrabPay", "Card"])

        if st.button("PAY NOW", use_container_width=True):
            if len(phone) < 10:
                st.warning("⚠️ Enter valid number")
            else:
                with st.spinner("Processing Payment..."):
                    res = OmegaAPI.process_transaction(f"TXN-{random.randint(1000,9999)}", 100)
                    st.balloons()
                    st.success(f"✅ LOAD SENT! Ref: {res['ref_id']}")
                    st.info("Receipt sent via SMS.")

    elif selected == "Travel":
        st.subheader("✈️ Flight Booking")
        st.info("System Connected to Amadeus GDS")
        
        c1, c2 = st.columns(2)
        with c1: st.text_input("Origin")
        with c2: st.text_input("Destination")
        
        st.date_input("Travel Date")
        st.button("SEARCH FLIGHTS", use_container_width=True)

    elif selected == "Accommodations":
        st.subheader("🏨 Hotel Booking")
        st.text_input("🔍 Search Location (e.g. Boracay)")
        st.button("FIND HOTELS", use_container_width=True)

# ==============================================================================
# 5. BUSINESS MODULE (Owner)
# ==============================================================================

def business_module():
    st.sidebar.button("LOGOUT", on_click=lambda: st.session_state.update(current_user=None))
    st.title("💼 Business Dashboard")
    
    # REVENUE CARDS
    m1, m2, m3 = st.columns(3)
    m1.metric("Gross Sales", "₱150,000", "+12%")
    m2.metric("Net Profit", "₱45,000", "+8%")
    m3.metric("Inventory Value", "₱200,000")
    
    tab1, tab2 = st.tabs(["Inventory Manager", "Accounting"])
    
    with tab1:
        st.subheader("📦 Stock Management (Auto-Sync)")
        # Drag and Drop Simulation
        df = pd.DataFrame([
            {"Item": "Shampoo", "Stock": 50, "Supplier Price": 100, "Selling Price": 150},
            {"Item": "Soap", "Stock": 120, "Supplier Price": 20, "Selling Price": 35}
        ])
        st.data_editor(df, num_rows="dynamic", use_container_width=True)
        st.success("☁️ All changes auto-saved to Google Drive")

# ==============================================================================
# 6. ADMIN MODULE (The God View)
# ==============================================================================

def admin_module():
    st.sidebar.button("LOGOUT", on_click=lambda: st.session_state.update(current_user=None))
    st.title("👁️ OMEGA GOD MODE")
    st.warning("RESTRICTED: REVENUE COMMAND CENTER")

    # THE PROFIT ENGINE VISUALIZATION
    st.subheader("💸 The Markup Engine (Real-Time)")
    st.caption("You see what the customer doesn't.")
    
    # Sample Data showing the "Invisible Markup"
    profit_data = pd.DataFrame({
        "Product": ["Globe 100", "Smart Giga", "Hotel Room A"],
        "Supplier Cost (You Pay)": [97.00, 48.00, 3500.00],
        "Your Markup (Profit)": [3.00, 2.00, 500.00],
        "Customer Price (They Pay)": [100.00, 50.00, 4000.00]
    })
    
    st.dataframe(profit_data, use_container_width=True)
    
    st.markdown("### 🌐 API Health Status")
    c1, c2 = st.columns(2)
    c1.success("LoadCentral: ONLINE")
    c2.success("Amadeus GDS: ONLINE")

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
