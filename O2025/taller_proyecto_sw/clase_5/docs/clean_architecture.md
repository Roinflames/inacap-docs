## 🏛 Clean Architecture

También propuesta por Robert C. Martin, plantea una organización del sistema en **capas independientes**, donde:

- Las **entidades** (reglas de negocio) están en el centro.
- Los **casos de uso** (aplicación) rodean a las entidades.
- La **interfaz del usuario**, **web**, **DB**, etc., están en el exterior.
- **Las dependencias siempre apuntan hacia el centro.**

> 💡 Ejemplo para los estudiantes:  
    > Separar lógica de agendamiento (`CasoUsoAgendarHora`) de la interfaz (`FormularioAgendar.vue`) y de la base de datos (`RepositorioHorasMongo`).