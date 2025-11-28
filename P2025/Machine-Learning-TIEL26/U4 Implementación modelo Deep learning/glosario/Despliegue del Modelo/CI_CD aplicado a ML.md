# CI/CD Aplicado a Machine Learning (MLOps)

La **Integración Continua (CI)** y la **Entrega/Despliegue Continuo (CD)** son prácticas de MLOps para automatizar y optimizar el ciclo de vida de los modelos de Machine Learning. A diferencia del desarrollo de software tradicional, en ML, el pipeline no solo depende del código, sino también de los datos y los modelos.

## Conceptos Clave

- **Integración Continua (CI):** Automatiza la integración y prueba de código, datos y modelos. En MLOps, la CI se extiende para incluir:
    - **Validación de Código:** Pruebas unitarias y de integración.
    - **Validación de Datos:** Comprobación de la calidad, formato y distribución de los datos para detectar anomalías o derivas (*data drift*).
    - **Validación de Modelos:** Evaluación del rendimiento del modelo contra métricas predefinidas.

- **Entrega Continua (CD):** Automatiza el empaquetado y despliegue de los modelos de ML y su infraestructura. En MLOps, esto a menudo significa desplegar un **pipeline de entrenamiento de ML** completo, que a su vez puede desplegar el servicio de predicción del modelo.

- **Entrenamiento Continuo (CT):** Es un concepto adicional en MLOps. Se refiere a la automatización del reentrenamiento de modelos, que puede ser activado por la disponibilidad de nuevos datos o por una degradación en el rendimiento del modelo en producción.

## Fases de un Pipeline de CI/CD para MLOps

1.  **Control de Versiones:** Uso de herramientas como Git para versionar código, datos (o metadatos de datos), y configuraciones de modelos.
2.  **Build y Test:** Compilación de código, ejecución de pruebas unitarias y de integración.
3.  **Validación de Datos y Modelos:** Pruebas automatizadas para asegurar la calidad de los datos y el rendimiento del modelo.
4.  **Entrenamiento del Modelo:** Ejecución de scripts de entrenamiento de forma automatizada.
5.  **Empaquetado:** Creación de un contenedor (e.g., Docker) con el modelo y todas sus dependencias.
6.  **Despliegue:** Publicación del modelo en un entorno de producción, ya sea como un servicio de API, en un dispositivo de borde (*edge*), etc.
7.  **Monitoreo:** Seguimiento continuo del rendimiento del modelo en producción para detectar degradación y activar alertas o reentrenamientos.

## Beneficios

- **Velocidad:** Acelera la entrega de nuevos modelos.
- **Fiabilidad:** Reduce errores humanos a través de la automatización.
- **Reproducibilidad:** Asegura que los experimentos y resultados sean consistentes y trazables.
- **Escalabilidad:** Facilita la gestión de múltiples modelos en producción.

## Herramientas Comunes

- **Orquestación:** Jenkins, GitLab CI/CD, GitHub Actions, Kubeflow, TFX (TensorFlow Extended).
- **Contenerización:** Docker, Kubernetes.
- **Plataformas Cloud:** AWS SageMaker, Google Vertex AI, Azure Machine Learning.
- **Seguimiento de Experimentos:** MLflow, DVC.
