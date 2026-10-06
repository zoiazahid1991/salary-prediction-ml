
# Salary Prediction using Machine Learning

## Project Description

This project develops an end-to-end Machine Learning application that predicts salary based on years of professional experience.

The project covers the complete Machine Learning workflow, including data exploration, preprocessing, model training, evaluation, model serialization, and deployment using Streamlit.

## Dataset

The dataset contains two variables:

- Experience Years
- Salary

The target variable is Salary, while Experience Years is used as the input feature.

## Model

Linear Regression

## Model Evaluation

The model was evaluated using:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

### Results

- MSE: 48,077,731.17
- RMSE: 6,933.81
- MAE: 6,419.91
- R² Score: 0.9069

## Application

A Streamlit web application allows users to enter their years of experience and receive a predicted salary.

## Project Structure

ML_Project/

├── data/

│   └── salary_dataset.csv

├── model/

│   └── salary_prediction_model.pkl

├── notebooks/

│   └── model_training.ipynb

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

## Author

Machine Learning Course Project
