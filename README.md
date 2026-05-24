# Car Price Prediction using Machine Learning

This project is a machine learning-based web application that predicts the selling price of used cars based on various factors such as present price, fuel type, transmission type, kilometers driven, ownership history, and car age.

The project was developed using Python, Scikit-learn, and Streamlit as part of a practical machine learning workflow covering data preprocessing, exploratory data analysis, model training, evaluation, and deployment.

# Project Objective

The main objective of this project is to build a regression model capable of estimating the selling price of a used car using historical automobile data.

This project demonstrates:

Data preprocessing
Feature engineering
Exploratory Data Analysis (EDA)
Regression algorithms
Model evaluation
Cross validation
Model deployment using Streamlit
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Pickle
Machine Learning Models Used
1. Linear Regression

Used as the baseline regression model to understand relationships between features and selling price.

2. Random Forest Regressor

Used to improve prediction performance and handle nonlinear relationships more effectively.

Features Used for Prediction
Present Price
Kilometers Driven
Fuel Type
Selling Type
Transmission Type
Number of Previous Owners
Car Age
Exploratory Data Analysis

The project includes:

Correlation Heatmap
Fuel Type Distribution
Car Age vs Selling Price Analysis
Outlier Detection
Prediction Error Visualization
Feature Importance Analysis
Model Evaluation Metrics

The models were evaluated using:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)
R² Score
Cross Validation

Random Forest Regressor achieved better performance compared to Linear Regression.

# Streamlit Web Application

A simple and interactive Streamlit web application was developed to allow users to input car details and receive predicted selling prices in real time.

Run the application using:

streamlit run app.py

# Project Structure
Car-Price-Prediction/
│
├── app.py
├── car_price_model.pkl
├── car data.csv
├── Car_Price_Prediction.ipynb
├── requirements.txt
└── README.md

# Future Improvements
Deploy the application on Streamlit Cloud
Improve accuracy using advanced boosting algorithms
Integrate real-time automobile datasets
Add a complete frontend dashboard
Implement cloud deployment and database integration

# Conclusion

This project successfully demonstrates an end-to-end machine learning workflow for predicting used car prices. It combines data analysis, regression modeling, visualization, evaluation, and deployment into a practical real-world application.
