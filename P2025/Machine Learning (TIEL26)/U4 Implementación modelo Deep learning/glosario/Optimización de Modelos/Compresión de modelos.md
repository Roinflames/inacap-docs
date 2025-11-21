# Compresión de Modelos de Machine Learning

La **compresión de modelos** es un conjunto de técnicas utilizadas para reducir el tamaño (en disco y en memoria) y la complejidad computacional de los modelos de Machine Learning, especialmente de las redes neuronales profundas. El objetivo es hacer que los modelos sean más eficientes, rápidos y adecuados para su despliegue en entornos con recursos limitados, como dispositivos móviles o embebidos (Edge AI / TinyML).

La compresión busca un equilibrio entre la reducción del tamaño y la latencia, y la preservación de la precisión del modelo. Un modelo más pequeño y rápido no es útil si su capacidad para hacer predicciones correctas se degrada significativamente.

---

## ¿Por qué Comprimir Modelos?

Los modelos de Deep Learning modernos, como los grandes modelos de lenguaje (LLMs) o los modelos de visión por computadora, pueden tener cientos de millones o incluso miles de millones de parámetros. Esto los hace:

- **Grandes:** Ocupan mucho espacio de almacenamiento.
- **Lentos:** Requieren una gran cantidad of operaciones de punto flotante (FLOPs) para realizar una sola predicción, lo que aumenta la latencia.
- **Costosos:** Su ejecución requiere hardware potente (GPUs, TPUs), lo que incrementa los costos de despliegue.
- **Consumen mucha energía:** Limita su uso en dispositivos que dependen de una batería.

La compresión aborda directamente estos problemas.

---

## Técnicas Principales de Compresión

Existen varias técnicas que se pueden usar de forma individual o combinada. Las más importantes son:

### 1. Poda (Pruning)

- **Idea:** Eliminar parámetros (pesos) "no importantes" de la red neuronal. Muchos modelos están sobre-parametrizados, lo que significa que tienen conexiones neuronales redundantes que contribuyen poco o nada a la predicción final.
- **¿Cómo funciona?:** Se identifican los pesos con una magnitud cercana a cero y se eliminan (se establecen en cero). Esto crea matrices de pesos "dispersas" (con muchos ceros), que pueden ser almacenadas y procesadas de manera más eficiente.
- **Tipos:**
    - **Poda no estructurada:** Elimina pesos individuales de forma irregular.
    - **Poda estructurada:** Elimina estructuras completas, como neuronas enteras o canales de convolución, lo que facilita la aceleración en hardware estándar.

### 2. Cuantificación (Quantization)

- **Idea:** Reducir la precisión numérica utilizada para almacenar los pesos y las activaciones del modelo.
- **¿Cómo funciona?:** Por defecto, los pesos se almacenan como números de punto flotante de 32 bits (FP32). La cuantificación los convierte a formatos de menor precisión, como punto flotante de 16 bits (FP16) o, más comúnmente, enteros de 8 bits (INT8).
- **Beneficios:**
    - **Reducción de tamaño:** Usar INT8 en lugar de FP32 reduce el tamaño del modelo en **4 veces**.
    - **Aceleración:** Las operaciones con enteros son mucho más rápidas en la mayoría de las CPUs y en hardware especializado (como las TPUs de Google o los Tensor Cores de NVIDIA).

### 3. Destilación de Conocimiento (Knowledge Distillation)

- **Idea:** Entrenar un modelo pequeño y eficiente (el "estudiante") para que imite el comportamiento de un modelo grande y complejo (el "maestro").
- **¿Cómo funciona?:** El modelo maestro, que tiene un alto rendimiento, se utiliza para generar "etiquetas suaves" (las probabilidades de salida completas, no solo la clase predicha). El modelo estudiante se entrena para replicar tanto las etiquetas verdaderas del conjunto de datos como las etiquetas suaves del maestro. De esta manera, el estudiante aprende los "patrones de razonamiento" del maestro.
- **Resultado:** Se obtiene un modelo compacto que logra una precisión mucho mayor de la que lograría si se entrenara solo desde cero.

### 4. Factorización de Bajo Rango (Low-Rank Factorization)

- **Idea:** Descomponer las grandes matrices de pesos de las capas densas en matrices más pequeñas.
- **¿Cómo funciona?:** Se basa en la observación de que muchas matrices de pesos son de "bajo rango", lo que significa que contienen información redundante. Técnicas como la Descomposición en Valores Singulares (SVD) pueden aproximar una matriz grande `W` (de tamaño `m x n`) como el producto de dos matrices más pequeñas `U` y `V` (de tamaños `m x k` y `k x n`, donde `k` es mucho menor que `m` y `n`).
- **Resultado:** Se reduce drásticamente el número de parámetros necesarios para representar la capa, disminuyendo el tamaño y el costo computacional.

Estas técnicas son fundamentales en el campo de **TinyML** y son implementadas en frameworks como **TensorFlow Lite** y **PyTorch Mobile** para hacer que la IA sea omnipresente y eficiente.
