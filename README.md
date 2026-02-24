## Estructura del proyecto

```
StressML/
├── stress_model.ipynb      # Notebook: EDA, entrenamiento y evaluación
├── StressLevelDataset.csv  # Dataset (1100 muestras)
├── main.py                 # API REST con FastAPI
├── models.py               # Esquemas Pydantic (request/response)
├── index.html              # Frontend (formulario + llamada a la API)
└── requirements.txt        # Dependencias
```

> **Nota:** `stress_model.joblib` no está incluido en el repositorio. Debes generarlo ejecutando el notebook (paso 2).

---

## Requisitos

- Python 3.9 o superior
- pip

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Melvin0406/StressML.git
cd StressML
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Generar el modelo entrenado

Abre y ejecuta todas las celdas del notebook `stress_model.ipynb`.
Esto genera el archivo `stress_model.joblib` necesario para la API.

### 4. Levantar la API

```bash
python -m uvicorn main:app --reload
```

La API quedará disponible en `http://localhost:8000`.
Se pueden explorar y probar los endpoints en `http://localhost:8000/docs`.

### 5. Abrir la interfaz web

Abre el archivo `index.html` directamente en tu navegador (doble clic o arrastrar al navegador).

Asegúrate de que la API esté corriendo antes de enviar el formulario.

---

## Endpoint de la API

### `POST /predict`

**Request body (JSON):**

```json
{
  "anxiety_level": 10,
  "self_esteem": 15,
  "mental_health_history": false,
  "depression": 10,
  "headache": 2,
  "blood_pressure": 2,
  "sleep_quality": 3,
  "breathing_problem": 1,
  "noise_level": 2,
  "living_conditions": 3,
  "safety": 3,
  "basic_needs": 3,
  "academic_performance": 3,
  "study_load": 3,
  "teacher_student_relationship": 3,
  "future_career_concerns": 3,
  "social_support": 2,
  "peer_pressure": 2,
  "extracurricular_activities": 2,
  "bullying": 1
}
```

**Response:**

```json
{
  "prediction": 0,
  "stress_level": "Sin Estrés",
  "confidence": 0.97
}
```
