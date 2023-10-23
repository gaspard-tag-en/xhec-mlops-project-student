import pandas as pd
from prefect import flow, task
from sklearn.pipeline import Pipeline


@flow
def train_model(pipeline: Pipeline, x_train: pd.DataFrame, y_train: pd.DataFrame):
    return pipeline.fit(x_train, y_train)
