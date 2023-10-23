import pandas as pd
import scipy.sparse
from prefect import flow, task
from sklearn.pipeline import Pipeline


@flow
def train_model(
    pipeline: Pipeline, x_train: scipy.sparse.csrmatrix, y_train: scipy.sparse.csrmatrix
):
    return pipeline.fit(x_train, y_train)
