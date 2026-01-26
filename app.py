import streamlit as st

# CONFIG
st.set_page_config(page_title="OMEGA POS", page_icon="🏨", layout="wide")

# HIDE BROWSER UI
st.markdown("""<style>
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
.stButton>button {width: 100%; height: 80px; font-size: 20px; font-weight:bold; border-radius: 12px;}
</style>""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("OMEGA OS 🚀")
    mode = st.radio("SELECT MODE:", ["🏨 FRONT DESK", "🍽️ RESTO POS", "📊 ADMIN"])
    st.success("SYSTEM: ONLINE (CLOUD)")

# === HOTEL MODE ===
if mode == "🏨 FRONT DESK":
    st.header("🏨 ROOM STATUS MANAGER")
    c1, c2 = st.columns(2)
    
    # Room 101
    with c1:
        st.success("ROOM 101: VACANT")
        if st.button("CHECK-IN GUEST (101)"):
            st.toast("✅ Check-In Successful!")
    
    # Room 102
    with c2:
        st.error("ROOM 102: OCCUPIED")
        if st.button("CHECK-OUT GUEST (102)"):
            st.toast("💰 Payment Received. Room Cleared.")

# === RESTO MODE ===
elif mode == "🍽️ RESTO POS":
    st.header("🍽️ TOUCH ORDERING")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🍔 WAGYU BURGER (₱350)"):
            st.toast("✅ Added: Wagyu Burger")
        if st.button("🍝 TRUFFLE PASTA (₱450)"):
            st.toast("✅ Added: Truffle Pasta")
            
    with col2:
        if st.button("🥤 COKE ZERO (₱80)"):
            st.toast("✅ Added: Coke Zero")
        if st.button("🍺 SAN MIG LIGHT (₱100)"):
            st.toast("✅ Added: Beer")

# === ADMIN MODE ===
elif mode == "📊 ADMIN":
    st.header("📊 SYSTEM DASHBOARD")
    st.info("Status: Running on Streamlit Cloud ☁️")
    st.metric("Total Revenue (Today)", "₱15,450", "+12%")
