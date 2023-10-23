import numpy as np
from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    MODEL_VERSION,
    PATH_TO_MODEL,
)
from fastapi import FastAPI
from lib.modelling import run_inference
from lib.models import AbaloneAge, InputData
from lib.utils import load_model

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": MODEL_VERSION}


@app.post("/predict")
def predict(payload: InputData):
    model = load_model(PATH_TO_MODEL)
    y = run_inference([payload], model)
    age = np.round(y[0], 2)
    return AbaloneAge(age=age)
