from pydantic import BaseModel, Field

class StressFeatures(BaseModel):
    anxiety_level: int = Field(..., ge=0, le=21)
    self_esteem: int = Field(..., ge=0, le=30)
    mental_health_history: bool
    depression: int = Field(..., ge=0, le=27)
    headache: int = Field(..., ge=0, le=5)
    blood_pressure: int = Field(..., ge=1, le=3)
    sleep_quality: int = Field(..., ge=0, le=5)
    breathing_problem: int = Field(..., ge=0, le=5)
    noise_level: int = Field(..., ge=0, le=5)
    living_conditions: int = Field(..., ge=0, le=5)
    safety: int = Field(..., ge=0, le=5)
    basic_needs: int = Field(..., ge=0, le=5)
    academic_performace: int = Field(..., ge=0, le=5)
    study_load: int = Field(..., ge=0, le=5)
    teacher_student_relationship: int = Field(..., ge=0, le=5)
    future_career_concerns: int = Field(..., ge=0, le=5)
    social_support: int = Field(..., ge=0, le=3)
    peer_pressure: int = Field(..., ge=0, le=5)
    extracurricular_activities: int = Field(..., ge=0, le=5)
    bullying: int = Field(..., ge=0, le=5)

class PredictionResponse(BaseModel):
    prediction: int
    stress_level: str
    confidence: float