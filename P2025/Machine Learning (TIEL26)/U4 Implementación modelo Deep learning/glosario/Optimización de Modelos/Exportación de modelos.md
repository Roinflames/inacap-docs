# Exportación de Modelos de Machine Learning

La **exportación de modelos** (a menudo llamada **serialización**) es el proceso de guardar un modelo de Machine Learning entrenado, junto con su arquitectura y sus pesos, en un archivo. Este paso es fundamental para mover el modelo desde el entorno de desarrollo (donde fue entrenado) a un entorno de producción (donde hará predicciones sobre datos nuevos).

Sin la exportación, un modelo solo existiría en la memoria durante la sesión de entrenamiento y se perdería al finalizar el script.

---

## ¿Por Qué Exportar un Modelo?

- **Despliegue (Deployment):** Es el objetivo principal. Un modelo exportado puede ser cargado en un servidor, una aplicación móvil o un dispositivo embebido para servir predicciones.
- **Persistencia:** Permite guardar el estado de un modelo que ha costado horas o días de entrenamiento, para poder reutilizarlo sin necesidad de volver a entrenar.
- **Interoperabilidad:** Ciertos formatos permiten que un modelo entrenado en un framework (e.g., PyTorch) pueda ser utilizado en otro (e.g., TensorFlow) o en un entorno que no sea Python (e.g., C++, Java).
- **Compartir y Colaborar:** Facilita que otros miembros del equipo puedan usar, evaluar o mejorar el modelo.

---

## Formatos de Exportación Comunes

La elección del formato depende del framework de entrenamiento, el entorno de despliegue y los requisitos de rendimiento.

### Formatos Nativos de Frameworks

Son específicos de cada librería y la forma más directa de guardar un modelo.

- **`pickle` / `joblib` (Scikit-learn):**
    - **Descripción:** `pickle` es la librería estándar de Python para serializar objetos. `joblib` es una versión optimizada para objetos grandes, como los modelos de Scikit-learn que contienen arrays de NumPy.
    - **Uso:** `joblib.dump(model, 'model.joblib')`
    - **Ventajas:** Extremadamente simple para modelos de Scikit-learn.
    - **Desventajas:** **Solo compatible con Python**. No es seguro cargar archivos `pickle` de fuentes no confiables. Puede haber problemas de compatibilidad entre versiones de librerías.

- **`SavedModel` (TensorFlow):**
    - **Descripción:** Es el formato estándar y más robusto de TensorFlow. Guarda todo: la arquitectura del modelo, los pesos, y el grafo de computación completo. Es una carpeta que contiene archivos `.pb` y subdirectorios.
    - **Uso:** `model.save('my_model_directory')`
    - **Ventajas:** Es independiente de la versión del código fuente original. Es el formato de entrada para **TensorFlow Serving** y **TensorFlow Lite**.
    - **Desventajas:** Es una carpeta, no un único archivo, lo que puede ser menos conveniente para la distribución.

- **`.h5` o `.keras` (Keras / TensorFlow):**
    - **Descripción:** Formato de archivo único que guarda la arquitectura, los pesos, la configuración del entrenamiento (optimizador, pérdida) y el estado del optimizador.
    - **Uso:** `model.save('my_model.h5')` o `model.save('my_model.keras')`
    - **Ventajas:** Conveniente por ser un solo archivo.
    - **Desventajas:** Menos robusto que `SavedModel` para despliegues complejos.

- **`.pt` o `.pth` (PyTorch):**
    - **Descripción:** El formato de PyTorch. Generalmente, lo que se guarda es el `state_dict`, un diccionario de Python que mapea cada capa a su tensor de pesos.
    - **Uso:** `torch.save(model.state_dict(), 'model_weights.pth')`
    - **Ventajas:** Flexible. Permite guardar solo los pesos o el objeto del modelo completo.
    - **Desventajas:** Para cargar el modelo, se necesita tener definida la clase de la arquitectura del modelo en el código.

### Formatos de Interoperabilidad

Estos formatos están diseñados para ser independientes del framework.

- **ONNX (Open Neural Network Exchange):**
    - **Descripción:** Un formato abierto y estándar de la industria para modelos de ML. Actúa como un puente entre diferentes frameworks y herramientas.
    - **Uso:** Se exporta el modelo desde PyTorch o TensorFlow a un archivo `.onnx`.
    - **Ventajas:** **Máxima interoperabilidad**. Permite entrenar en un framework y desplegar en otro. Es la base para motores de inferencia de alto rendimiento como **ONNX Runtime** (que puede usar GPUs con CUDA o TensorRT).
    - **Desventajas:** La conversión no siempre es perfecta y puede fallar para arquitecturas muy nuevas o complejas.

- **TensorFlow Lite (`.tflite`):**
    - **Descripción:** No es un formato de exportación directo, sino el resultado de una **conversión**. Se toma un modelo de TensorFlow (`SavedModel` o `.h5`) y se convierte a `.tflite`.
    - **Uso:** Es el formato optimizado para desplegar modelos en **dispositivos móviles y embebidos**.
    - **Ventajas:** El modelo es cuantificado (optimizado) para ser más pequeño, rápido y eficiente energéticamente.
    - **Desventajas:** Es un formato específico para inferencia en el borde (edge).

La elección del formato es una decisión de arquitectura clave en cualquier proyecto de MLOps.
