# ¿Qué es la cardinalidad?
La cardinalidad describe la cantidad de ocurrencias que pueden existir en una relación entre dos entidades en un modelo de datos.

En otras palabras, indica cuántas instancias de una entidad pueden estar asociadas con instancias de otra entidad.

# Tipos comunes de cardinalidad:
Uno a uno (1:1)
Cada instancia de una entidad se relaciona con exactamente una instancia de otra entidad.
Ejemplo: Una persona tiene un pasaporte único.

Uno a muchos (1:N)
Una instancia de la primera entidad puede estar relacionada con muchas instancias de la segunda entidad, pero cada instancia de la segunda entidad solo con una de la primera.
Ejemplo: Un profesor puede impartir muchas clases, pero cada clase tiene un solo profesor.

Muchos a muchos (M:N)
Muchas instancias de la primera entidad pueden estar relacionadas con muchas instancias de la segunda entidad.
Ejemplo: Un estudiante puede estar inscrito en varios cursos, y un curso puede tener varios estudiantes.

# Cómo se representa en diagramas ER
En la notación de Chen, a veces se usa texto o símbolos junto a las líneas de relación.

En la notación de Barker o UML, se especifican rangos como (0..1), (1), (0..N), etc., al lado de la conexión entre entidades.