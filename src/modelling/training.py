
from sklearn.pipeline import Pipeline
import pandas as pd

def train_model(pipeline: Pipeline, x_train: pd.DataFrame, y_train: pd.DataFrame):
    return pipeline.fit(x_train, y_train)