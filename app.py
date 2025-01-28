import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('models/best_model.pkl', 'rb'))

# Route for the main page (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from the form
            total_sqft = float(request.form['total_sqft'])
            bath = float(request.form['bath'])
            bhk = int(request.form['bhk'])
            
            # Make prediction
            prediction = model.predict([[total_sqft, bath, bhk]])
            
            # Return the predicted price
            return render_template('index.html', prediction_text=f'Predicted Price: {prediction[0]:,.2f} INR')
        except Exception as e:
            return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
