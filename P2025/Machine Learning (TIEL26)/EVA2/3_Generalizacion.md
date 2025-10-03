# Tarea 3: Generalización

## ¿Qué es la Generalización?

En machine learning, la **generalización** es la capacidad de un modelo para adaptarse y funcionar bien con datos nuevos y desconocidos, después de haber sido entrenado con un conjunto de datos de entrenamiento.

En otras palabras, un modelo que generaliza bien no se limita a "memorizar" las respuestas de los datos que ya ha visto, sino que es capaz de **aprender los patrones subyacentes** en ellos. Este aprendizaje le permite hacer predicciones precisas sobre datos que nunca antes ha encontrado.

La generalización es, posiblemente, el objetivo más importante del machine learning.

## El Dilema: Underfitting vs. Overfitting

El reto de la generalización se encuentra en encontrar un equilibrio entre dos problemas comunes:

1.  **Underfitting (Subajuste):**
    - **¿Qué es?** El modelo es **demasiado simple** y no logra capturar los patrones fundamentales de los datos. 
    - **Resultado:** Funciona mal tanto en los datos de entrenamiento como en los de prueba. No ha aprendido lo suficiente.

2.  **Overfitting (Sobreajuste):**
    - **¿Qué es?** El modelo es **demasiado complejo** y aprende no solo los patrones, sino también el "ruido" y las fluctuaciones aleatorias de los datos de entrenamiento.
    - **Resultado:** Funciona extremadamente bien con los datos de entrenamiento (casi de memoria), pero falla estrepitosamente con datos nuevos porque el ruido que memorizó no está presente en ellos.

El objetivo es un **"buen ajuste" (good fit)**, un modelo que se encuentra en el punto medio.

## Ejemplo Práctico: Ajuste de Polinomios

Imaginemos que queremos que un modelo aprenda una curva (una función coseno con ruido).

- **Datos de entrenamiento:** Puntos azules.
- **Función verdadera (lo que queremos aprender):** Línea verde.
- **Modelo aprendido:** Línea roja.

#### Caso 1: Buen Ajuste (Buena Generalización)

Un modelo con la complejidad adecuada (un polinomio de grado 4) aprende la forma general de la curva sin seguir cada punto ruidoso.

- **Resultado:** La línea roja del modelo se parece mucho a la línea verde (la función verdadera). Este modelo hará buenas predicciones para nuevos puntos.

![Buen Ajuste](https://i.imgur.com/6mZ8e3L.png) *(Referencia del notebook `ejemplo_generalizacion.ipynb`)*

#### Caso 2: Overfitting (Mala Generalización)

Un modelo demasiado complejo (un polinomio de grado 15) intenta pasar por todos y cada uno de los puntos de entrenamiento.

- **Resultado:** La línea roja se retuerce de forma errática para tocar todos los puntos azules. Aunque es perfecta para los datos de entrenamiento, se aleja drásticamente de la función verdadera. Este modelo hará predicciones muy malas para nuevos puntos.

![Overfitting](https://i.imgur.com/6mZ8e3L.png) *(Referencia del notebook `ejemplo_generalizacion.ipynb`)*

## ¿Cómo se Logra una Buena Generalización?

- **Usando un conjunto de validación/prueba:** Separar los datos en conjuntos de entrenamiento y prueba es crucial para poder medir objetivamente qué tan bien generaliza el modelo.
- **Regularización:** Aplicar técnicas que limitan la complejidad del modelo (como limitar la profundidad de un árbol de decisión) para evitar que se sobreajuste.
- **Validación Cruzada:** Evaluar el modelo en múltiples subconjuntos de los datos para obtener una estimación más estable de su rendimiento.
