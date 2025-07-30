# 🏗 Diagrama de Arquitectura en Capas con Mermaid

```mermaid
graph TD
    subgraph Capa de Presentación
        A[Aplicación Web]
        B[App Móvil]
    end

    subgraph Capa de Lógica de Negocio
        C[API REST (Backend)]
        D[Gestor de Turnos]
        E[Gestor de Usuarios]
    end

    subgraph Capa de Persistencia
        F[(Base de Datos PostgreSQL)]
        G[(Sistema de Archivos)]
    end

    A --> C
    B --> C
    C --> D
    C --> E
    D --> F
    E --> F
    C --> G
