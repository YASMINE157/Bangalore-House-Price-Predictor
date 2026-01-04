import streamlit as st
import joblib
import json
import pandas as pd
import numpy as np


# load the trained model
@st.cache_resource
def load_model():
    return joblib.load("Bengaluru_House_price_model.pkl")

model = load_model()

# head of page
st.set_page_config(page_title="Bengaluru House Price Predictor", page_icon="🏠")
st.title("🏡 Bengaluru House Price Predictor")
st.markdown("---") 
st.write("Enter house details for getting the predicted price")

#build input cols
col1,col2 = st.columns(2)

with col1 :
    location = st.selectbox("Choose Location",["Whitefield", "Indira Nagar", "Sarjapur Road", "Other"])
    sqft = st.number_input("Enter ave sqft", min_value=300, value=1200, step=50)

with col2:
    bath = st.number_input("number of Bathrooms", min_value=1, max_value=10, value=2)
    size = st.number_input("number of rooms", min_value=1, max_value=10, value=2)

st.markdown("---")

# predection button
if st.button("💰 predict the house price"):
    try:
        query_df = pd.DataFrame([[location, sqft, bath, size]], 
                                columns=['location', 'sqft', 'bath', 'size'])
        
        # prediction
        prediction = model.predict(query_df)[0]
        
        # result
        st.balloons()
        st.success(f"### The predicted price {prediction:.2f} Lakh")

    except Exception as e:
        st.error(f"Error:{e}")
        st.warning("make sure that names of cols are right")