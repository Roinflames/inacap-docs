# Poda de Modelos (Pruning)

La **poda** (o *pruning* en inglés) es una técnica de compresión de modelos que consiste en **eliminar sistemáticamente los parámetros (pesos) menos importantes** de una red neuronal entrenada.

La intuición detrás de la poda es que muchas redes neuronales están **sobre-parametrizadas**, lo que significa que contienen neuronas y conexiones redundantes que contribuyen muy poco a la predicción final. Eliminar estas conexiones no solo reduce el tamaño del modelo, sino que también puede disminuir el costo computacional y, en algunos casos, mejorar la capacidad de generalización al reducir el sobreajuste (overfitting).

---

## ¿Cómo Funciona la Poda?

El proceso general de poda suele ser iterativo y sigue estos pasos:

1.  **Entrenar el Modelo:** Se entrena una red neuronal de manera convencional hasta que alcance la precisión deseada.

2.  **Identificar Pesos a Podar:** Se establece un criterio para medir la "importancia" de cada peso en la red. El criterio más común y simple es la **magnitud del peso**: se asume que los pesos con valores absolutos más pequeños (cercanos a cero) son los menos importantes.

3.  **Podar el Modelo:** Se eliminan los pesos que no cumplen con el criterio de importancia. En la práctica, esto significa establecer sus valores a cero, creando **matrices de pesos dispersas** (con un alto porcentaje de ceros). Se define un **nivel de escasez (sparsity)**, que es el porcentaje de pesos que se van a podar (e.g., 50%, 80%, 90%).

4.  **Ajuste Fino (Fine-Tuning):** Después de la poda, la precisión del modelo generalmente disminuye. Para recuperarla, el modelo podado se vuelve a entrenar durante unas pocas épocas con una tasa de aprendizaje baja. Este paso permite que los pesos restantes se reajusten para compensar los que fueron eliminados.

Estos pasos (podar y re-entrenar) se pueden repetir de forma iterativa para alcanzar niveles de escasez muy altos (superiores al 90%) con una pérdida mínima de precisión.

---

## Tipos de Poda

### 1. Poda no Estructurada (Unstructured Pruning)

- **¿Qué es?:** Se eliminan pesos individuales de cualquier parte de la red, basándose únicamente en su magnitud.
- **Resultado:** Se obtiene una matriz de pesos dispersa, sin un patrón regular de ceros.
- **Ventajas:** Puede alcanzar niveles de escasez muy altos sin una gran pérdida de precisión.
- **Desventajas:** **No siempre se traduce en una aceleración real en hardware de propósito general (CPUs, GPUs)**. Las librerías y el hardware están optimizados para operaciones con matrices densas. Para aprovechar la dispersión se necesita hardware o librerías especializadas que soporten la multiplicación de matrices dispersas.

### 2. Poda Estructurada (Structured Pruning)

- **¿Qué es?:** En lugar de eliminar pesos individuales, se eliminan **estructuras completas** de la red.
- **Ejemplos:**
    - **Poda de neuronas/nodos:** Se eliminan neuronas enteras (todas sus conexiones de entrada y salida).
    - **Poda de filtros/canales:** En las Redes Neuronales Convolucionales (CNNs), se eliminan filtros o canales completos de las capas convolucionales.
- **Resultado:** La arquitectura de la red se vuelve más pequeña y las matrices de pesos siguen siendo densas, pero de menor tamaño.
- **Ventajas:** **Sí se traduce en una aceleración directa en hardware estándar**. Al eliminar un filtro completo, por ejemplo, se reduce el número de operaciones de convolución a realizar.
- **Desventajas:** Es una técnica más "agresiva" y puede causar una mayor pérdida de precisión que la poda no estructurada para el mismo número de pesos eliminados.

La poda es una técnica fundamental en la optimización de modelos, y a menudo se combina con la **cuantificación** para lograr la máxima compresión y eficiencia. Frameworks como TensorFlow (a través del *TensorFlow Model Optimization Toolkit*) y PyTorch proporcionan herramientas para aplicar estas técnicas de poda.
