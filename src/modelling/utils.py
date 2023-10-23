# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import os
import pickle

from prefect import flow, task
from sklearn.pipeline import Pipeline


@task
def save_to_pickle(pipeline: Pipeline, file_path: os.PathLike):
    """
    Save a pipeline to a pickle file.

    Parameters:
        - pipeline: scikit-learn pipeline object
        - file_path: The path where the pickle file should be saved.
    """
    try:
        with open(file_path, "wb") as file:
            pickle.dump(pipeline, file)
        print(f"Pipeline saved to {file_path}")
    except Exception as e:
        print(f"Error saving the pipeline to {file_path}: {e}")
