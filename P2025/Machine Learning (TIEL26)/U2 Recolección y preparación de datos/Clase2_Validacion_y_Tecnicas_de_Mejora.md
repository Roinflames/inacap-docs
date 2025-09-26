
# Clase 2: Validación y Técnicas para Mejorar Datos

**Fecha:** 26/09/2025

**Tema central:** Validación y técnicas para mejorar datos

---

## 1. Introducción

En la clase anterior, discutimos la importancia de la **generalización**: la capacidad de un modelo para funcionar bien con datos nuevos y no vistos. Vimos que un modelo que "memoriza" los datos de entrenamiento sufre de **overfitting** y no es útil en la práctica.

Hoy nos enfocaremos en las técnicas que nos permiten **medir y asegurar** que nuestro modelo generaliza correctamente. La pregunta clave es: **¿Cómo podemos confiar en que nuestro modelo funcionará en el mundo real?**

La respuesta está en la **validación** y en las estrategias para mejorar la calidad y cantidad de nuestros datos.

---

## 2. Validación de Datos: ¿Cómo medimos el rendimiento real?

La idea fundamental es simple: **nunca evalúes tu modelo con los mismos datos que usaste para entrenarlo**. Si lo haces, un modelo con overfitting siempre parecerá perfecto.

### a. Partición Train/Test (Hold-Out)

La estrategia más básica es dividir nuestro conjunto de datos en dos:

1.  **Conjunto de Entrenamiento (Train Set):** Se utiliza para que el modelo aprenda los patrones. Típicamente, es el 70%-80% de los datos.
2.  **Conjunto de Prueba (Test Set):** Se mantiene "oculto" durante el entrenamiento y se usa una sola vez al final para evaluar el rendimiento del modelo final. Es nuestra simulación de "datos nuevos".

**Proceso:**
1.  Mezclar los datos aleatoriamente.
2.  Dividir los datos en `train` y `test`.
3.  Entrenar el modelo **solo** con el `train set`.
4.  Evaluar el modelo con el `test set` para obtener una métrica de rendimiento (ej. accuracy, F1-score, etc.).

```python
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# X: features, y: labels
# Suponiendo que X e y ya están cargados con tus datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar el modelo
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluar el modelo
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy en el conjunto de prueba: {accuracy:.2f}")
```

**Limitación del Hold-Out:** El rendimiento puede depender mucho de *cómo* se hizo la división. Si por casualidad en el `test set` caen los ejemplos más "fáciles", nuestro modelo parecerá mejor de lo que es (y viceversa).

---

## 3. Validación Cruzada (Cross-Validation)

Para solucionar la limitación del hold-out, usamos la validación cruzada. Es una técnica más robusta que nos da una estimación más estable del rendimiento del modelo.

### a. K-Fold Cross-Validation

Es el método más común. El proceso es el siguiente:

1.  Dividir el conjunto de datos (sin contar el `test set` final) en **K** "pliegues" (folds) de igual tamaño. Un valor común para K es 5 o 10.
2.  Realizar **K** iteraciones. En cada iteración:
    *   Se usa un pliegue diferente como **conjunto de validación**.
    *   Se usan los **K-1** pliegues restantes como **conjunto de entrenamiento**.
3.  El rendimiento final es el **promedio** del rendimiento obtenido en las K iteraciones.

