import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os

st.set_page_config(layout="wide")

st.title(" PragyanAI Student Data Advanced Visualization App")
st.image("PragyanAI_Transperent.png")
# -----------------------------
# SAFE DATA LOADING
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV (Recommended)", type=["csv"])

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    default_path = "student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv"
    
    if os.path.exists(default_path):
        df = load_data(default_path)
    else:
        st.error("❌ Dataset not found. Please upload CSV.")
        st.stop()

st.success("✅ Data Loaded Successfully")
# -----------------------------
# Raw Data Toggle
# -----------------------------
st.subheader("Dataset Preview")
if st.checkbox("Show Full Data"):
    st.write(df)
else:
    st.dataframe(df.head(20))

# -----------------------------
# SAFE COLUMN CHECK
# -----------------------------
required_cols = ["Final_Price", "Converted", "Program_Type", "Revenue", "Discount_%"]

missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"❌ Missing columns: {missing}")
    st.stop()

# -----------------------------
# LIMIT DATA (avoid crash)
# -----------------------------
df = df.head(5000)
