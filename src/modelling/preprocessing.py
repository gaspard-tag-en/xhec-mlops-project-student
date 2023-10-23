from typing import List
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression




def load_data(path: str):
    return pd.read_csv(path)

def compute_target(df: pd.DataFrame):
    return df['Rings'].map(lambda x : x + 1.5)

def extract_x_y(df):
    X = df.drop('Rings', axis=1)
    y = compute_target(df)
    return X, y

def define_pipeline(cat_cols : List[str]):
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, cat_cols)
        ],
        
        remainder='passthrough'  # Pass through the numeric columns
    )

    # Create a pipeline that first preprocesses the data and then applies Linear Regression
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    return pipeline
