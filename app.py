
from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pandas as pd
import sys
from src.exception import CustomException

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists and password matches
        if username in users and users[username] == password:
            flash('Login successful!', 'success')
            return redirect('http://localhost:8081')
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash('Username already exists', 'danger')
        else:
            users[username] = password
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('signup.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            data = CustomData(
                longitude=request.form['longitude'],
                latitude=request.form['latitude']
            )

            pred_df = data.get_data_as_data_frame()
            pipeline = PredictPipeline()
            prediction = pipeline.predict(pred_df)

            return render_template('result.html', prediction=prediction[0])

        except Exception as e:
            raise CustomException(e, sys)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80) 

