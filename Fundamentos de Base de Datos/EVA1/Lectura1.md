# Enfoque tradicional de procesamiento de datos y enfoque de base de datos
# 1 Conceptos clave a manejar

- Procesamiento de datos => necesidad de las empresas; almacenar información.
- Enfoques: tradicional, base de datos

| Característica                  | Enfoque Tradicional                            | Enfoque con Base de Datos                          |
| ------------------------------- | ---------------------------------------------- | -------------------------------------------------- |
| **Almacenamiento de datos**     | Archivos físicos o planos (textos, hojas)      | Sistema de gestión de bases de datos (SGBD)        |
| **Redundancia de datos**        | Alta (datos duplicados en varios archivos)     | Baja (datos centralizados y normalizados)          |
| **Integridad de datos**         | Difícil de mantener                            | Más fácil de asegurar con reglas y restricciones   |
| **Acceso a la información**     | Manual y lento                                 | Rápido y eficiente mediante consultas              |
| **Seguridad de la información** | Limitada (acceso físico)                       | Alta (control de usuarios, permisos, encriptación) |
| **Escalabilidad**               | Limitada                                       | Alta (fácil de expandir)                           |
| **Mantenimiento de datos**      | Costoso y propenso a errores                   | Automatizado y más confiable                       |
| **Relaciones entre datos**      | Difíciles de gestionar                         | Uso de claves y relaciones bien definidas          |
| **Actualización de datos**      | Manual, requiere cambios en múltiples archivos | Centralizada y automática                          |
| **Costo inicial**               | Bajo (en papel o con herramientas básicas)     | Mayor (software, hardware, capacitación)           |
| **Ejemplos**                    | Hojas de cálculo, archivos de texto            | MySQL, Oracle, PostgreSQL, Microsoft SQL Server    |