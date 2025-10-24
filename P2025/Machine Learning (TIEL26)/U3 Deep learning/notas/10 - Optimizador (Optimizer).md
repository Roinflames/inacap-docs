# Optimizador (Optimizer)
En deep learning, un optimizador es el algoritmo o método matemático que ajusta los pesos y sesgos de una red neuronal con el fin de minimizar la función de pérdida durante el entrenamiento.

Los optimizadores determinan cómo se actualan los parámetros después de calcular el gradiente (a través del algoritmo de retropropagación). Su función es guiar la red para que aprenda de manera eficiente y converja hacia una buena solución.

## Ejemplo simple:
Si la pérdida indica que la red cometió un error, el optimizador decide cuánto y en qué dirección ajustar cada peso para reducir ese error en el siguiente paso.

## Tipos comunes de optimizadores:

SGD (Stochastic Gradient Descent): actualiza los pesos en cada lote de datos; simple pero lento.

Momentum: mejora el SGD agregando una “inercia” que suaviza los cambios bruscos.

RMSprop: ajusta automáticamente la tasa de aprendizaje para cada parámetro.

Adam (Adaptive Moment Estimation): combina Momentum y RMSprop; es el más usado actualmente por su eficiencia y estabilidad.

## Fórmula general (ejemplo con SGD):
wnuevo​=wviejo​−η⋅∇L(w)

donde:

w: pesos del modelo
η: tasa de aprendizaje
∇L(w): gradiente de la función de pérdida respecto a los pesos

## En resumen:
El optimizador es quien decide cómo aprende la red neuronal —es el motor que ajusta sus parámetros para que el modelo se acerque cada vez más a la respuesta correcta.