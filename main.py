# Importar librerías
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
# Importar clases
from models import StressFeatures, PredictionResponse

app = FastAPI(title="Stress Level Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# Cargar modelo
model = joblib.load("stress_model.joblib")
CLASS_NAMES = {0: 'Sin Estrés', 1: 'Eustrés', 2: 'Distrés'}

# Endpoint de predicción
@app.post("/predict", response_model=PredictionResponse)
def predict(ft: StressFeatures):
    # Preparar datos para el modelo
    X = np.array([[ft.anxiety_level, ft.self_esteem, ft.mental_health_history, ft.depression,
                   ft.headache, ft.blood_pressure, ft.sleep_quality, ft.breathing_problem,
                   ft.noise_level, ft.living_conditions, ft.safety, ft.basic_needs,
                   ft.academic_performance, ft.study_load, ft.teacher_student_relationship, ft.future_career_concerns,
                   ft.social_support, ft.peer_pressure, ft.extracurricular_activities, ft.bullying]])
    
    # Realizar predicción
    prediction = model.predict(X)[0]
    probas = model.predict_proba(X)[0]

    # Regresar predicción
    return {
        "prediction": int(prediction),
        "stress_level": CLASS_NAMES[prediction],
        "confidence": float(probas[int(prediction)])
    }
