
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model/salary_prediction_model.pkl')

st.title('Salary Prediction App')

st.write(
    'Enter your years of experience to predict the expected salary.'
)

experience = st.number_input(
    'Experience Years',
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)

if st.button('Predict Salary'):
    input_data = pd.DataFrame({
        'Experience Years': [experience]
    })

    prediction = model.predict(input_data)[0]

    st.success(f'Predicted Salary: {prediction:,.2f}')
