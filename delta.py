import numpy as np
import streamlit as st
from scipy.stats import norm

def black_scholes_delta(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == "call":
        return norm.cdf(d1)
    else:
        return -norm.cdf(-d1)

st.title("Delta Change Calculator")

S = st.number_input("Spot Price (S)", min_value=0.01, value=100.0)
K = st.number_input("Strike Price (K)", min_value=0.01, value=100.0)
T = st.number_input("Time to Expiry (T in years)", min_value=0.001, value=0.5)
r = st.number_input("Risk-Free Rate (r %)", min_value=0.0, value=5.0) / 100
sigma = st.number_input("Implied Volatility (σ %)", min_value=0.1, value=20.0) / 100
delta_S = st.number_input("Change in Spot Price (ΔS)", value=1.0)
option_type = st.radio("Option Type", ("call", "put"))

if st.button("Calculate Delta Change"):
    initial_delta = black_scholes_delta(S, K, T, r, sigma, option_type)
    new_delta = black_scholes_delta(S + delta_S, K, T, r, sigma, option_type)
    delta_change = new_delta - initial_delta
    
    st.write(f"**Initial Delta:** {initial_delta:.4f}")
    st.write(f"**New Delta:** {new_delta:.4f}")
    st.write(f"**Change in Delta:** {delta_change:.4f}")
