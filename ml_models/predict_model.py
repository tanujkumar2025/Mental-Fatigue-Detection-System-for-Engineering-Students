import joblib
import numpy as np


def load_model():

    model = joblib.load("models/fatigue_model.pkl")

    return model


def predict_fatigue(model, input_data):

    features = np.array(input_data).reshape(1, -1)

    prediction = model.predict(features)

    fatigue_map = {
        0: "Low Fatigue",
        1: "Medium Fatigue",
        2: "High Fatigue"
    }

    return fatigue_map[prediction[0]]