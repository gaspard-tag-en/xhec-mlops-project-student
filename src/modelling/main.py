# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.
import preprocessing, training, utils
import os
import argparse


def main(trainset_path: os.PathLike) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    df_train = preprocessing.load_data(trainset_path)
    # Preprocess data
    X, y = preprocessing.extract_x_y(df_train)
    pipeline = preprocessing.define_pipeline(cat_cols='Sex')
    # (Optional) Pickle encoder if need be
    
    # Train model
    trained_model = training.train_model(pipeline, X, y)
    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder
    utils.save_to_pickle(trained_model, '../local_models/model__v0.0.1')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
