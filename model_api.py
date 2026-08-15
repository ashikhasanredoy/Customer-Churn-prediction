from fastapi import FastAPI, HTTPException

from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from schema.user_input import UserInput
from schema.response_models import PredictionResponse, ChurnRiskLevel


app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn using a trained ML model.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/predict",response_model=PredictionResponse)
def make_prediction(user_input: UserInput):

    try:
        data = CustomData(
            gender=user_input.gender,
            SeniorCitizen=user_input.SeniorCitizen,
            Partner=user_input.Partner,
            tenure=user_input.tenure,
            Dependents=user_input.Dependents,
            PhoneService=user_input.PhoneService,
            MultipleLines=user_input.MultipleLines,
            InternetService=user_input.InternetService,
            OnlineSecurity=user_input.OnlineSecurity,
            OnlineBackup=user_input.OnlineBackup,
            DeviceProtection=user_input.DeviceProtection,
            TechSupport=user_input.TechSupport,
            StreamingTV=user_input.StreamingTV,
            StreamingMovies=user_input.StreamingMovies,
            Contract=user_input.Contract,
            PaperlessBilling=user_input.PaperlessBilling,
            PaymentMethod=user_input.PaymentMethod,
            MonthlyCharges=user_input.MonthlyCharges,
            TotalCharges=user_input.TotalCharges
        )

        features = data.get_dataframe()

        pipeline = PredictPipeline()
        prediction, confidence = pipeline.predict_with_confidence(features)
        prediction_value = prediction[0]
        confidence_score = confidence[0]

        is_churn = str(prediction_value).strip().lower() in {"1", "yes"}
        churn_risk = "high" if is_churn else "low"

        return PredictionResponse(
        success=True,
        prediction="Yes",
        churn_risk=ChurnRiskLevel.HIGH,
        confidence_score=round(confidence_score, 4),
        confidence_percentage=round(confidence_score * 100, 2)
    )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}" )