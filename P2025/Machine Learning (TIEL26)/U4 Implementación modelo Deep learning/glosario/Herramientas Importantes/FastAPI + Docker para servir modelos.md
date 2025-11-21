# FastAPI + Docker: La Combinación Perfecta para Servir Modelos de ML

Cuando un modelo de Machine Learning está entrenado, el siguiente paso es "servirlo", es decir, ponerlo en producción para que pueda recibir datos y devolver predicciones. La combinación de **FastAPI** y **Docker** se ha convertido en el estándar de la industria para esta tarea por su eficiencia, escalabilidad y reproducibilidad.

---

## ¿Qué Rol Cumple cada Herramienta?

### FastAPI: El Servidor de API

**FastAPI** es un framework web de Python moderno y de alto rendimiento. Su función es crear una **API (Interfaz de Programación de Aplicaciones)** que actúe como una puerta de entrada a nuestro modelo.

- **Crea un "Endpoint":** Expone una URL (por ejemplo, `/predict`) a la que otras aplicaciones pueden enviar solicitudes HTTP.
- **Recibe Datos:** Acepta datos de entrada (las características para la predicción), generalmente en formato JSON.
- **Invoca al Modelo:** Carga el modelo de ML previamente entrenado, le pasa los datos recibidos y obtiene la predicción.
- **Devuelve la Predicción:** Envía la predicción de vuelta a la aplicación que la solicitó, también en formato JSON.

**¿Por qué FastAPI?**
- **Rendimiento:** Es extremadamente rápido, ideal para inferencia en tiempo real.
- **Fácil de Usar:** Su sintaxis es simple y moderna.
- **Validación de Datos:** Usa Pydantic para validar automáticamente los datos de entrada, evitando errores.
- **Documentación Automática:** Genera una documentación interactiva (Swagger UI) de la API de forma automática, lo que facilita enormemente las pruebas y la integración.

### Docker: El Contenedor de la Aplicación

**Docker** es una plataforma de contenerización. Su función es empaquetar nuestra aplicación FastAPI, el modelo de ML y **todas sus dependencias** en una unidad aislada y portátil llamada **contenedor**.

- **Resuelve el "Funciona en mi Máquina":** El contenedor incluye todo lo necesario para ejecutar la aplicación: el código de Python, la versión correcta de las librerías (TensorFlow, PyTorch, Scikit-learn, etc.), el modelo serializado y hasta el sistema operativo base.
- **Garantiza la Reproducibilidad:** Asegura que el entorno de ejecución sea idéntico en desarrollo, pruebas y producción.
- **Portabilidad:** Un contenedor Docker puede ejecutarse en cualquier máquina que tenga Docker instalado, ya sea un portátil, un servidor local (*on-premise*) o cualquier proveedor de la nube (AWS, GCP, Azure).
- **Aislamiento y Escalabilidad:** Cada contenedor se ejecuta de forma aislada. Si la demanda aumenta, es muy fácil lanzar múltiples copias idénticas del contenedor para distribuir la carga.

---

## Flujo de Trabajo Típico

1.  **Entrenar y Guardar el Modelo:** Se entrena el modelo y se guarda en un archivo (e.g., `model.joblib`, `model.h5`).

2.  **Crear la App FastAPI (`main.py`):**
    - Se importa FastAPI.
    - Se carga el modelo guardado al iniciar la aplicación.
    - Se define un "endpoint" (e.g., `@app.post("/predict")`).
    - Se define la lógica para recibir datos, hacer la predicción y devolverla.

3.  **Listar Dependencias (`requirements.txt`):**
    - Se crea un archivo de texto con todas las librerías de Python necesarias (e.g., `fastapi`, `uvicorn`, `scikit-learn`).

4.  **Crear el Contenedor (`Dockerfile`):**
    - Es un archivo de texto con instrucciones para construir la imagen de Docker.
    - **`FROM python:3.9`**: Usa una imagen base de Python.
    - **`COPY . .`**: Copia todos los archivos del proyecto (código, modelo, etc.) dentro de la imagen.
    - **`RUN pip install -r requirements.txt`**: Instala las dependencias.
    - **`CMD ["uvicorn", "main:app"]`**: Especifica el comando para iniciar el servidor FastAPI cuando se ejecute el contenedor.

5.  **Construir y Ejecutar:**
    - **`docker build -t mi-modelo-api .`**: Construye la imagen del contenedor.
    - **`docker run -p 8000:8000 mi-modelo-api`**: Ejecuta el contenedor, haciendo que la API sea accesible en el puerto 8000 de la máquina anfitriona.

El resultado es un servicio de ML robusto, reproducible y listo para ser desplegado en cualquier entorno, desde un servidor local hasta una plataforma en la nube a gran escala.
