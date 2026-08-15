from pydantic import BaseModel, Field
from enum import Enum

class ChurnRiskLevel(str, Enum):
    HIGH = "high"
    LOW = "low"

class PredictionResponse(BaseModel):
    success: bool
    prediction: str
    churn_risk: ChurnRiskLevel
    confidence_score: float = Field(..., ge=0, le=1)
    confidence_percentage: float = Field(..., ge=0, le=100)