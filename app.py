import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('car_price_model.pkl', 'rb'))

# App title
st.title("Car Price Prediction System")

st.write("Enter the car details to predict the selling price.")

# User Inputs
present_price = st.number_input(
    "Present Price (in lakhs)",
    min_value=0.0,
    step=0.1
)

kms = st.number_input(
    "Kilometers Driven",
    min_value=0
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Diesel", "Petrol", "CNG"]
)

selling_type = st.selectbox(
    "Selling Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual"]
)

owner = st.number_input(
    "Number of Previous Owners",
    min_value=0,
    max_value=5,
    step=1
)

age = st.number_input(
    "Car Age",
    min_value=0,
    max_value=30,
    step=1
)

# Encoding mappings
fuel_map = {
    "Diesel": 0,
    "Petrol": 1,
    "CNG": 2
}

selling_map = {
    "Dealer": 0,
    "Individual": 1
}

transmission_map = {
    "Automatic": 0,
    "Manual": 1
}

# Prediction Button
if st.button("Predict Car Price"):

    input_data = [[
        present_price,
        kms,
        fuel_map[fuel_type],
        selling_map[selling_type],
        transmission_map[transmission],
        owner,
        age
    ]]

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs"
    )
