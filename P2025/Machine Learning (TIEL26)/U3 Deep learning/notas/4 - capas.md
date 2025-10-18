# Glosario: Capas (Layers)
En el contexto de las redes neuronales artificiales, una capa es una estructura fundamental que agrupa un conjunto de neuronas (o nodos) que procesan información de manera conjunta.

Cada capa recibe entradas, aplica una transformación matemática (por ejemplo, multiplicación por pesos, suma de sesgos y función de activación) y envía salidas a la siguiente capa.
## Tipos de capas principales
### 1. Capa de entrada (Input Layer)
- Es la primera capa de la red.
- Recibe los datos de entrada (por ejemplo, píxeles de una imagen o características numéricas).
- No realiza cálculos complejos; solo pasa los datos al siguiente nivel.
### 2. Capas ocultas (Hidden Layers)
- Son las capas intermedias entre la entrada y la salida.
- Realizan la mayor parte del procesamiento y aprendizaje mediante operaciones con pesos, sesgos y funciones de activación.
- En redes profundas hay muchas capas ocultas, de ahí el nombre deep learning.
### 3. Capa de salida (Output Layer)
- Entrega el resultado final del modelo (por ejemplo, una clase en clasificación o un valor numérico en regresión).
- Suele usar funciones de activación específicas, como Softmax (clasificación multiclase) o Sigmoid (binaria).
## Ejemplo conceptual
Si pensamos en una red que clasifica imágenes de gatos y perros:
- La capa de entrada recibe los píxeles de la imagen.
- Las capas ocultas procesan patrones (bordes, formas, texturas).
- La capa de salida entrega la probabilidad de “gato” o “perro”.
## En PyTorch
Las capas suelen definirse desde el módulo torch.nn, por ejemplo:
```python
import torch.nn as nn

# Ejemplo: red simple con una capa oculta
modelo = nn.Sequential(
    nn.Linear(4, 8),   # capa totalmente conectada (input=4, output=8)
    nn.ReLU(),         # función de activación
    nn.Linear(8, 2)    # capa de salida (2 clases)
)
```