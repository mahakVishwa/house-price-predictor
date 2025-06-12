House Price Predictor

This is a simple Machine Learning web application built during the DevTown Python Bootcamp.

The app predicts house prices based on input features from the Boston Housing Dataset, using a trained Linear Regression model.

Tech Stack

- Python  
- Flask (for backend API)  
- HTML + CSS (for UI)  
- scikit-learn  
- Pickle (to save the trained model)

How It Works

1. The model was trained using the Boston Housing dataset in Google Colab  
2. The trained model was saved as 'model.pkl'  
3. Flask reads the '.pkl' model and uses it to predict prices based on user inputs  
4. The app takes 13 input features and returns the predicted price (in $1000s)

Files Included

- 'app.py' — Flask backend for predictions  
- 'model.pkl' — Trained Linear Regression model  
- 'boston_model_train.ipynb' — Training code from Google Colab  
- 'templates/index.html' — User interface for entering input

Sample Inputs to Test

CRIM: 0.2
ZN: 18.0
INDUS: 5.0
CHAS: 0
NOX: 0.45
RM: 6.2
AGE: 45.0
DIS: 5.0
RAD: 4
TAX: 300
PTRATIO: 17.0
B: 390.0
LSTAT: 12.0

Expected Output: `$24.28` (approx)

Created for

The DevTown 5-Day Python Bootcamp Project Submission by a student developer practicing ML and backend integration.
