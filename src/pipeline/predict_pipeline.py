import os
import sys
import pandas as pd
import numpy as np
from src.utils import load_object
from src.exception import CustomException

class PredictPipeline:
    def predict(self, features: pd.DataFrame):
        try:
            model_path = os.path.join("artifact", "model.pkl")
            preprocessor_path = os.path.join("artifact", "preprocessor.pkl")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            transformed_features = preprocessor.transform(features)

            return model.predict(transformed_features)

        except Exception as error:
            raise CustomException(error, sys)
    
    def predict_with_confidence(self, features: pd.DataFrame):
        """
        Prediction method that returns both class prediction and confidence score.
        
        Returns:
            tuple: (predictions, confidence_scores)
                - predictions: numpy array of predicted classes
                - confidence_scores: numpy array of confidence scores (0-1)
        """
        try:
            model_path = os.path.join("artifact", "model.pkl")
            preprocessor_path = os.path.join("artifact", "preprocessor.pkl")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            transformed_features = preprocessor.transform(features)

            predictions = model.predict(transformed_features)


            if hasattr(model, 'predict_proba'):

                probabilities = model.predict_proba(transformed_features)
                confidence_scores = np.max(probabilities, axis=1)
            
            elif hasattr(model, 'decision_function'):
            
                decision_scores = model.decision_function(transformed_features)
                if decision_scores.ndim == 1:
                    confidence_scores = 1 / (1 + np.exp(-decision_scores))
                else:
                    exp_scores = np.exp(decision_scores - np.max(decision_scores, axis=1, keepdims=True))
                    confidence_scores = np.max(exp_scores / np.sum(exp_scores, axis=1, keepdims=True), axis=1)
            
            else:
                # Fallback
                confidence_scores = np.array([0.9] * len(predictions))

            return predictions, confidence_scores

        except Exception as error:
            raise CustomException(error, sys)

class CustomData:
    def __init__(self, gender: str, SeniorCitizen: int, Partner: str, tenure: int,
                 Dependents: str, PhoneService: str, MultipleLines: str,
                 InternetService: str, OnlineSecurity: str, OnlineBackup: str,
                 DeviceProtection: str, TechSupport: str, StreamingTV: str,
                 StreamingMovies: str, Contract: str, PaperlessBilling: str,
                 PaymentMethod: str, MonthlyCharges: float, TotalCharges: float):
        self.data={
            "gender":gender,
            "SeniorCitizen":SeniorCitizen,
            "Partner":Partner,
            "tenure":tenure,
            "Dependents":Dependents,
            "PhoneService":PhoneService,
            "MultipleLines":MultipleLines,
            "InternetService":InternetService,
            "OnlineSecurity":OnlineSecurity,
            "OnlineBackup":OnlineBackup,
            "DeviceProtection":DeviceProtection,
            "TechSupport":TechSupport,
            "StreamingTV":StreamingTV,
            "StreamingMovies":StreamingMovies,
            "Contract":Contract,
            "PaperlessBilling":PaperlessBilling,
            "PaymentMethod":PaymentMethod,
            "MonthlyCharges":MonthlyCharges,
            "TotalCharges":TotalCharges
        }
          
    
    def get_dataframe(self)->pd.DataFrame:
        return pd.DataFrame([self.data])
