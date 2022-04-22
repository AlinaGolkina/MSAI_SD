from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import copy
import random
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

class Prototype:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, X_train, y_train, df_share):
        #<YOUR CODE HERE>
        xtrain = copy.deepcopy(self.X_train)
        ytrain = copy.deepcopy(self.y_train)
        ind = list(range(len(xtrain)))
        random.shuffle(ind)
        subset_size = df_share * len(xtrain) // 100
        #return xtrain[:subset_size], ytrain[:subset_size]
        return xtrain[ind[:subset_size]], ytrain[ind[:subset_size]]
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """

if __name__ == "__main__":
    
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, shuffle=True, random_state=42 )
    
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """

    pattern_item = Prototype(X_train, y_train)

    for df_share in range(10, 101, 10):
        curr_X_train, curr_y_train = pattern_item.get_subsample(X_train, y_train, df_share)
        scaler = StandardScaler()
        curr_X_train = scaler.fit_transform(curr_X_train)
        X_test_scaler = scaler.transform(X_test)
        model = LinearRegression()
        model.fit(curr_X_train, curr_y_train)
        predictions = model.predict(X_test_scaler)
        predictions = np.round(predictions)
        score = accuracy_score(predictions, y_test)
        print(score)
        #<YOUR CODE HERE>
        """
        1. Preprocess curr_X_train, curr_y_train in the way you want
        2. Train Linear Regression on the subsample
        3. Save or print the score to check how df_share affects the quality
        """