from dataclasses import dataclass
import sys
import os 
from src.exception import CustomException
from src.logger import logging
from src.utils import model_evaluate, save_object_file

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, recall_score

@dataclass
class ModeltrainConfig:
    train_model_file_path: str = os.path.join("artifact",'model.pkl')

class ModelTrain:
    def __init__(self):
        self.model_train_config = ModeltrainConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )
            models = {
                "RandomForestClassifier": RandomForestClassifier(n_estimators=300, class_weight='balanced', random_state=42),
                "GradientBoostingClassifier": GradientBoostingClassifier(random_state=42),
                "DecisionTreeClassifier": DecisionTreeClassifier(class_weight='balanced', random_state=42),
                'LogisticRegression': LogisticRegression(class_weight='balanced',
                                                         max_iter=1000,
                                                         random_state=42),
                "KNeighborsClassifier": KNeighborsClassifier(),
                "SVC": SVC(class_weight='balanced', probability=True, random_state=42)
            }
            
            params = {
                "RandomForestClassifier": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [None, 5, 10, 20],
                    "criterion": ["gini", "entropy"],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4],
                    "class_weight": [None, "balanced"]
                },
                "GradientBoostingClassifier": {
                    "n_estimators": [100, 200, 300],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "max_depth": [3, 5, 10],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4],
                    "subsample": [0.8, 1.0]
                },
                "DecisionTreeClassifier": {
                    "criterion": ["gini", "entropy"],
                    "splitter": ["best", "random"],
                    "max_depth": [None, 5, 10, 20],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4],
                    "class_weight": [None, "balanced"]
                },
                "LogisticRegression": {
                    "C": [0.001, 0.01, 0.1, 1, 10, 100],
                    "penalty": ["l1", "l2"],
                    "solver": ["liblinear", "saga"],
                    "max_iter": [200, 500, 1000],
                    "class_weight": [None, "balanced"]
                },
                "KNeighborsClassifier": {
                    "n_neighbors": [3, 5, 7, 9, 11],
                    "weights": ["uniform", "distance"],
                    "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
                    "leaf_size": [20, 30, 40],
                    "p": [1, 2]
                },
                "SVC": {
                    "C": [0.001, 0.01, 0.1, 1, 10, 100],
                    "kernel": ["linear", "rbf", "poly", "sigmoid"],
                    "gamma": ["scale", "auto"],
                    "degree": [2, 3, 4],
                    "class_weight": [None, "balanced"]
                }
            }
            
            model_report: dict = model_evaluate(
                X_train=X_train, y_train=y_train,
                X_test=X_test, y_test=y_test,
                models=models, param=params
            )
            
            best_score_model = max(model_report.values())
            
        
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]
            
            if best_score_model < 0.7:
                raise CustomException("No best model found. Best score is below 0.7 threshold.")
            
            logging.info(f"Best model found: {best_model_name} with accuracy score: {best_score_model}")
            
            save_object_file(
                file_path=self.model_train_config.train_model_file_path,
                obj=best_model
            )
            
            predict = best_model.predict(X_test)
            
            recall_sco = recall_score(y_test, predict, average='weighted', zero_division=0)
            f1_sco = f1_score(y_test, predict, average='weighted', zero_division=0)
            
            return recall_sco, f1_sco
            
        except Exception as e:
            raise CustomException(e, sys)