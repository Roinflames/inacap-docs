# 1. Modelos de Bases de Datos (Database Models)
Un modelo de base de datos define cómo se estructuran, almacenan y relacionan los datos. En la industria TI, se utilizan distintos modelos según las necesidades de rendimiento, escalabilidad y complejidad del sistema.

## Elementos Comunes de los Modelos de Datos:
Entidades: Representan objetos o conceptos del mundo real (ej. cliente, producto).
Atributos: Características de cada entidad (ej. nombre, precio).
Relaciones: Vínculos entre entidades (ej. un cliente compra productos).
Restricciones: Reglas que aseguran la integridad de los datos (ej. una venta debe tener un cliente asociado).

## 🛠️ Tipos de Modelos Usados en TI:

| Modelo                 | Características clave                                             | Uso típico en la industria                |
| ---------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| **Relacional**         | Datos organizados en tablas. Usa SQL para consultas.              | ERPs, CRMs, backends de sitios web        |
| **Documental (NoSQL)** | Almacena datos en formato tipo JSON o BSON. Flexible y escalable. | Aplicaciones web modernas, microservicios |
| **Clave-Valor**        | Datos almacenados como pares clave-valor. Ultra rápido.           | Cachés, sesiones, IoT                     |
| **Columnares**         | Datos almacenados por columnas, optimizado para lectura masiva.   | Big data, analítica avanzada              |
| **Grafos**             | Representa entidades como nodos y relaciones como aristas.        | Redes sociales, motores de recomendación  |


# 💾 2. Sistemas de Gestión de Bases de Datos (DBMS)
Un DBMS es el software que permite crear, manipular, consultar y administrar bases de datos.

## 🔧 Componentes de un DBMS:
Motor de almacenamiento: Administra cómo se guardan físicamente los datos.
Lenguaje de consulta: Permite interactuar con la base de datos (ej. SQL, Cypher).
Mecanismos de seguridad: Control de accesos, roles y permisos.
Transacciones: Garantizan operaciones completas y seguras (ACID).
Gestión de respaldo y recuperación: Protección frente a pérdidas o fallos.

## 💼 Ejemplos populares en la industria:

| DBMS                    | Tipo                   | Usos típicos                          |
| ----------------------- | ---------------------- | ------------------------------------- |
| **MySQL / PostgreSQL**  | Relacional             | Aplicaciones web, plataformas SaaS    |
| **Oracle**              | Relacional corporativo | Bancos, telecomunicaciones, gobiernos |
| **MongoDB**             | Documental (NoSQL)     | Apps móviles, gestión de usuarios     |
| **Redis**               | Clave-valor            | Caché, ranking en tiempo real         |
| **Neo4j**               | Grafos                 | Recomendaciones, detección de fraude  |
| **BigQuery / Redshift** | Columnares             | Data warehouses, BI, análisis masivo  |

