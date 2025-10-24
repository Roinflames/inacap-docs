# Sesgo (Bias)

## Definición:
En deep learning, el sesgo puede referirse a dos conceptos principales:

### Sesgo del modelo (bias matemático):
Es un parámetro adicional en las neuronas de una red neuronal que permite desplazar la función de activación hacia arriba o abajo. Este término mejora la capacidad del modelo para ajustarse a los datos, ya que sin él, todas las salidas estarían forzadas a pasar por el origen (cero).

Ejemplo: En la ecuación de una neurona y=w1​x1​+w2​x2​+b, el término 𝑏 es el sesgo.

### Sesgo de aprendizaje o sesgo estadístico:
Se refiere a los errores sistemáticos que ocurren cuando un modelo aprende patrones incorrectos o incompletos debido a:

Datos de entrenamiento no representativos o desequilibrados (por ejemplo, pocas muestras de ciertos grupos).

Suposiciones erróneas sobre la relación entre variables.
Este tipo de sesgo puede generar predicciones injustas o distorsionadas, especialmente en modelos usados en contextos sociales o médicos.

### Importancia:
Un sesgo adecuado en la arquitectura del modelo es necesario para aprender correctamente, pero un sesgo estadístico en los datos o el proceso de entrenamiento puede afectar la equidad y precisión del sistema.