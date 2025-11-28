# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

# Transformers
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

MODEL_DIR = os.getenv("MODEL_DIR", "./modelo_entrenado")

app = FastAPI(title="API de Clasificación (Demo U4)")

# Schema para recibir peticiones JSON
class TextIn(BaseModel):
    text: str

# Cargar modelo y tokenizer al iniciar la app
@app.on_event("startup")
def load_model():
    global model, tokenizer, device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
        model.to(device)
        model.eval()
        print(f"Modelo cargado desde {MODEL_DIR} en {device}")
    except Exception as e:
        print("Error cargando el modelo:", e)
        raise

# Endpoint de prueba
@app.get("/")
def root():
    return {"msg": "API lista. POST /predict con JSON {'text': '...'}"}

# Endpoint de predicción
@app.post("/predict")
def predict(payload: TextIn):
    text = payload.text
    if not text:
        raise HTTPException(status_code=400, detail="Campo 'text' vacío")

    # Tokenizar y predecir
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        pred = int(logits.argmax(dim=-1).item())

    # Asume etiquetas 0 = negativa, 1 = positiva (ajusta si tu modelo difiere)
    label = "Positiva" if pred == 1 else "Negativa"
    return {"text": text, "prediction": pred, "label": label}
