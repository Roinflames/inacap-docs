# 🧠 Buenas prácticas de desarrollo de software

## 🧱 Principios SOLID

Los principios **SOLID** ayudan a diseñar software mantenible, escalable y fácil de probar.

- **S** - *Single Responsibility Principle* (Responsabilidad Única):  
  Una clase debe tener una sola razón para cambiar.

- **O** - *Open/Closed Principle* (Abierto/Cerrado):  
  El código debe estar abierto a la extensión, pero cerrado a la modificación.

- **L** - *Liskov Substitution Principle*:  
  Las clases derivadas deben poder sustituir a sus clases base sin alterar el comportamiento del programa.

- **I** - *Interface Segregation Principle*:  
  Prefiere muchas interfaces específicas en lugar de una sola interfaz general.

- **D** - *Dependency Inversion Principle*:  
  Depende de abstracciones, no de implementaciones concretas.

## > 💡 Ejemplo para los estudiantes: 
    Separar el módulo de login en clases como `Autenticador`, `ValidadorEmail`, y `RepositorioUsuarios`.

---