![K-Fold](https://scikit-learn.org/stable/_images/grid_search_cross_validation.png)

**Ventajas:**
*   **Estimación más robusta:** El rendimiento no depende de una única división de los datos.
*   **Uso eficiente de los datos:** Todos los datos se usan tanto para entrenar como para validar en algún punto.

```python
from sklearn.model_selection import cross_val_score

# Crear el modelo
model = KNeighborsClassifier(n_neighbors=3)

# Realizar validación cruzada con K=5
# cv=5 significa 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"Scores de cada fold: {scores}")
print(f"Accuracy promedio (CV): {scores.mean():.2f}")
print(f"Desviación estándar (CV): {scores.std():.2f}")
```
Una desviación estándar baja nos indica que el rendimiento del modelo es estable a través de diferentes subconjuntos de datos.

---

## 4. Etiquetado de Datos (Data Labeling)

El aprendizaje supervisado (clasificación, regresión) depende de tener **datos etiquetados**. Una etiqueta es la "respuesta correcta" que el modelo debe aprender a predecir.

*   **Ejemplo de clasificación:** En un dataset de imágenes, la etiqueta es "perro" o "gato".
*   **Ejemplo de regresión:** En un dataset de casas, la etiqueta es el `precio`.

**¿De dónde vienen las etiquetas?**
*   **Etiquetado Manual:** Un humano revisa cada dato y le asigna la etiqueta correcta. Es costoso y lento, pero a menudo es la única forma de obtener etiquetas de alta calidad. Herramientas como Labelbox o VGG Image Annotator ayudan en este proceso.
*   **Etiquetado Automático/Programático:** Se usan reglas, heurísticas u otros modelos para asignar etiquetas de forma automática. Es más rápido y barato, pero puede introducir ruido o errores.

La calidad de las etiquetas es **fundamental**. Un mal etiquetado (ej. asignar "perro" a una foto de un gato) es como darle a un estudiante un libro con respuestas incorrectas.

---

## 5. Aumento de Datos (Data Augmentation)

¿Qué hacemos si tenemos pocos datos? ¡Inventamos más! El **aumento de datos** es una técnica para crear nuevos datos de entrenamiento a partir de los existentes, aplicando transformaciones que no cambian la etiqueta.

**Objetivo:** Ayudar al modelo a generalizar mejor y reducir el overfitting.

### a. Aumento de Datos para Imágenes

Podemos aplicar transformaciones geométricas o de color:
*   Rotación
*   Zoom (acercar/alejar)
*   Traslación (mover la imagen)
*   Flip (horizontal/vertical)
*   Cambios de brillo o contraste

![Data Augmentation](https://nanonets.com/blog/content/images/2021/01/data_augmentation_synopsis.png)
*Fuente: nanonets.com*

### b. Aumento de Datos para Texto

*   **Reemplazo de sinónimos:** Cambiar palabras por otras con significado similar.
    *   "El coche es rápido" → "El auto es veloz".
*   **Traducción inversa (Back-translation):** Traducir el texto a otro idioma y luego de vuelta al original.
    *   "Me gusta el helado" → (inglés) "I like ice cream" → (español) "Disfruto el helado".

### c. Oversampling para Datos Tabulares

En problemas de clasificación con **clases desbalanceadas** (ej. 99% de transacciones no son fraude, 1% sí lo son), el modelo puede aprender a ignorar la clase minoritaria.

Técnicas como **SMOTE** (Synthetic Minority Over-sampling Technique) crean ejemplos sintéticos de la clase minoritaria para balancear el dataset.

---

## 6. Actividades Prácticas

### a. Ejercicio Práctico con Scikit-learn

Usando el dataset `train.csv` de la carpeta `ejemplos` (dataset de Titanic):
1.  Carguen los datos y seleccionen algunas características numéricas (ej. `Age`, `Fare`, `Pclass`) y la variable objetivo (`Survived`).
2.  Pre-procesen los datos si es necesario (ej. rellenar valores faltantes).
3.  Implementen una validación cruzada (K-Fold con K=5) para un modelo de clasificación como `KNeighborsClassifier` o `DecisionTreeClassifier`.
4.  Reporten el accuracy promedio y su desviación estándar.
5.  Discutan: ¿Qué nos dice el resultado sobre la estabilidad del modelo?

### b. Discusión en Grupos

Dividirse en grupos y discutir la siguiente pregunta:

> **“En un proyecto real para predecir la deserción de estudiantes en INACAP, ¿qué errores de validación podrían ocurrir y cómo los evitarían? Piensen en cómo están distribuidos los datos (ej. por carrera, por año, por sede) y cómo eso podría afectar una simple partición train/test.”**

Preparen una breve conclusión para compartir con la clase.
