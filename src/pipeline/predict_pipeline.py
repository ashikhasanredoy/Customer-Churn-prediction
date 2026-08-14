import os
import sys
import pandas as pd
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
