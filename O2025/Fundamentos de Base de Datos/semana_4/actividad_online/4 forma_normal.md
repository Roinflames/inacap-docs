3FN significa Tercera Forma Normal, una etapa del proceso de normalización de bases de datos. La normalización es una técnica para diseñar tablas de manera que se eviten redundancias y se mejore la integridad de los datos.

# ¿Qué es la 3FN (Tercera Forma Normal)?

Una tabla está en Tercera Forma Normal si:

Está en Segunda Forma Normal (2FN)
Es decir, no tiene dependencias parciales (los atributos no clave dependen totalmente de la clave primaria).
No hay dependencias transitivas entre atributos no clave.
Es decir, los atributos no clave deben depender únicamente de la clave primaria, y no de otros atributos no clave.

# Ejemplo para entender 3FN:
Supón esta tabla de estudiantes:

| Rut      | Nombre | Código Carrera | Nombre Carrera |
| -------- | ------ | -------------- | -------------- |
| 12345678 | Ana    | INF            | Informática    |
| 87654321 | Pedro  | ADM            | Administración |

Clave primaria: Rut

El Nombre Carrera depende del Código Carrera, que a su vez depende del Rut.

Aquí hay una dependencia transitiva:
Rut → Código Carrera → Nombre Carrera

# Solución: Dividir la tabla en dos
Estudiantes:

| Rut      | Nombre | Código Carrera |
| -------- | ------ | -------------- |
| 12345678 | Ana    | INF            |
| 87654321 | Pedro  | ADM            |

Carreras:

| Código Carrera | Nombre Carrera |
| -------------- | -------------- |
| INF            | Informática    |
| ADM            | Administración |

Con eso, el modelo está en 3FN, porque:

Todos los atributos no clave dependen directamente de la clave primaria.
No hay dependencias transitivas.