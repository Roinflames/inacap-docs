# 🏗 Definición de Arquitectura de Software

La **arquitectura de software** es la estructura fundamental de un sistema, representada por sus **componentes**, las **relaciones entre ellos** y las **decisiones** que guían su diseño y evolución.

Incluye:

- 📦 **Componentes**: Módulos, clases, servicios, etc.
- 🔁 **Relaciones**: Cómo se comunican los componentes entre sí.
- 📐 **Decisiones arquitectónicas**: Elecciones técnicas y estratégicas, como el uso de patrones (MVC, capas, hexagonal), frameworks, bases de datos, etc.
- 🎯 **Objetivos de calidad**: Rendimiento, escalabilidad, mantenibilidad, seguridad, etc.
- **Estilos arquitectónicos**:
  - Arquitectura en capas
  - Cliente-servidor
  - Microservicios
  - Event-driven
- **Patrones comunes**:
  - MVC (Modelo-Vista-Controlador)
  - Clean Architecture
  - Hexagonal Architecture
  
> 💡 Ejemplo aplicado: En un sistema de gestión de turnos, la arquitectura define que existirá una API REST (backend), una app móvil (frontend) y una base de datos relacional (PostgreSQL), y cómo estos elementos interactúan.

---

## 🎯 Objetivos de la arquitectura

- Establecer una **visión técnica común** del sistema
- Asegurar que el software sea:
  - Mantenible
  - Escalable
  - Reutilizable
  - Seguro

---

## ¿Por qué es importante?

- Define **la base técnica** del sistema.
- Afecta directamente la **escalabilidad**, **facilidad de mantenimiento** y **costo futuro**.
- Permite **alinear al equipo** en torno a una visión técnica común.

---

## 📌 Diferencia entre arquitectura y diseño

- **Arquitectura**: visión global, alto nivel, decisiones estratégicas.
- **Diseño**: detalles de implementación, estructuras de clases, algoritmos.

---

## 🛠 Herramientas comunes para definir arquitectura

- Diagramas UML (componentes, despliegue)
- [Archimate](archimate.md)
- Diagramas C4 (Contexto, Contenedor, Componente, Código)
- Modelos en herramientas como Lucidchart, Draw.io, PlantUML o [Mermaid](arquitectura_en_capas.md)

