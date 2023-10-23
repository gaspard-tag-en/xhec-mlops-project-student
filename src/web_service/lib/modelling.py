import json

import numpy as np
import pandas as pd
from lib.models import InputData
from loguru import logger
from sklearn.base import BaseEstimator


def run_inference(input_data: InputData, model: BaseEstimator) -> np.ndarray:
    """Run inference on a list of input data.

    Args:
        payload (dict): the data point to run inference on.
        model (BaseEstimator): the fitted model object.

    Returns:
        np.ndarray: the predicted trip durations in minutes.

    Example payload:
        json of Inputs
    """
    logger.info(f"Running inference on:\n{input_data}")
    df = pd.DataFrame([x.dict() for x in input_data])
    X = df.rename(
        columns={
            "Whole_weight": "Whole weight",
            "Shucked_weight": "Shucked weight",
            "Viscera_weight": "Viscera weight",
            "Shell_weight": "Shell weight",
        }
    )
    y = model.predict(X)
    logger.info(f"Predicted abalone age:\n{y}")

    return y
