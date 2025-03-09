import streamlit as st
from math import exp

# Web App Title
st.title("📈 Futures Fair Value Calculator")

# User Inputs
S = st.number_input("Spot Price", min_value=0.0, format="%.2f")
D = st.number_input("Dividend Amount", min_value=0.0, format="%.2f")
r = st.number_input("Interest Rate (%)", min_value=0.0, format="%.2f") / 100
T = st.number_input("Expiry (days)", min_value=1, format="%d") / 365

# Calculation
if st.button("Calculate Fair Value"):
    F = (S - D) * exp(r * T)
    st.success(f"📊 Futures Fair Value: {round(F, 2)}")
