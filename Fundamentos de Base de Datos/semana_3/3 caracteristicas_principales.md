# 1. Modelo Jerárquico
Estructura en forma de árbol.
Relación uno a muchos (1:N) entre registros.
Cada nodo (registro) tiene un solo padre y puede tener varios hijos.
Navegación mediante recorrido desde la raíz hacia las hojas.
Adecuado para datos con estructura estrictamente jerárquica.
Limitado para relaciones complejas (no permite muchos a muchos).

# 2. Modelo de Red
Estructura en forma de grafo.
Permite relaciones uno a muchos (1:N) y muchos a muchos (M:N).
Cada nodo puede tener múltiples padres y múltiples hijos.
Más flexible que el modelo jerárquico.
Navegación a través de punteros entre registros relacionados.

# 3. Modelo Relacional
Basado en tablas (relaciones).
Datos organizados en filas (tuplas) y columnas (atributos).
Soporta relaciones de tipo 1:1, 1:N y M:N.
Utiliza SQL como lenguaje estándar para manipulación de datos.
Alto nivel de independencia de datos y facilidad para consultas complejas.
Muy popular y ampliamente usado.

# 4. Modelo Orientado a Objetos
Integra conceptos de programación orientada a objetos.
Soporta entidades con atributos, métodos y herencia.
Adecuado para aplicaciones complejas con datos multimedia, gráficos, etc.
Permite encapsulación, polimorfismo y reutilización.

# 5. Modelo Documento / NoSQL
Basado en documentos estructurados (JSON, XML).
Flexible para datos semi-estructurados o no estructurados.
Escalabilidad horizontal y alta performance en grandes volúmenes de datos.
Usado en aplicaciones web, Big Data y sistemas distribuidos.