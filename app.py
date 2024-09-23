# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()


class ModelInput(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float


# Load your model
model = pickle.load(open("model1.pkl", "rb"))


@app.post('/predict')
def prediction(input_param: ModelInput):
    # Convert input parameters to JSON, then to dictionary
    input_data = input_param.json()
    input_dict = json.loads(input_data)

    # Extract the features from input dictionary
    nitrogen = input_dict['N']
    phosphorous = input_dict['P']
    potassium = input_dict['K']
    temp = input_dict['temperature']
    humid = input_dict['humidity']
    phv = input_dict['ph']
    rain = input_dict['rainfall']

    # Create a list of inputs for the model
    input_list = [nitrogen, phosphorous, potassium, temp, humid, phv, rain]

    # Get the model prediction
    prediction = model.predict([input_list])

    # Mapping prediction values to crop names using a dictionary
    crop_map = {
        1: 'apple',
        2: 'banana',
        3: 'rice',
        4: 'pomegranate',
        5: 'pigeonpeas',
        6: 'papaya',
        7: 'orange',
        8: 'muskmelon',
        9: 'mungbean',
        10: 'mothbeans',
        11: 'mango',
        12: 'maize',
        13: 'lentil',
        14: 'kidneybeans',
        15: 'jute',
        16: 'grapes',
        17: 'cotton',
        18: 'coffee',
        19: 'coconut',
        20: 'chickpea',
        21: 'blackgram',
        22: 'watermelon'
    }

    # Return the predicted crop name
    predicted_crop = crop_map.get(prediction[0], "Unknown crop")

    return {"predicted_crop": predicted_crop}