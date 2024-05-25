import sys
import pandas as pd
from flask import Flask, request, render_template
from src.exception import CustomException
from src.utils import load_object
import os

app = Flask(__name__)

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, longitude, latitude, name, religion, addr_street, crime,
                 nearest_police_chowki, population_density, rape, kidnapping_abduction_total,
                 acid_attack, assault_on_women, sexual_harassment, use_of_criminal_force_to_women,
                 stalking, other_assault_on_women, district, amenity):
        
        self.longitude = longitude
        self.latitude = latitude
        self.name = name
        self.religion = religion
        self.addr_street = addr_street
        self.crime = crime
        self.nearest_police_chowki = nearest_police_chowki
        self.population_density = population_density
        self.rape = rape
        self.kidnapping_abduction_total = kidnapping_abduction_total
        self.acid_attack = acid_attack
        self.assault_on_women = assault_on_women
        self.sexual_harassment = sexual_harassment
        self.use_of_criminal_force_to_women = use_of_criminal_force_to_women
        self.stalking = stalking
        self.other_assault_on_women = other_assault_on_women
        self.district = district
        self.amenity = amenity

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "longitude": [self.longitude],
                "latitude": [self.latitude],
                "name": [self.name],
                "religion": [self.religion],
                "addr:street": [self.addr_street],
                "crime": [self.crime],
                "nearest_police_chowki": [self.nearest_police_chowki],
                "population_density": [self.population_density],
                "rape": [self.rape],
                "kidnapping_abduction_total": [self.kidnapping_abduction_total],
                "acid_attack": [self.acid_attack],
                "assault_on_women": [self.assault_on_women],
                "sexual_harassment": [self.sexual_harassment],
                "use_of_criminal_force_to_women": [self.use_of_criminal_force_to_women],
                "stalking": [self.stalking],
                "other_assault_on_women": [self.other_assault_on_women],
                "district": [self.district],
                "amenity": [self.amenity]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

