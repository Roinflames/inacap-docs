`torch.nn` es uno de los módulos más importantes de PyTorch.
Su nombre completo significa "Torch Neural Networks", y su propósito es facilitar la creación, entrenamiento y evaluación de redes neuronales.

`torch.nn` contiene bloques básicos para construir modelos de deep learning, como `capas` (Linear, Conv2d, etc.), `funciones de activación` (ReLU, Sigmoid), y `utilidades para calcular pérdidas` (CrossEntropyLoss, MSELoss, etc.).

# Estructura y componentes principales

## 1. Capas (Layers)

Se usan para definir la arquitectura del modelo.

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 128),  # Capa totalmente conectada
    nn.ReLU(),            # Activación
    nn.Linear(128, 10)    # Capa de salida
)
```
## 2.Funciones de activación

Introducen no linealidad en la red.
```python
nn.ReLU()
nn.Sigmoid()
nn.Tanh()
```

## 3. Funciones de pérdida (Loss Functions)

Miden qué tan bien está aprendiendo la red.
```python
loss_fn = nn.CrossEntropyLoss()
```

## 4. Módulo base: nn.Module

Toda red neuronal en PyTorch debe heredar de nn.Module.

Permite definir el modelo, los parámetros y cómo se procesan los datos.
```python
class MiRed(nn.Module):
    def __init__(self):
        super(MiRed, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)
```

# Relación con otros módulos
| Módulo             | Función principal                            |
| ------------------ | -------------------------------------------- |
| `torch`            | Tensores y operaciones matemáticas básicas   |
| `torch.nn`         | Construcción de modelos neuronales           |
| `torch.optim`      | Algoritmos de optimización (SGD, Adam, etc.) |
| `torch.utils.data` | Manejo de datasets y dataloaders             |

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Definir red simple
class Modelo(nn.Module):
    def __init__(self):
        super(Modelo, self).__init__()
        self.linear = nn.Linear(1, 1)  # y = wx + b

    def forward(self, x):
        return self.linear(x)

# Crear instancia
modelo = Modelo()

# Definir pérdida y optimizador
criterio = nn.MSELoss()
optimizador = optim.SGD(modelo.parameters(), lr=0.01)

# Entrenamiento
for epoch in range(100):
    x = torch.randn(10, 1)
    y = 3 * x + 2

    pred = modelo(x)
    loss = criterio(pred, y)

    optimizador.zero_grad()
    loss.backward()
    optimizador.step()

print("w y b aprendidos:", list(modelo.parameters()))
```