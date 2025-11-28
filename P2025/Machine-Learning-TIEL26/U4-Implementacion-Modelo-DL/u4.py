"""
Cargar y Probar el Modelo Entrenado (Clase U4 – Implementación de Modelo Deep Learning)

En esta sección aprenderemos a cargar un modelo previamente entrenado utilizando la librería transformers y 
a realizar predicciones nuevas sin necesidad de reentrenarlo. Esto es especialmente útil cuando trabajamos 
con pipenv, entornos aislados o cuando reiniciamos el runtime (Google Colab, VSCode, etc.).
"""
# 1. Activar ambiente virtual (pipenv) dentro de "Machine Learning (TIEL26)\" y ejecutar script principal
"""
Antes de probar el modelo, primero activamos el ambiente virtual donde se instalaron las dependencias:

# Activar ambiente virtual (pipenv)
cd "Machine Learning (TIEL26)"
pipenv shell

# Ir a la unidad correspondiente
cd "U4 Implementación modelo Deep learning"

# Ejecutar el script del entrenamiento
python u4.py
"""
#  2. Cargar el modelo previamente guardado
"""
Cuando ya tenemos un modelo fine-tuneado, HuggingFace nos permite cargarlo desde una carpeta local. La carpeta debe contener:
- pytorch_model.bin → pesos del modelo
- config.json → arquitectura
- tokenizer.json / vocab.txt → vocabulario
- tokenizer_config.json
"""
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("./modelo_entrenado")
tokenizer = AutoTokenizer.from_pretrained("./modelo_entrenado")

# 3. Realizar predicciones con textos nuevos
# Prueba con texto nuevo positivo
text = "This movie was absolutely amazing!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
pred = outputs.logits.argmax().item()
print("Positiva" if pred == 1 else "Negativa")

# Prueba con texto nuevo negativo
text = "This movie was absolutely shitty!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
pred = outputs.logits.argmax().item()
print("Positiva" if pred == 1 else "Negativa")

# Explicación conceptual para la clase
"""
- Tokenización: Convierte el texto a tensores que el modelo puede procesar.
- Modelo: AutoModelForSequenceClassification ejecuta un forward pass y nos entrega logits.
- Predicción (argmax):
    - 0 → Clase "Negativa"
    - 1 → Clase "Positiva"

Estos ejemplos permiten verificar que el modelo está funcionando después de reiniciar el runtime o en una nueva sesión pipenv.
"""