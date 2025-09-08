# 📅 Planificación Unidad 2.1 – Machine Learning: Requerimientos de los datos

## Clase 1 – 12/09/2025
Tema central: Tipos de datos y Generalización
### Contenidos:
Tipos de datos en ML (estructurados, no estructurados, numéricos, categóricos, texto, imágenes, etc.).

Relación entre problema → tipo de dato → tipo de modelo.

Concepto de generalización: aprender patrones que funcionen en nuevos datos.

Introducción a overfitting y underfitting con ejemplos gráficos.
### Actividades:
Ejercicio práctico: analizar un conjunto de datos (Titanic, MNIST o uno simple de CSV) y discutir:

¿Qué tipo de datos hay?

¿Para qué problema serían útiles?

Mini debate: ¿qué pasa si un modelo “memoriza” vs. si “generaliza”?

## Clase 2 – 26/09/2025
Tema central: Validación y técnicas para mejorar datos
### Contenidos:
Validación de datos: partición train/test, importancia de separar conjuntos.

Validación cruzada (cross-validation): k-fold, ventajas vs. hold-out.

Etiquetado de datos: necesidad, ejemplos de etiquetado manual/automático.

Aumento de datos (data augmentation): imágenes, texto, oversampling.
### Actividades:
Ejercicio práctico con scikit-learn: validación cruzada con un dataset pequeño.

Discusión en grupos: “¿Qué errores de validación podrían ocurrir en un dataset real de su área (ej: salud, comercio, transporte)?”

## Clase 3 – 03/10/2025
Tema central: Integración de conceptos + Introducción a la Eva2
### Contenidos:
Repaso general: tipos de datos + generalización + validación + etiquetado + aumento de datos + overfitting.

Ejemplos de casos reales:

Dataset de imágenes → problema de clasificación.

Dataset tabular → predicción numérica.

Dataset texto → análisis de sentimiento.

Conexión entre teoría y práctica.
### Actividades:
Kahoot o quiz de repaso.

Presentación de la Evaluación 2 (Eva2):

Entrega: se explica en clase y se entrega ese mismo día (03/10).

Plazo: 1 semana de desarrollo (entrega final el 10/10).

Formato sugerido: análisis de un caso donde deben:

Describir el tipo de datos necesarios.

Explicar cómo garantizar generalización.

Diseñar un esquema de validación.

Identificar riesgos de overfitting y proponer mejoras (ej: aumento de datos).
## ✅ Sugerencia de Evaluación 2 (Eva2)
Consigna posible:

Dado un problema de Machine Learning a elección (clasificación de correos spam, predicción de clientes que abandonan un servicio, reconocimiento de objetos en imágenes, etc.), describe los requerimientos de los datos necesarios para resolverlo.
Incluye: tipo de datos, generalización, validación, etiquetado, aumento de datos y posibles problemas de overfitting.

Ponderación sugerida:

Tipos de datos → 20%

Generalización → 20%

Validación de datos → 20%

Etiquetado y aumento de datos → 20%

Identificación de riesgos de overfitting → 20%