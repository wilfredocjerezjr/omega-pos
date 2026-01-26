import streamlit as st

# 1. SETUP & STYLE
st.set_page_config(page_title="OMEGA OS", page_icon="💎", layout="wide")
st.markdown("""<style>
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
.block-container {padding-top: 15px;}
button[data-baseweb="tab"] {font-size: 16px; font-weight: bold; flex-grow: 1;}
.stButton>button {width: 100%; border-radius: 12px; height: 60px; font-weight: bold; border: 1px solid #ddd;}
</style>""", unsafe_allow_html=True)

# 2. HEADER
st.title("💎 OMEGA ENTERPRISE")
st.caption("Central Command System | v3.0 Online")

# 3. TABS (ITO YUNG HINAHANAP MO)
tabs = st.tabs(["🏨 HOTEL", "🍔 BURGER", "✈️ TRAVEL", "👗 STORE", "📊 ADMIN"])

# === HOTEL ===
with tabs[0]:
    st.header("🏨 Room Management")
    c1, c2 = st.columns(2)
    with c1:
        st.info("Room 101: 🟢 VACANT")
        if st.button("Check-In 101"): st.success("✅ Checked In!")
    with c2:
        st.error("Room 102: 🔴 OCCUPIED")
        if st.button("Check-Out 102"): st.warning("💰 Bill: ₱1,500")

# === BURGER ===
with tabs[1]:
    st.header("🍔 Burger Joint POS")
    c1, c2 = st.columns(2)
    with c1:
        st.write("#### 🍔 FOOD")
        if st.button("Classic Burger (₱85)"): st.toast("➕ Classic")
        if st.button("Cheese Burger (₱95)"): st.toast("➕ Cheese")
    with c2:
        st.write("#### 🥤 DRINKS")
        if st.button("Coke (₱25)"): st.toast("➕ Coke")
        if st.button("Water (₱15)"): st.toast("➕ Water")

# === TRAVEL ===
with tabs[2]:
    st.header("✈️ Travel Agency")
    st.selectbox("Select Service:", ["Book Flight", "Hotel", "Visa Assistance"])
    if st.button("🚀 CONFIRM BOOKING"): st.success("Ticket Generated!")

# === STORE ===
with tabs[3]:
    st.header("👗 Inaul Malong")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔴 SELL RED (₱1,200)"): st.toast("Sold Red!")
    with c2:
        if st.button("🟡 SELL GOLD (₱1,500)"): st.toast("Sold Gold!")

# === ADMIN ===
with tabs[4]:
    st.header("📊 Dashboard")
    st.metric("Total Sales", "₱24,500", "+15%")
