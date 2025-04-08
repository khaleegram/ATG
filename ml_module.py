import numpy as np
from sklearn.ensemble import RandomForestRegressor

def train_ml_model():
    X = np.array([[80, 100], [50, 300], [120, 300]])
    y = np.array([0.8, 0.9, 0.95])

    model = RandomForestRegressor()
    model.fit(X, y)
    return model
