[Presentación](https://gamma.app/docs/Overfitting-en-Machine-Learning-sur7qyq114nn0vo?mode=doc)
# Tarea 4: Overfitting (Sobreajuste)

## ¿Qué es el Overfitting?

El **overfitting** o **sobreajuste** es uno de los problemas más comunes en machine learning. Ocurre cuando un modelo aprende "demasiado bien" los datos de entrenamiento, hasta el punto de que empieza a memorizar el ruido y las peculiaridades específicas de ese conjunto de datos, en lugar de los patrones generales subyacentes.

Un modelo sobreajustado es como un estudiante que memoriza las respuestas de un examen de práctica pero no entiende los conceptos. Cuando se enfrenta a un examen real con preguntas ligeramente diferentes (datos nuevos), su rendimiento es muy bajo.

**En resumen:** El modelo tiene un rendimiento excelente en los datos de entrenamiento, pero falla al generalizar a datos nuevos.

## ¿Cómo Detectar el Overfitting?

La forma más clara de detectar el overfitting es comparar el rendimiento del modelo en el conjunto de **entrenamiento** versus el conjunto de **prueba**.

- **Señal de Alerta:**
  - **Precisión de Entrenamiento (Training Accuracy):** Muy alta (ej. 99-100%).
  - **Precisión de Prueba (Test/Validation Accuracy):** Notablemente más baja (ej. 75-85%).

Una **gran diferencia** entre estas dos métricas es un indicador claro de que el modelo no está generalizando bien y ha sobreajustado.

### Ejemplo Práctico: Árbol de Decisión

Entrenamos dos árboles de decisión para predecir la supervivencia en el Titanic:

1.  **Árbol sin restricciones:** Le permitimos crecer tan profundo como quiera.
2.  **Árbol regularizado:** Limitamos su profundidad a `max_depth=4`.

**Resultados del Modelo con Overfitting (sin restricciones):**
- Precisión en Entrenamiento: **97.99%**
- Precisión en Prueba: **75.35%**
- **Diferencia:** ~22.6%

La enorme caída en la precisión revela un sobreajuste severo.

**Resultados del Modelo Regularizado (`max_depth=4`):**
- Precisión en Entrenamiento: **83.37%**
- Precisión en Prueba: **81.40%**
- **Diferencia:** ~2.0%

Aquí, las precisiones son muy similares, lo que indica que el modelo ha generalizado mucho mejor.

## ¿Cómo Prevenir el Overfitting?

Existen varias estrategias para combatir el sobreajuste:

1.  **Regularización:** Es la técnica más común. Consiste en añadir una penalización a la complejidad del modelo para forzarlo a ser más simple.
    - **Para Árboles de Decisión:** Limitar la `max_depth` (profundidad máxima) o `min_samples_leaf` (muestras mínimas por hoja).
    - **Para Regresión Lineal/Logística:** Usar regularización L1 (Lasso) o L2 (Ridge), que penalizan los coeficientes grandes.

2.  **Conseguir más Datos:** Un conjunto de datos más grande y diverso hace más difícil que el modelo memorice el ruido. A menudo, esta es la solución más efectiva, aunque no siempre es posible.

3.  **Aumento de Datos (Data Augmentation):** Si no se pueden conseguir más datos, se pueden generar artificialmente nuevas muestras a partir de las existentes (rotando imágenes, cambiando palabras por sinónimos, etc.).

4.  **Validación Cruzada (Cross-Validation):** Proporciona una estimación más robusta del rendimiento del modelo, lo que ayuda a elegir un modelo que generalice mejor y no esté sobreajustado a una única división de datos de prueba.

5.  **Simplificar el Modelo:** Usar un modelo inherentemente más simple (ej. Regresión Logística en lugar de un Random Forest con muchos árboles) o reducir el número de características (variables) de entrada.
