## 📖 Clean Code

Basado en el libro de Robert C. Martin. Código limpio es:

- Legible
- Nombrado con sentido
- Sin duplicaciones innecesarias
- Con funciones pequeñas y enfocadas
- Bien estructurado y con comentarios solo donde realmente se necesitan

> 💡 Ejemplo para los estudiantes:  
> En vez de:
> ```js
> function p(u, p) { if (u === "admin" && p === "1234") return true; }
> ```
> Usa:
> ```js
> function esUsuarioValido(usuario, clave) {
>     return usuario === "admin" && clave === "1234";
> }
> ```