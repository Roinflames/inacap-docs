# MLOps con TFX (TensorFlow Extended)

**TensorFlow Extended (TFX)** es una plataforma de Google, de nivel de producción, para implementar prácticas de **MLOps (Machine Learning Operations)**. TFX proporciona un conjunto de herramientas y componentes para construir y gestionar pipelines de Machine Learning de extremo a extremo, desde la ingesta de datos hasta el despliegue y monitoreo del modelo.

Es la misma tecnología que Google utiliza internamente para sus propios productos de ML a gran escala.

---

## ¿Qué es un Pipeline de TFX?

Un pipeline de TFX es un **Grafo Acíclico Dirigido (DAG)** donde cada nodo es un **componente** que realiza una tarea específica en el ciclo de vida de ML. Los componentes están diseñados para ser modulares y reutilizables, y se comunican entre sí a través de artefactos almacenados en un repositorio de metadatos (ML Metadata).

### Componentes Estándar de TFX

1.  **`ExampleGen`**:
    - **Función:** Es el punto de entrada del pipeline. Ingiere datos de diversas fuentes (CSV, BigQuery, etc.).
    - **Salida:** Divide los datos en conjuntos de entrenamiento y evaluación.

2.  **`StatisticsGen`**:
    - **Función:** Calcula estadísticas descriptivas detalladas para cada característica de los datos (media, desviación estándar, valores faltantes, etc.).
    - **Salida:** Un artefacto de estadísticas que puede ser visualizado con `tfdv.visualize_statistics`.

3.  **`SchemaGen`**:
    - **Función:** Infiere un esquema de los datos basándose en las estadísticas generadas. El esquema define los tipos de datos, la valencia (si es un valor único o una lista) y la presencia esperada de cada característica.
    - **Salida:** Un esquema que actúa como un "contrato" para los datos.

4.  **`ExampleValidator`**:
    - **Función:** Compara los nuevos lotes de datos con el esquema para detectar anomalías y derivas (*data drift*). Es crucial para asegurar la calidad de los datos que entran al modelo.
    - **Salida:** Un reporte de anomalías.

5.  **`Transform`**:
    - **Función:** Realiza la ingeniería de características (preprocesamiento). Crea transformaciones (como normalización, codificación one-hot, etc.) que se aplican de manera consistente tanto en el entrenamiento como en la inferencia.
    - **Salida:** Un grafo de TensorFlow que se puede adjuntar al modelo, evitando el sesgo de entrenamiento-servicio (*training-serving skew*).

6.  **`Trainer`**:
    - **Función:** Entrena el modelo de Machine Learning utilizando la API de TensorFlow (generalmente Keras).
    - **Salida:** El modelo entrenado.

7.  **`Evaluator`**:
    - **Función:** Realiza un análisis profundo del rendimiento del modelo sobre el conjunto de evaluación. Permite comparar el nuevo modelo con una versión anterior (el modelo actualmente en producción) para decidir si el nuevo es "suficientemente bueno" para ser desplegado.
    - **Salida:** Métricas de evaluación y una decisión de "bendición" (blessing) del modelo.

8.  **`Pusher`**:
    - **Función:** Si el `Evaluator` bendice el modelo, el `Pusher` lo despliega en un entorno de servicio.
    - **Salida:** El modelo copiado a una infraestructura de despliegue, como **TensorFlow Serving**, o a un registro de modelos.

### Orquestación

Un pipeline de TFX necesita un **orquestador** para ejecutar los componentes en el orden correcto y gestionar las dependencias. TFX es flexible y se puede ejecutar con varios orquestadores:
- **Local:** Para desarrollo y pruebas rápidas.
- **Kubeflow Pipelines:** La opción recomendada para producción en clústeres de Kubernetes.
- **Apache Airflow:** Un orquestador de flujos de trabajo muy popular.
- **Google Cloud Vertex AI Pipelines:** Un servicio totalmente gestionado en GCP para ejecutar pipelines de TFX (y otros) sin administrar la infraestructura.

### ML Metadata (MLMD)

Cada vez que se ejecuta un pipeline, TFX registra automáticamente información sobre cada componente, sus artefactos de entrada/salida y sus parámetros en **ML Metadata**. Esto proporciona una trazabilidad completa, permitiendo:
- Ver el linaje de un modelo (qué datos y qué código se usaron para entrenarlo).
- Comparar experimentos.
- Depurar pipelines.

## ¿Por qué usar TFX para MLOps?

- **Robustez y Escalabilidad:** Está diseñado para manejar terabytes de datos y flujos de trabajo complejos.
- **Automatización End-to-End:** Permite la implementación de **CI/CD/CT (Entrenamiento Continuo)** para modelos de ML.
- **Prevención de Errores Comunes:** Ayuda a evitar problemas como el *data drift* y el *training-serving skew*.
- **Ecosistema TensorFlow:** Se integra perfectamente con todo el ecosistema de TensorFlow, incluyendo TensorFlow Data Validation (TFDV), TensorFlow Transform (TFT) y TensorFlow Model Analysis (TFMA).
