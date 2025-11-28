# Retropropagación (Backpropagation)

## Definición:
La retropropagación es un algoritmo fundamental en el entrenamiento de redes neuronales artificiales. Su función principal es ajustar los pesos y sesgos de la red para minimizar el error entre las predicciones del modelo y los valores reales.

## Cómo funciona:

Propagación hacia adelante: se calcula la salida del modelo a partir de las entradas y los pesos actuales.

Cálculo del error: se mide la diferencia entre la salida obtenida y la deseada mediante una función de pérdida.

Propagación hacia atrás: el error se distribuye desde la capa de salida hacia las capas anteriores, calculando los gradientes (derivadas parciales) de la función de pérdida con respecto a cada peso.

Actualización de pesos: se ajustan los pesos utilizando un algoritmo de optimización (como descenso del gradiente) para reducir el error.

## Importancia:
La retropropagación permite que las redes neuronales aprendan de los datos y mejoren su rendimiento con cada iteración del entrenamiento. Es la base del aprendizaje profundo (Deep Learning).

## Ejemplo simple:
En una red que intenta reconocer dígitos escritos a mano, la retropropagación ajusta los pesos de las neuronas cada vez que la red se equivoca, haciendo que las predicciones futuras sean más precisas.

Palabras clave: gradiente, descenso del gradiente, error, derivadas parciales, función de pérdida, entrenamiento supervisado.
