import streamlit as st
import joblib
import pandas as pd

# Modeli Yükle
model = joblib.load('model.pkl')

st.title("🏦 Credit Score Calculator")

# Giriş Alanları
salary = st.number_input("Salary (TL)", min_value=0, value=25000)
age = st.slider("Age", 18, 80, 30)
late = st.number_input("Number of Late Payment", 0, 10, 0)

if st.button("Calcute Score"):
    input_df = pd.DataFrame([[0] * len(model.feature_names_in_)], columns=model.feature_names_in_)
    if 'Salary' in input_df.columns: input_df['Salary'] = salary
    if 'Age' in input_df.columns: input_df['Age'] = age
    if 'Number of Late Payments' in input_df.columns: input_df['Number of Late Payments'] = late
    
    prediction = model.predict(input_df)
    st.success(f"Credit Score: {int(prediction[0])}")
