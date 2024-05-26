from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pandas as pd
import sys
from src.exception import CustomException

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/', methods=['GET', 'POST'])
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

    return render_template('form1.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80) 

