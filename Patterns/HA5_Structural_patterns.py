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


class Facade:
    
    
    def __init__(self, classifiers:list) -> None:
        """
        Initialize a class item with a list of classificators
        """
        self.classifiers = classifiers

    def fit(self, X_train, y_train):
        """
        Fit classifiers from the initialization stage
        """
        for cl in self.classifiers:
            cl.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Get predicts from all the classifiers and return
        the most popular answers
        """
        n = len(X_test)
        all_pred = self.classifiers[0].predict(X_test).reshape(1, n)
        if len(self.classifiers)>1:
            for cl in self.classifiers[1:]:
                pred = cl.predict(X_test)
                all_pred = np.concatenate([all_pred, pred.reshape(1, n)])
                final_pred = [max(set(all_pred[:,i]), key = a.count) for i in range(n) ]
        else:
            final_pred = all_pred
        return final_pred

        
if __name__ == "__main__":
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    3. Prepare classifiers to initialize <StructuralPatternName> class.
    4. Train the ensemble
    """

    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, shuffle=True, random_state=42 )
    pattern_item = Facade([SGDClassifier(), XGBClassifier(use_label_encoder=False), CatBoostClassifier(verbose=0)])
    pattern_item.fit(X_train, y_train)
    predictions = pattern_item.predict(X_test)
    score = accuracy_score(predictions, y_test)
    print(score)