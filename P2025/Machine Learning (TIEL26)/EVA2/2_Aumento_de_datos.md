# Tarea 2: Aumento de Datos (Data Augmentation)

## ¿Qué es el Aumento de Datos?

El **aumento de datos** es una técnica que consiste en generar nuevas muestras de datos a partir de las existentes, aplicando transformaciones leves pero realistas. El objetivo es incrementar artificialmente el tamaño y la diversidad del conjunto de entrenamiento sin necesidad de recopilar nuevos datos.

Es una de las estrategias más efectivas y económicas para mejorar el rendimiento y la robustez de un modelo.

## ¿Por Qué es Importante?

1.  **Previene el Overfitting:** Al exponer al modelo a una mayor variedad de versiones de los mismos datos, se reduce el riesgo de que "memorice" las muestras de entrenamiento. El modelo se ve forzado a aprender patrones más generales y robustos.

2.  **Aumenta el Tamaño del Dataset:** Es especialmente útil cuando se dispone de pocos datos, una situación común en muchos proyectos de machine learning. Un dataset más grande y variado generalmente conduce a un mejor modelo.

3.  **Mejora la Generalización:** Un modelo entrenado con datos aumentados es más capaz de generalizar y funcionar bien con datos nuevos y no vistos, ya que ha sido expuesto a diferentes perspectivas, iluminaciones, orientaciones, etc.

## Técnicas Comunes de Aumento de Datos

Las técnicas varían según el tipo de dato.

### Para Imágenes:

Es el campo donde el aumento de datos es más popular. Las transformaciones comunes incluyen:

- **Rotación:** Girar la imagen en un ángulo determinado.
- **Traslación (Shift):** Mover la imagen horizontal o verticalmente.
- **Zoom:** Acercar o alejar una parte de la imagen.
- **Volteo (Flip):** Invertir la imagen horizontal o verticalmente (el volteo vertical no es adecuado para todos los casos, como en el reconocimiento de texto).
- **Cambios de Brillo y Contraste:** Simular diferentes condiciones de iluminación.
- **Añadir Ruido:** Introducir ruido gaussiano para hacer el modelo más robusto a imperfecciones.

**Ejemplo Visual:**

A partir de una única imagen de un perro, podemos generar múltiples variantes:

*Imagen Original* → *Rotada 15°* → *Con Zoom* → *Volteada Horizontalmente*

![Ejemplo de Aumento de Datos](https://i.imgur.com/T8fXf3p.png) *(Referencia del notebook `ejemplo_aumento_datos.ipynb`)*

### Para Texto:

El aumento de datos en texto es más complejo, ya que las transformaciones deben preservar el significado de la oración.

- **Reemplazo de Sinónimos:** Cambiar palabras por sus sinónimos (ej. `"bonito"` por `"hermoso"`).
- **Back-Translation (Retrotraducción):** Traducir el texto a otro idioma y luego de vuelta al original. A menudo introduce variaciones interesantes en la redacción.
    - `"Es un buen libro"` → (Alemán) `"Es ist ein gutes Buch"` → `"Es un libro bueno"`.
- **Inserción o Eliminación Aleatoria:** Añadir o quitar palabras que no cambian el sentido general de la frase.

## Conclusión

El aumento de datos es una herramienta poderosa y esencial en el arsenal de un ingeniero de machine learning. Permite construir modelos más precisos y robustos, especialmente cuando los datos son escasos. Es una forma inteligente de sacar el máximo provecho de un conjunto de datos limitado.
