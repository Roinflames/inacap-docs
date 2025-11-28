# Glosario: Pesos (Weights)
# ¿Qué son los pesos?
Los pesos son los parámetros ajustables de una red neuronal.
Determinan cuánto influye cada entrada en la salida de una neurona o capa.

📖 En palabras simples:

Los pesos son los “botones” que la red ajusta durante el entrenamiento para aprender relaciones entre los datos.
## 1. Representación matemática
En una red neuronal simple (perceptrón):
```
y=f(w1​x1​+w2​x2​+⋯+wn​xn​+b)
```
Donde:
𝑥𝑖 → entradas
𝑤𝑖 → pesos
𝑏 → sesgo (bias)
𝑓 → función de activación
𝑦 → salida

Los pesos determinan la pendiente o inclinación de la función.
El entrenamiento busca valores de 𝑤𝑖 y 𝑏 que minimicen el error (loss).
## 2. Pesos en PyTorch
En PyTorch, los pesos están almacenados dentro de los módulos (nn.Module) y son tensores con gradiente habilitado.
```python
import torch
import torch.nn as nn

# Red simple
modelo = nn.Linear(2, 1)  # 2 entradas, 1 salida

print(modelo.weight)  # Pesos
print(modelo.bias)    # Bias
```
Salida típica:
```bash
Parameter containing:
tensor([[0.1234, -0.5321]], requires_grad=True)
```
Nota: requires_grad=True significa que PyTorch calculará gradientes sobre esos pesos durante el entrenamiento.
## 3. Inicialización de pesos
Antes de entrenar, los pesos se inicializan (normalmente al azar).
Esto es importante porque una mala inicialización puede impedir el aprendizaje.

Ejemplos comunes:
- Uniforme o normal aleatoria: valores pequeños al azar.
- Xavier/Glorot: ideal para capas lineales con activaciones simétricas (tanh).
- He initialization: ideal para ReLU o LeakyReLU.

```python
nn.init.xavier_uniform_(modelo.weight)
nn.init.zeros_(modelo.bias)
```
## 4. Actualización de pesos
Durante el entrenamiento, los pesos se actualizan usando el gradiente descendente:
wnuevo ​= wviejo​ − η ⋅ (∂L/∂w​)

Donde:

- 𝜂: tasa de aprendizaje (learning rate)
- ∂𝐿/∂𝑤: gradiente del error respecto al peso

```python
optimizer.zero_grad()  # Limpia gradientes
loss.backward()        # Calcula gradientes
optimizer.step()       # Actualiza pesos
```
## 5. Bias (sesgo)
El bias o sesgo es un parámetro adicional que permite desplazar la función de activación,
lo que ayuda a que el modelo aprenda relaciones incluso si las entradas son cero.

Ejemplo en PyTorch:
```python
print(modelo.bias)  # tensor con requires_grad=True
```
## 6. Congelar o desbloquear pesos
A veces se necesita congelar pesos (por ejemplo, al hacer transfer learning).
Así PyTorch no los actualiza durante el entrenamiento:
```python
for param in modelo.parameters():
    param.requires_grad = False
```
Para volver a entrenarlos:
```python
for param in modelo.parameters():
    param.requires_grad = True
```
## 7. Visualización e inspección de pesos
Puedes ver los valores actuales de los pesos de un modelo:
```python
for name, param in modelo.named_parameters():
    print(name, param.data)
```
O convertirlos a NumPy:
```python
param_numpy = modelo.weight.data.numpy()
```
## 8. Pesos en distintas capas
| Tipo de capa               | Nombre de parámetro            | Forma típica      | Ejemplo                                |
| -------------------------- | ------------------------------ | ----------------- | -------------------------------------- |
| `nn.Linear(in, out)`       | `weight`                       | `[out, in]`       | `[10, 5]` → 10 neuronas, 5 entradas    |
| `nn.Conv2d(in, out, k, k)` | `weight`                       | `[out, in, k, k]` | 32 filtros de 3×3 sobre 3 canales      |
| `nn.LSTM`                  | `weight_ih_l0`, `weight_hh_l0` | Matrices grandes  | Para conexiones internas y recurrentes |

## 9. Regularización de pesos
Para evitar sobreajuste, se aplican penalizaciones a los pesos grandes:

L2 regularization (Weight decay):

```text
L' = L + λ ∑(wi²)
```

En PyTorch:

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
```

## 10. Guardar y cargar pesos
Los pesos son lo que realmente “aprende” un modelo.
Puedes guardarlos y reutilizarlos fácilmente:

```python
torch.save(modelo.state_dict(), 'pesos.pth')
modelo.load_state_dict(torch.load('pesos.pth'))
```

## En resumen
| Concepto            | Descripción                                                        |
| ------------------- | ------------------------------------------------------------------ |
| **Pesos (Weights)** | Parámetros ajustables que determinan la influencia de cada entrada |
| **Bias (sesgo)**    | Desplaza la función de activación                                  |
| **Inicialización**  | Valores iniciales de los pesos (aleatorios o estratégicos)         |
| **Actualización**   | Se modifican con gradiente descendente                             |
| **Regularización**  | Evita pesos excesivos para mejorar generalización                  |
| **State dict**      | Estructura donde PyTorch guarda los pesos y biases                 |

# Ejemplo visual (mental):

Entrada → [ w1, w2, w3, ... ] → Neurona → Activación → Salida
          ↑ Pesos que se ajustan en cada epoch
