# Glosario: Funciones de Activación en PyTorch
# ¿Qué es una función de activación?

Una función de activación introduce no linealidad en una red neuronal, permitiendo que aprenda patrones complejos.
Sin estas funciones, una red sería solo una combinación lineal (como una regresión múltiple).

## 1. ReLU — Rectified Linear Unit
Nombre en PyTorch: nn.ReLU() o F.relu(x)

Fórmula:
```
f(x)=max(0,x)
```
- Intuición: deja pasar valores positivos y corta los negativos (los vuelve 0).
- Ventajas: rápida, sencilla y evita saturación.
- Uso típico: redes convolucionales (CNN), perceptrones multicapa (MLP).

```python
import torch.nn as nn
act = nn.ReLU()
```
Gráfico mental:
```
x < 0 → 0  
x ≥ 0 → x
```
# 2. Leaky ReLU
Nombre: nn.LeakyReLU(negative_slope=0.01)

Fórmula:
```
f(x) = { x       ​si x>0
        0.01x   i x≤0​
```    
# 3. Sigmoid
Nombre: nn.Sigmoid()

Fórmula:
```
f(x) = 1 / (1 + e ** −x)
```    
- Rango: (0, 1)
- Intuición: convierte valores en probabilidades.
- Uso típico: salida de modelos binarios (clasificación 0/1).
- Problema: se “aplasta” en los extremos (gradientes pequeños → aprendizaje lento).
# 4. Tanh — Tangente hiperbólica
Nombre: nn.Tanh()

Fórmula:
```
f(x)=tanh(x)=ex+e−xex−e−x​
```    
- Rango: (-1, 1)
- Intuición: similar a Sigmoid, pero centrada en cero → mejora la estabilidad en algunas redes.
- Uso típico: redes recurrentes (RNN, LSTM).
# 5. Softmax
Nombre: nn.Softmax(dim=1)

Fórmula:
```
f(xi​) = e ** x sub i​​ / (∑ sub j ​e ** x sub j​)
```    
- Intuición: convierte un vector de puntuaciones en una distribución de probabilidad.
- Uso típico: capa de salida en clasificación multiclase.
# 6. ELU — Exponential Linear Unit
Nombre: nn.ELU(alpha=1.0)

Fórmula:
```
f(x)={xα(ex−1)​si x>0si x≤0​
```    
- Intuición: suaviza la transición negativa y mantiene gradiente.
- Uso típico: redes profundas donde ReLU genera mucha activación cero.
# 7. GELU — Gaussian Error Linear Unit
Nombre: nn.GELU()

Fórmula (aproximada):
```
f(x)=0.5x(1+tanh(2/π
​(x+0.044715x3)))
```    
- Intuición: activa parcialmente los valores según una distribución gaussiana.
- Uso típico: modelos modernos como BERT y Transformers.
# 8. SELU — Scaled Exponential Linear Unit
Nombre: nn.SELU()

- Intuición: variante autoescalada de ELU que mantiene normalización interna (Self-Normalizing Networks).
- Uso típico: redes totalmente conectadas profundas sin BatchNorm.
# 9. Softplus
Nombre: nn.Softplus()

Fórmula:
```
f(x)=ln(1+ex)
```    
- Intuición: versión suavizada de ReLU.
- Ventaja: derivable en todos los puntos.
- Uso típico: cuando se necesita continuidad (por ejemplo, VAEs).
# 10. Swish
No está directamente en torch.nn, pero puede implementarse como:
```
f(x)=x⋅sigmoid(x)
```    
Uso típico: arquitecturas modernas (EfficientNet).
```python
import torch
import torch.nn.functional as F
def swish(x):
    return x * F.sigmoid(x)
```

# Resumen general:

| Activación     | Rango salida    | Uso común                | Comentario             |
| -------------- | --------------- | ------------------------ | ---------------------- |
| **ReLU**       | [0, ∞)          | CNN, MLP                 | Rápida y efectiva      |
| **Leaky ReLU** | (-∞, ∞)         | CNN                      | Evita neuronas muertas |
| **Sigmoid**    | (0, 1)          | Clasificación binaria    | Saturación             |
| **Tanh**       | (-1, 1)         | RNN                      | Centrada en 0          |
| **Softmax**    | (0, 1) (suma=1) | Clasificación multiclase | Normaliza salida       |
| **ELU**        | (-α, ∞)         | Redes profundas          | Gradientes suaves      |
| **GELU**       | (-∞, ∞)         | Transformers             | Activación moderna     |
| **SELU**       | (-∞, ∞)         | MLP                      | Auto-normalización     |
| **Softplus**   | (0, ∞)          | Modelos continuos        | Suave ReLU             |
| **Swish**      | (-∞, ∞)         | EfficientNet             | Similar a GELU         |
