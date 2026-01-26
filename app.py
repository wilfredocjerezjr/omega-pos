import streamlit as st
import pandas as pd
import io

# 1. SETUP & CONFIG
st.set_page_config(page_title="OMEGA SUPER APP", page_icon="💎", layout="wide")
st.markdown("""<style>
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
.block-container {padding-top: 15px;}
.stButton>button {
    width: 100%; border-radius: 10px; height: auto; padding: 15px;
    font-weight: bold; border: 1px solid #ddd; text-align: left;
}
</style>""", unsafe_allow_html=True)

# 2. HEADER
st.title("💎 OMEGA")
st.caption("One App for Everything. Travel. Eat. Stay.")

# 3. MAIN NAVIGATION
tabs = st.tabs(["🏨 HOTELS", "🍽️ RESTAURANTS", "✈️ TRAVEL", "👤 ACCOUNT / DB"])

# ==========================================
# TAB 1: HOTELS (Vision)
# ==========================================
with tabs[0]:
    st.subheader("Find your stay")
    c1, c2 = st.columns([3, 1])
    c1.text_input("Where are you going?", placeholder="Manila, Boracay, Cebu...")
    c2.button("🔍 Search", key="search_hotel")
    st.divider()
    with st.expander("📍 OKADA MANILA (⭐⭐⭐⭐⭐) - ₱8,500/night"):
        st.write("Experience world-class luxury and entertainment.")
        st.button("Reserve Now", key="h1")

# ==========================================
# TAB 2: RESTAURANTS (Vision)
# ==========================================
with tabs[1]:
    st.subheader("Food Delivery")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🍔 JOLLIBEE")
        st.button("View Menu", key="r1")
    with col2:
        st.info("🍗 MANG INASAL")
        st.button("View Menu", key="r2")

# ==========================================
# TAB 3: TRAVEL (Vision)
# ==========================================
with tabs[2]:
    st.subheader("✈️ Flight Booking")
    c1, c2 = st.columns(2)
    c1.text_input("From (Origin)")
    c2.text_input("To (Destination)")
    st.button("Search Flights 🚀", key="f1")

# ==========================================
# TAB 4: ACCOUNT & DATABASE GENERATOR (NEW!)
# ==========================================
with tabs[3]:
    st.header("👤 CEO Control Panel")
    
    st.info("🔐 Welcome, Admin. Generate your System Database below.")
    
    # === DATABASE GENERATOR LOGIC ===
    if st.button("📥 DOWNLOAD MASTER DATABASE (.xlsx)", type="primary"):
        # The 13-Tab Structure
        db_structure = {
            "USERS_MASTER": ["user_id", "username", "password", "full_name", "role", "phone", "wallet"],
            "LOGS_AUDIT": ["log_id", "timestamp", "user_id", "action", "details"],
            "HOTELS_MAIN": ["hotel_id", "owner_id", "hotel_name", "city", "address", "rating", "image_url"],
            "HOTEL_ROOMS": ["room_id", "hotel_id", "type", "price", "qty", "amenities"],
            "RESTOS_MAIN": ["resto_id", "owner_id", "name", "cuisine", "location", "status"],
            "RESTO_MENU": ["item_id", "resto_id", "category", "item_name", "price", "is_available"],
            "TRAVEL_FLIGHTS": ["flight_id", "airline", "origin", "dest", "time", "price", "status"],
            "TRAVEL_BOOKINGS": ["book_id", "user_id", "flight_id", "passenger", "status"],
            "ORDERS_HEAD": ["order_id", "user_id", "total", "payment_method", "status"],
            "ORDERS_ITEMS": ["item_id", "order_id", "product", "qty", "subtotal"],
            "VOUCHERS": ["code", "discount", "min_spend", "expiry"],
            "REVIEWS": ["review_id", "user_id", "rating", "comment"],
            "DRIVERS": ["driver_id", "name", "plate_no", "status"]
        }
        
        # Create Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            for sheet, cols in db_structure.items():
                df = pd.DataFrame(columns=cols)
                df.to_excel(writer, sheet_name=sheet, index=False)
        output.seek(0)
        
        # Download Button
        st.download_button("✅ CLICK TO SAVE FILE", data=output, file_name="OMEGA_DB_MASTER.xlsx")
        st.success("Database Generated! Please upload this to Google Drive.")
