# Sistemas de información asociados al enfoque de base de datos
# 2 Conceptos clave a manejar

## - Tipos de sistemas de información

• Sistemas operacionales o TPS (Transaction Processing Systems).
• Sistemas administrativos o MIS (Management Information Systems).
• Sistemas de apoyo a la toma de decisiones o DSS (Decision Support System).

| Característica                   | TPS (Transaction Processing Systems)      | MIS (Management Information Systems)                        | DSS (Decision Support Systems)                              |
| -------------------------------- | ----------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
|(*) **Propósito principal**          | Procesar transacciones diarias rutinarias | Proporcionar informes y apoyo para decisiones estructuradas | Apoyar decisiones semiestructuradas o no estructuradas      |
| **Usuarios principales**         | Personal operativo                        | Gerentes de nivel medio                                     | Alta gerencia, analistas, tomadores de decisiones           |
| **Tipo de decisiones**           | Operativas y repetitivas                  | Tácticas, basadas en información consolidada                | Estratégicas, basadas en análisis y simulaciones            |
| **Frecuencia de uso**            | Diariamente y en tiempo real              | Periódica (diaria, semanal, mensual)                        | Según necesidad (ad hoc)                                    |
|(*) **Ejemplos de funciones**        | Registro de ventas, pagos, inventario     | Informes de rendimiento, análisis de costos                 | Proyecciones financieras, análisis de escenarios            |
| **Tipo de información manejada** | Transaccional, detallada                  | Agregada, resumida                                          | Analítica, modelada y proyectada                            |
| **Nivel organizacional**         | Nivel operativo                           | Nivel medio                                                 | Nivel estratégico                                           |
| **Interacción del usuario**      | Baja, estandarizada                       | Moderada, consultas e informes                              | Alta, con herramientas interactivas y modelos de simulación |
|(*) **Ejemplos de sistemas**         | Punto de venta (POS), sistemas contables  | Sistemas de informes gerenciales, dashboards                | Sistemas de apoyo a decisiones financieras o logísticas     |

## - Data Warehouse (Almacén de Datos)
Es una **base de datos** centralizada diseñada para almacenar grandes cantidades de información histórica y consolidada, proveniente de diferentes fuentes. Su objetivo es facilitar el análisis y la toma de decisiones.

- centralizada: reúne todos los datos importantes de una organización en un solo lugar, facilitando el acceso, la gestión y el análisis.
Toda la información, sin importar de qué área provenga (ventas, finanzas, recursos humanos), se almacena en un sistema común. Esto evita tener datos dispersos en diferentes sistemas o formatos.

- histórica: permite analizar cómo han cambiado los datos a lo largo del tiempo, lo cual es clave para detectar tendencias, patrones y realizar proyecciones.
Los datos no se borran ni se reemplazan, sino que se acumulan con el tiempo. Esto crea un registro completo del pasado.

- consolidada: garantiza que los datos sean consistentes y estén integrados correctamente, eliminando duplicaciones y errores.
La información de diferentes áreas o sistemas es combinada y limpiada para formar una "versión única de la verdad".

- diferentes fuentes: una organización genera datos desde múltiples sistemas (ERP, CRM, hojas de cálculo, etc.) y todos son valiosos para el análisis.
El Data Warehouse puede recibir datos de múltiples aplicaciones, plataformas y bases de datos, sin importar su formato o procedencia.

Ejemplo:
Una empresa de supermercados utiliza un data warehouse para guardar información de ventas de todas sus sucursales, permitiendo analizar tendencias de consumo por temporada o región.

## - Minería de datos (Data Mining)
Es el **proceso** de analizar grandes volúmenes de datos para descubrir patrones, correlaciones o tendencias ocultas que no son evidentes a simple vista.

- patrones: Son formas repetitivas o estructuras comunes que se detectan en los datos.
Un cliente siempre compra productos de limpieza los fines de semana.
- correlaciones: Relaciones entre dos o más variables, donde un cambio en una influye en la otra.
Cuando sube la temperatura, aumentan las ventas de helados.
- tendencias: Cambios o comportamientos que se mantienen en una misma dirección a lo largo del tiempo.
Cada año, crecen las compras en línea durante el mes de diciembre.

Ejemplo:
Una plataforma de streaming analiza el historial de visualización de los usuarios para recomendar películas personalizadas, basándose en patrones de comportamiento similares.

## - Clasificación de los sistemas de información
### OLTP
**Sistemas** orientados al procesamiento de transacciones en tiempo real. Se enfocan en tareas operativas como registrar ventas, pagos, reservas, etc.

Ejemplo:
El sistema de punto de venta (POS) en un supermercado, que registra cada compra a medida que sucede.

### OLAP
**Sistemas** diseñados para el análisis multidimensional de datos. Permiten realizar consultas complejas y generar reportes estratégicos a partir de información histórica.

Ejemplo:
Un gerente de marketing usa un sistema OLAP para analizar las ventas por producto, región y trimestre, con el fin de decidir dónde enfocar la próxima campaña publicitaria.