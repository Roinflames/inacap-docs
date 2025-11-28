# Función de Pérdida (Loss Function)

## Definición:
La función de pérdida es una medida que indica qué tan bien o mal está funcionando un modelo de aprendizaje automático. Calcula la diferencia entre las predicciones del modelo y los valores reales (etiquetas o resultados esperados). Su valor numérico representa el "error" del modelo, y el objetivo durante el entrenamiento es minimizar esa pérdida.

## En otras palabras:
La función de pérdida le dice al modelo qué tan equivocado está, y sirve como guía para ajustar los parámetros (pesos y sesgos) durante el entrenamiento.

### Ejemplo:

En un problema de regresión, se usa comúnmente el Error Cuadrático Medio (MSE):

MSE=n1​i=1∑n​(yi​−y^i​​)2

donde 𝑦𝑖 es el valor real y 𝑦^𝑖 la predicción del modelo.

En clasificación, se usa la Entropía Cruzada (Cross-Entropy Loss), que penaliza más fuerte los errores de predicción con alta confianza.

### Importancia en Deep Learning:
La función de pérdida es el corazón del proceso de aprendizaje. Es a partir de ella que el modelo ajusta sus parámetros mediante propagación hacia atrás (backpropagation), buscando reducir el error global.

### Ejemplo intuitivo:
Imagina que lanzas dardos a un blanco: la función de pérdida mide qué tan lejos están tus lanzamientos del centro. Cuanto más cerca del centro (resultado correcto), menor es la pérdida.