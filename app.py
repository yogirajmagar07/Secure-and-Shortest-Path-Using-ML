from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import sys
from src.exception import CustomException

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

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
                latitude=request.form['latitude'],
                name=request.form['name'],
                religion=request.form['religion'],
                addr_street=request.form['addr_street'],
                crime=request.form['crime'],
                nearest_police_chowki=request.form['nearest_police_chowki'],
                population_density=request.form['population_density'],
                rape=request.form['rape'],
                kidnapping_abduction_total=request.form['kidnapping_abduction_total'],
                acid_attack=request.form['acid_attack'],
                assault_on_women=request.form['assault_on_women'],
                sexual_harassment=request.form['sexual_harassment'],
                use_of_criminal_force_to_women=request.form['use_of_criminal_force_to_women'],
                stalking=request.form['stalking'],
                other_assault_on_women=request.form['other_assault_on_women'],
                district=request.form['district'],
                amenity=request.form['amenity']
            )

            pred_df = data.get_data_as_data_frame()
            pipeline = PredictPipeline()
            prediction = pipeline.predict(pred_df)

            return render_template('result.html', prediction=prediction[0])

        except Exception as e:
            raise CustomException(e, sys)

    return render_template('form1.html')

if __name__ == '__main__':
    app.run(debug=True)
