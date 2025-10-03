[Presentación](https://gamma.app/docs/Etiquetado-de-Datos-en-Machine-Learning-1es46fy2bdog4fx?mode=doc)
# Tarea 1: Etiquetado de Datos

## ¿Qué es el Etiquetado de Datos?

El **etiquetado de datos** es el proceso de identificar y marcar (etiquetar) datos crudos (como imágenes, textos o sonidos) para que un modelo de machine learning pueda aprender de ellos. Es un paso fundamental en el **aprendizaje supervisado**, donde el modelo aprende a partir de ejemplos que ya tienen la "respuesta correcta".

En resumen, si los datos son la materia prima, las etiquetas son las instrucciones que le dicen al modelo qué patrones debe buscar.

## ¿Por Qué es Importante?

Un modelo de machine learning es como un estudiante: aprende de los ejemplos que se le proporcionan. Si los ejemplos están mal etiquetados, el modelo aprenderá patrones incorrectos y no podrá hacer predicciones precisas.

- **Calidad sobre cantidad:** Un conjunto de datos más pequeño pero bien etiquetado es a menudo más valioso que uno masivo con etiquetas de mala calidad.
- **Base del aprendizaje:** Sin etiquetas, un modelo de aprendizaje supervisado no tiene forma de saber si sus predicciones son correctas o incorrectas durante el entrenamiento.

## Tipos de Etiquetado (Ejemplos)

El tipo de etiqueta depende del problema que se quiera resolver:

1.  **Clasificación:** Asignar una categoría a un dato.
    - **Ejemplo:** Etiquetar correos electrónicos como `spam` o `no spam`.
    - **Ejemplo:** En una imagen, determinar si contiene un `perro` o un `gato`.

2.  **Regresión:** Asignar un valor numérico continuo.
    - **Ejemplo:** Etiquetar una foto de una casa con su `precio de venta`.
    - **Ejemplo:** Etiquetar datos de tráfico con el `tiempo de viaje`.

3.  **Detección de Objetos:** Dibujar un cuadro delimitador (bounding box) alrededor de objetos en una imagen y asignarles una etiqueta.
    - **Ejemplo:** En una foto de una calle, dibujar cuadros alrededor de cada `coche`, `peatón` y `semáforo`.

4.  **Segmentación Semántica:** Asignar una etiqueta a cada píxel de una imagen.
    - **Ejemplo:** En una imagen satelital, etiquetar todos los píxeles que corresponden a `agua`, `vegetación` o `edificios`.

## Técnicas de Etiquetado

- **Manual:** Realizado por personas (anotadores humanos). Es el método más preciso pero también el más lento y costoso.
- **Semiautomático:** Un modelo pre-entrenado sugiere etiquetas, y los humanos las corrigen. Acelera el proceso.
- **Automático:** Un modelo existente etiqueta los nuevos datos. Es rápido pero puede propagar errores si el modelo no es muy preciso.

## Ejemplo Práctico: One-Hot Encoding

Una vez que tenemos etiquetas categóricas (como `"Hombre"` o `"Mujer"`), necesitamos convertirlas a un formato numérico que el modelo entienda. Una técnica común es el **One-Hot Encoding**.

Consiste en crear nuevas columnas binarias (0 o 1) para cada categoría.

**Datos Originales:**

| Sex    |
|--------|
| male   |
| female |
| female |

**Después de One-Hot Encoding:**

| Sex_male | Sex_female |
|----------|------------|
| 1        | 0          |
| 0        | 1          |
| 0        | 1          |

Este formato numérico es directamente utilizable por los algoritmos de machine learning.
