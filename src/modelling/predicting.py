import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline



def predict_age(input_data: pd.DataFrame, model: Pipeline):
    return model.predict(input_data)

def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray):
    return mean_squared_error(y_true, y_pred, squared=False)