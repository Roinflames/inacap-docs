# Despliegue de Modelos de Machine Learning en la Nube

El despliegue de modelos de Machine Learning (ML) en la nube consiste en poner un modelo entrenado en un entorno de producción accesible a través de internet. Esto permite que las aplicaciones consuman las predicciones del modelo sin necesidad de alojar la infraestructura computacional localmente.

## ¿Por qué Desplegar en la Nube?

- **Escalabilidad:** Los proveedores de la nube (como AWS, Google Cloud, Azure) permiten ajustar los recursos computacionales (CPU, GPU, RAM) de forma dinámica según la demanda de predicciones.
- **Accesibilidad:** Una vez desplegado, el modelo puede ser consumido por diversas aplicaciones (web, móviles, IoT) desde cualquier lugar a través de una API REST.
- **Costo-Eficiencia:** Se paga solo por los recursos que se utilizan, evitando grandes inversiones iniciales en hardware.
- **Mantenimiento Simplificado:** El proveedor de la nube se encarga de la gestión y el mantenimiento de la infraestructura subyacente.

## Métodos Comunes de Despliegue en la Nube

1.  **Inferencia en Tiempo Real (Online):**
    - Se despliega el modelo como un punto final (endpoint) de una API.
    - La aplicación envía una solicitud (e.g., un JSON con los datos de entrada) al endpoint y recibe una predicción en tiempo real.
    - Ideal para aplicaciones interactivas que requieren respuestas inmediatas.

2.  **Inferencia por Lotes (Batch):**
    - Se utiliza para procesar grandes volúmenes de datos de una sola vez.
    - Un proceso programado ejecuta el modelo sobre un conjunto de datos almacenado (e.g., en un data lake) y guarda las predicciones para su uso posterior.
    - Ideal para análisis periódicos, informes o cuando no se necesita una respuesta instantánea.

## Pasos Típicos para el Despliegue

1.  **Empaquetado del Modelo:** Se serializa el modelo entrenado (e.g., usando `pickle` o `joblib` en Python) y se empaqueta junto con su código de inferencia y dependencias en un contenedor (usualmente Docker).
2.  **Creación de una API:** Se utiliza un framework como **FastAPI** o **Flask** para crear una API que reciba datos, los procese, los pase al modelo y devuelva la predicción.
3.  **Selección del Servicio en la Nube:**
    - **Plataformas de ML Gestionadas:**
        - **AWS SageMaker:** Ofrece un ecosistema completo para entrenar, desplegar y monitorear modelos.
        - **Google Vertex AI:** Plataforma unificada de Google Cloud para todo el ciclo de vida de ML.
        - **Azure Machine Learning:** Solución de Microsoft que se integra con su ecosistema de servicios.
    - **Servicios de Contenedores:**
        - **AWS ECS/EKS, Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS):** Para desplegar contenedores Docker a gran escala.
    - **Funciones como Servicio (Serverless):**
        - **AWS Lambda, Google Cloud Functions, Azure Functions:** Para desplegar modelos más pequeños y ejecutar inferencias de forma económica y escalable.
4.  **Despliegue y Monitoreo:** Se sube el contenedor a la plataforma elegida y se configura el endpoint. Es crucial monitorear el rendimiento del modelo, la latencia y los costos para asegurar su correcto funcionamiento.

## Ejemplo con FastAPI y Docker

Un flujo de trabajo común sería:
1. Entrenar un modelo y guardarlo.
2. Crear una aplicación con **FastAPI** que cargue el modelo y defina una ruta `/predict`.
3. Escribir un **Dockerfile** para instalar Python, las librerías necesarias, y copiar el código de la API y el modelo.
4. Construir la imagen de Docker y subirla a un registro de contenedores (como Docker Hub, AWS ECR, o Google Container Registry).
5. Desplegar esa imagen en un servicio de nube como AWS SageMaker, Vertex AI, o un clúster de Kubernetes.
