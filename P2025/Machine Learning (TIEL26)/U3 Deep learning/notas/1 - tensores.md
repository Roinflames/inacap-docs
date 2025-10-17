# Glosario: Tensores en PyTorch
# ¿Qué es un tensor?
Un tensor es la estructura de datos fundamental en PyTorch (y en la mayoría de los frameworks de deep learning).
Es similar a un arreglo o matriz de NumPy, pero con capacidades adicionales:

- puede correr en GPU,
- permite autodiferenciación (para entrenamiento de redes neuronales),
- y puede tener cualquier número de dimensiones.

## Tipos según sus dimensiones
| Nombre                   | Ejemplo en código                | Descripción                                              |
| ------------------------ | -------------------------------- | -------------------------------------------------------- |
| **Escalar (0D)**         | `torch.tensor(5)`                | Un solo número.                                          |
| **Vector (1D)**          | `torch.tensor([1, 2, 3])`        | Una lista de números.                                    |
| **Matriz (2D)**          | `torch.tensor([[1, 2], [3, 4]])` | Filas y columnas.                                        |
| **Tensor 3D**            | `torch.randn(3, 3, 3)`           | Por ejemplo, una secuencia de 3 imágenes 3×3.            |
| **Tensor 4D o superior** | `torch.randn(16, 3, 28, 28)`     | Usado en CNN: batch de 16 imágenes RGB de 28×28 píxeles. |

## Propiedades principales
| Propiedad       | Ejemplo           | Descripción                                                   |
| --------------- | ----------------- | ------------------------------------------------------------- |
| `shape`         | `x.shape`         | Dimensiones del tensor (ej: `(3, 4, 2)`)                      |
| `dtype`         | `x.dtype`         | Tipo de dato (`torch.float32`, `torch.int64`, etc.)           |
| `device`        | `x.device`        | Indica si está en CPU o GPU                                   |
| `requires_grad` | `x.requires_grad` | Si PyTorch debe rastrear operaciones para calcular gradientes |

## Creación de tensores
```python
import torch

# Desde listas o tuplas
x = torch.tensor([[1, 2], [3, 4]])

# Tensor de ceros o unos
a = torch.zeros(3, 3)
b = torch.ones(2, 2)

# Tensor con valores aleatorios
r = torch.randn(4, 4)

# Tensor con rango secuencial
t = torch.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
```
## Operaciones comunes
```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

print(x + y)        # Suma elemento a elemento
print(x * y)        # Multiplicación elemento a elemento
print(torch.dot(x, y))  # Producto punto
print(x.mean())     # Promedio
print(x.view(3, 1)) # Cambiar forma (reshape)
```
## Tensores y GPU
```python
x = torch.randn(2, 2)
x = x.to('cuda')      # Mover a GPU
x = x.to('cpu')       # Volver a CPU
```
## Tensores y gradientes (autograd)
```python
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 3*x + 1
y.backward()           # Calcula dy/dx
print(x.grad)          # → tensor([7.])
```
## Relación con NumPy
```python
import numpy as np

a = np.array([1, 2, 3])
t = torch.from_numpy(a)      # NumPy → Tensor
b = t.numpy()                # Tensor → NumPy
```
## En resumen
- Un tensor es una matriz generalizada que puede tener cualquier número de dimensiones.
- Es el bloque básico de datos en PyTorch.
- Se usa en todas las operaciones de torch.nn, desde pesos de redes neuronales hasta entradas de datos.