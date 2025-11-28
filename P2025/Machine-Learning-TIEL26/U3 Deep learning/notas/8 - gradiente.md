# Glosario: Gradiente
# ¿Qué es un gradiente?

El gradiente mide cómo cambia una función respecto a sus variables de entrada.
En aprendizaje automático, representa la dirección y magnitud del cambio que debe hacerse en los pesos del modelo para minimizar el error (función de pérdida).

En palabras simples:

El gradiente te dice cuánto y en qué dirección ajustar cada parámetro del modelo para mejorar su desempeño.

## 1. Definición matemática

Si tenemos una función 𝑓(𝑥), su gradiente es la derivada respecto a 𝑥:

dx / df​

Si la función depende de varios parámetros (x1​,x2​,x3​,…,xn​), el gradiente es un vector de derivadas parciales:

∇f(x)=(∂x1​∂f​,∂x2​∂f​,…,∂xn​∂f​)

En el contexto de redes neuronales:

f(x) = función de pérdida (error)
x sub i = pesos y sesgos del modelo
	​ 
## 2. Gradiente en PyTorch
## 3. Gradiente descendente (Gradient Descent)
## 4. Propagación hacia atrás (Backpropagation)
## 5. Explosión y desaparición de gradientes
## 6. Gradiente y requires_grad
## 7. .grad, .backward() y .detach()
## 8. Visualización intuitiva

En resumen

| Concepto                   | Significado                                                |
| -------------------------- | ---------------------------------------------------------- |
| **Gradiente**              | Derivada que indica dirección y magnitud del cambio óptimo |
| **Autograd**               | Sistema automático de cálculo de gradientes de PyTorch     |
| **Backpropagation**        | Propagación inversa del error para ajustar pesos           |
| **Gradient Descent**       | Algoritmo que usa gradientes para minimizar la pérdida     |
| **Explosión/Desaparición** | Problemas por gradientes demasiado grandes o pequeños      |

