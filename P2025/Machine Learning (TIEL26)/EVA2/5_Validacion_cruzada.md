# Tarea 5: Validación Cruzada (Cross-Validation)

## ¿Qué es la Validación Cruzada?

La **validación cruzada** es una técnica de evaluación de modelos que proporciona una medida más fiable y estable de su rendimiento en datos no vistos. En lugar de hacer una única división de datos (entrenamiento y prueba), la validación cruzada divide los datos en múltiples subconjuntos y entrena y evalúa el modelo repetidamente.

El objetivo es asegurarse de que el rendimiento medido del modelo no dependa de una "división afortunada" de los datos.

## El Problema con un Único Train/Test Split

Cuando usamos una única división de datos (ej. 80% para entrenar, 20% para probar), el rendimiento que obtenemos en el conjunto de prueba puede ser engañoso. 

- Si, por casualidad, el conjunto de prueba contiene muestras "fáciles", obtendremos una puntuación demasiado optimista.
- Si contiene muestras "difíciles" o atípicas, la puntuación será demasiado pesimista.

La validación cruzada resuelve este problema promediando los resultados de múltiples divisiones.

## ¿Cómo Funciona K-Fold Cross-Validation?

**K-Fold** es el método de validación cruzada más popular. El proceso es el siguiente:

1.  **Dividir los datos:** Se divide aleatoriamente todo el conjunto de datos en `k` subconjuntos de igual tamaño, llamados **"pliegues" (folds)**. Un valor común para `k` es 5 o 10.

2.  **Iterar y Entrenar:** Se realizan `k` iteraciones. En cada iteración:
    - Un pliegue se reserva como **conjunto de prueba**.
    - Los `k-1` pliegues restantes se utilizan como **conjunto de entrenamiento**.
    - Se entrena el modelo con los datos de entrenamiento y se evalúa con los datos de prueba.

3.  **Promediar los Resultados:** Al final de las `k` iteraciones, se tienen `k` puntuaciones de rendimiento. La puntuación final del modelo es el **promedio** de estas `k` puntuaciones.

### Ejemplo Visual (con k=5)

| Iteración | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Resultado |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | <span style="color:red">Prueba</span> | Entrenamiento | Entrenamiento | Entrenamiento | Entrenamiento | **Score 1** |
| **2** | Entrenamiento | <span style="color:red">Prueba</span> | Entrenamiento | Entrenamiento | Entrenamiento | **Score 2** |
| **3** | Entrenamiento | Entrenamiento | <span style="color:red">Prueba</span> | Entrenamiento | Entrenamiento | **Score 3** |
| **4** | Entrenamiento | Entrenamiento | Entrenamiento | <span style="color:red">Prueba</span> | Entrenamiento | **Score 4** |
| **5** | Entrenamiento | Entrenamiento | Entrenamiento | Entrenamiento | <span style="color:red">Prueba</span> | **Score 5** |

**Rendimiento Final = Promedio(Score 1, Score 2, Score 3, Score 4, Score 5)**

## Beneficios de la Validación Cruzada

1.  **Estimación de Rendimiento más Robusta:** El resultado promedio es una estimación mucho más fiable de cómo funcionará el modelo en datos del mundo real.

2.  **Uso Eficiente de los Datos:** Todos los datos se utilizan tanto para entrenamiento como para prueba en algún momento. Esto es especialmente valioso cuando se tienen conjuntos de datos pequeños.

3.  **Detección de Variabilidad:** La desviación estándar de las `k` puntuaciones nos dice qué tan sensible es el modelo a diferentes subconjuntos de datos. Una desviación estándar alta puede ser una señal de que el modelo no es estable.

### Ejemplo Práctico

Al evaluar un modelo de Regresión Logística en el dataset del Titanic:

- **Precisión con un único Train/Test Split:** `79.07%`
- **Resultados con Validación Cruzada (k=5):**
  - Puntuaciones: `[0.7622, 0.8112, 0.7832, 0.7902, 0.8308]`
  - **Precisión Promedio:** `79.55%`
  - **Desviación Estándar:** `0.0265`

La validación cruzada nos muestra que el rendimiento del modelo fluctúa entre ~76% y ~83%, y que el `79.55%` es una estimación más confiable de su rendimiento general.
