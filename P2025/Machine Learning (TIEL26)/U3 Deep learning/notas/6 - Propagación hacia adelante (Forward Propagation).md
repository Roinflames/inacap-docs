# Propagación hacia adelante (Forward Propagation)

## Definición:
La propagación hacia adelante es el proceso mediante el cual una red neuronal toma los datos de entrada y los hace pasar a través de sus capas (ocultas y de salida), aplicando en cada una operaciones matemáticas (como multiplicaciones por pesos, sumas con sesgos y funciones de activación) para generar una salida final o predicción.

### En otras palabras:
Es la “ida” del flujo de información dentro de la red, donde los datos se transforman capa a capa hasta producir el resultado que la red estima.

### Ejemplo conceptual:

- Se ingresa un vector de entrada 𝑥.
- Cada neurona calcula z=w⋅x+b (pesos y sesgo).
- Se aplica una función de activación a=f(z).
- El resultado 𝑎 pasa a la siguiente capa hasta llegar a la salida.

### Rol en el entrenamiento:
La salida generada por la propagación hacia adelante se compara con el valor real (etiqueta) para calcular el error o pérdida. Este error luego se utiliza en la propagación hacia atrás (backpropagation) para ajustar los pesos de la red.

### Analogía simple:
Es como si la red neuronal “pensara hacia adelante”: toma la información, la procesa paso a paso y llega a una conclusión (su predicción).
