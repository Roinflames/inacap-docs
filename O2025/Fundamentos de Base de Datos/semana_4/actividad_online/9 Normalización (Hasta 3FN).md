# 4. Normalización (Hasta 3FN)
Ejemplo: Evaluacion

## Forma no normal:
Evaluacion: rut_estudiante, cod_modulo, fecha, tipo, nota, nombre_modulo

## 1FN:
Todos los atributos atómicos (ok).

## 2FN:
La clave compuesta es (rut_estudiante, cod_modulo, fecha, tipo).
nombre_modulo depende solo de cod_modulo, separamos:

Evaluacion(rut_estudiante, cod_modulo, fecha, tipo, nota)
Modulo(cod_modulo, nombre_modulo)

## 3FN:
Todos los atributos no clave dependen únicamente de la clave primaria.

