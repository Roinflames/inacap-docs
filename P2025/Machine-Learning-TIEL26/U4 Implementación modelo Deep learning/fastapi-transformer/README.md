cd P2025\Machine Learning (TIEL26)\U4 Implementación modelo Deep learning\mi_modelo_api
# 1. Estructura del proyecto (recomendada)
mi_modelo_api/
├─ modelo_entrenado/        # carpeta exportada de HuggingFace (pytorch_model.bin, config.json, tokenizer...)
├─ main.py                  # FastAPI app (carga y endpoints)
├─ client_test.py           # script opcional para probar la API
├─ requirements.txt
├─ Dockerfile
└─ README.md                # (opcional) pasos para la clase

# 2. main.py — FastAPI que carga el modelo al iniciar
[main.py](./main.py)

# 3. requirements.txt
pipenv install --python 3.10
pipenv install -r requirements.txt
pipenv shell

# 4. Ejecutar sin Docker (rápido para demo en clase)
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 5. client_test.py — script para probar la API desde Python
python client_test.py

# 6. Dockerfile — crear imagen para clase / despliegue
[Dockerfile](./Dockerfile)

# 7. Pruebas curl (útiles en clase)
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"text\":\"This movie was absolutely amazing!\"}"

# 8. Ideas para la demostración en clase (30–40 minutos)
- 1. Intro (5 min): explicar el flujo: entrenar → exportar carpeta modelo → cargar en FastAPI → exponer endpoint → consumir.

- 2. Demo local (10 min):

Activar venv/pipenv.

uvicorn main:app y abrir /docs.

Probar POST /predict con ejemplos positivos y negativos.

- 3. Mostrar client_test.py haciendo la petición desde Python (3 min).

- 4. Docker (10 min):

Mostrar Dockerfile.

docker build (puedes hacerlo antes de la clase si toma tiempo).

docker run y probar con curl.

- 5. Q&A y troubleshooting (5–10 min).

# 9. Posibles problemas y soluciones rápidas
- Instalación de torch falla: explicar que la instalación depende de la plataforma (CPU vs GPU). Si hay problemas, usar una imagen base con torch ya instalada o ejecutar en una VM con torch.

- Modelo no carga: revisar que ./modelo_entrenado exista y tenga pytorch_model.bin, config.json y los archivos del tokenizer.

- GPU detectada pero errores: forzar CPU temporalmente poniendo device = "cpu" en main.py o ejecutando CUDA_VISIBLE_DEVICES="" uvicorn ....

- Tiempo de arranque largo: el primer from_pretrained puede tardar; para la demo, cargar modelo antes de la clase o mostrar log de carga.

# 10. Variantes y mejoras (opcional para la asignatura)
- Endpoint batch (/predict_batch) que acepte lista de textos.

- Endpoint que devuelva probabilidades con softmax.

- Caching y pooling de solicitudes para mayor throughput (usar fastapi.ConcurrencyLimiter o colas).

- Añadir una interfaz web simple (HTML + JS) para que los estudiantes prueben desde el navegador.

- Instrumentación: agregar logs y métricas (Prometheus) para clase avanzada.