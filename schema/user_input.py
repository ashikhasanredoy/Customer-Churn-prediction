from pydantic import BaseModel, Field
from typing import Annotated, Literal

class UserInput(BaseModel):
    
    gender: Annotated[Literal["Male", "Female"], Field(..., description="Customer gender")] 
    SeniorCitizen: Annotated[Literal[0, 1], Field(..., description="1 if senior citizen, 0 otherwise")] 
    Partner: Annotated[Literal["Yes", "No"], Field(..., description="Whether customer has a partner")]
    tenure: Annotated[int, Field(..., ge=0, le=72, description="Number of months with the company (0-72)")] 
    Dependents: Annotated[Literal["Yes", "No"], Field(..., description="Whether customer has dependents")]
    PhoneService: Annotated[Literal["Yes", "No"], Field(..., description="Whether customer has phone service")]
    MultipleLines: Annotated[Literal["Yes", "No", "No phone service"], 
                            Field(..., description="Whether customer has multiple phone lines")]
    
    InternetService: Annotated[Literal["DSL", "Fiber optic", "No"], 
                              Field(..., description="Type of internet service")]
    
    OnlineSecurity: Annotated[Literal["Yes", "No", "No internet service"], 
                             Field(..., description="Whether customer has online security service")]
    
    OnlineBackup: Annotated[Literal["Yes", "No", "No internet service"], 
                           Field(..., description="Whether customer has online backup service")]
    
    DeviceProtection: Annotated[Literal["Yes", "No", "No internet service"], 
                               Field(..., description="Whether customer has device protection")]
    
    TechSupport: Annotated[Literal["Yes", "No", "No internet service"], 
                          Field(..., description="Whether customer has tech support")]
    
    StreamingTV: Annotated[Literal["Yes", "No", "No internet service"], 
                          Field(..., description="Whether customer has streaming TV service")]
    
    StreamingMovies: Annotated[Literal["Yes", "No", "No internet service"], 
                              Field(..., description="Whether customer has streaming movies service")]
    
    Contract: Annotated[Literal["Month-to-month", "One year", "Two year"], 
                       Field(..., description="Customer contract type")]
    
    PaperlessBilling: Annotated[Literal["Yes", "No"], 
                               Field(..., description="Whether customer uses paperless billing")]
    
    PaymentMethod: Annotated[Literal["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], 
                            Field(..., description="Customer payment method")]
    MonthlyCharges: Annotated[float, Field(..., ge=0, le=150, description="Monthly service charge (0-150)")]
    TotalCharges: Annotated[float, Field(..., ge=0, description="Total charges (cumulative)")]

    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "gender": "Male",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "tenure": 53,
                "Dependents": "Yes",
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "Fiber optic",
                "OnlineSecurity": "No",
                "OnlineBackup": "No",
                "DeviceProtection": "Yes",
                "TechSupport": "Yes",
                "StreamingTV": "Yes",
                "StreamingMovies": "Yes",
                "Contract": "One year",
                "PaperlessBilling": "No",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 27.6,
                "TotalCharges": 2723.4
            }
        }