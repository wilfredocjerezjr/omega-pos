import database

import streamlit as st
import random
import datetime
import time

# This is the "Consumer Store" Building
# It handles Load, Bills, and Flights

def run():
    # NAVIGATION
    selected = st.selectbox(
        "Navigate",
        ["📱 Load & Bills", "✈️ Travel", "🏨 Accommodations"],
        label_visibility="collapsed"
    )

    if selected == "📱 Load & Bills":
        st.subheader("📱 Buy Load & Pay Bills")
        
        # 1. QUICK ICONS
        c1, c2, c3, c4 = st.columns(4)
        c1.button("💧 Water", use_container_width=True)
        c2.button("⚡ Electric", use_container_width=True)
        c3.button("💳 Credit", use_container_width=True)
        c4.button("📱 Load", use_container_width=True)
        
        st.divider()
        
        # 2. BUY LOAD INTERFACE
        col_net, col_promo = st.columns(2)
        with col_net:
            network = st.radio("Select Network", ["Globe", "Smart", "DITO", "TM", "TNT"], horizontal=True)
            phone = st.text_input("Mobile Number (+63)", max_chars=10)
            
        with col_promo:
            # STATIC PROMOS (We will connect to API later)
            st.info(f"Browsing {network} Promos...")
            promo = st.selectbox("Select Promo", ["Regular 100", "Go50", "AllNet 20"])
            
                # THE BUY BUTTON (CONNECTED TO DATABASE)
        if st.button("PAY NOW", type="primary", use_container_width=True):
            if len(phone) < 10:
                st.error("⚠️ Please enter a valid mobile number")
            else:
                with st.spinner("Processing Transaction..."):
                    time.sleep(1) # Processing simulation
                    
                    # --- THE MONEY SHOT: RECORD THE SALE ---
                    # We record a 100 peso sale with 3 peso profit
                    ref_id = database.record_sale(f"{network} Load", 100.00, 3.00)
                    
                    st.balloons()
                    st.success(f"✅ LOAD SENT! Ref: {ref_id}")
                    st.toast("💰 Revenue Recorded in Admin Dashboard")
                    

    elif selected == "✈️ Travel":
        st.subheader("✈️ Flight Booking (Amadeus GDS)")
        c1, c2 = st.columns(2)
        c1.text_input("Origin (e.g., MNL)")
        c2.text_input("Destination (e.g., CEB)")
        st.button("SEARCH FLIGHTS", use_container_width=True)

    elif selected == "🏨 Accommodations":
        st.subheader("🏨 Hotel Booking")
        st.text_input("Search Location")
        st.button("FIND HOTELS", use_container_width=True)
  
