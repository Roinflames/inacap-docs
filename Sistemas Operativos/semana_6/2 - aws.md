# 🔹 Sesión 1 – Semana 7: Licenciamiento de Software (Acumulativa 7)
Objetivo: Comprender los tipos de licencias de software con foco en software libre, licencias open source, y su relación con el uso de Linux.

## 1. Introducción (6:30 – 7:00)
- Presentación de la clase y objetivos.
- Breve historia del software libre.

El movimiento del software libre, liderado por Richard Stallman, surgió como una reacción contra las restricciones impuestas por el software propietario.

El objetivo era devolver a los usuarios la libertad de usar, estudiar, modificar y distribuir el software. 

La iniciativa GNU, con proyectos como GCC y Bash, fue fundamental en este movimiento, proporcionando herramientas esenciales para construir sistemas operativos libres.

En 1991, Linus Torvalds creó el núcleo Linux, inicialmente con una licencia restrictiva, pero luego adoptó la licencia GNU General Public License (GPL), convirtiéndose en software libre. 

La combinación de GNU y Linux dio origen al sistema operativo GNU/Linux, también conocido como Linux, que es la base de numerosas distribuciones (distros). 

- Pregunta detonadora: ¿Por qué Linux es gratuito? ¿Qué implica eso?

Gratuito en Costo:
Linux es gratuito en el sentido de que no requiere el pago de una licencia para su uso, distribución o modificación. 

Código Abierto:
La gratuidad de Linux se debe a su naturaleza de código abierto. Esto significa que su código fuente está disponible para que cualquiera pueda acceder a él, estudiarlo, modificarlo y redistribuirlo bajo los términos de la licencia GPL. 
Implicaciones:

Libertad del Usuario: 
La gratuidad de Linux se traduce en la libertad para los usuarios de usar el sistema operativo sin restricciones, adaptarlo a sus necesidades, y contribuir a su mejora. 

Comunidad Activa: 
La naturaleza de código abierto de Linux fomenta una comunidad activa de desarrolladores y usuarios que colaboran en su desarrollo y soporte. 

Flexibilidad y Personalización: 
La posibilidad de modificar el código permite crear diferentes distribuciones (distros) de Linux, cada una con sus propias características y propósitos, ofreciendo una amplia gama de opciones para los usuarios. 

Alternativa a Sistemas Propietarios: 
Linux representa una alternativa a los sistemas operativos propietarios como Windows y macOS, ofreciendo una opción gratuita y con mayor control para los usuarios. 

Impacto en la Educación: 
El software libre, incluido Linux, ha tenido un impacto significativo en la educación, permitiendo a las instituciones educativas acceder a herramientas informáticas sin costo y fomentando la cultura del conocimiento compartido. 

Impacto Social: 
El software libre, en general, promueve una cultura de colaboración, transparencia y acceso al conocimiento, lo que tiene un impacto positivo en la sociedad. 

## 2. Teoría del licenciamiento (7:00 – 8:00)
Tipos de licencias:
- Propietarias
Estas licencias otorgan derechos limitados al usuario, generalmente restringiendo la modificación, distribución y uso del software. El código fuente no se comparte y el usuario paga por el derecho a usar el software bajo términos específicos. Ejemplos incluyen licencias de usuario único, licencias por volumen, y licencias OEM (preinstalada en hardware, no transferible)

- Software libre (GPL, LGPL)
GPL (GNU General Public License): Es una licencia copyleft, lo que significa que cualquier software derivado debe ser liberado con la misma licencia GPL, permitiendo su uso, modificación y distribución libremente. La GPL busca garantizar la libertad del software y evitar que se restrinja su uso en el futuro. 

LGPL (GNU Lesser General Public License): Similar a la GPL, pero permite enlazar bibliotecas con software propietario sin obligar a que este último también sea de código abierto bajo la LGPL. Esto la hace más flexible para su uso en proyectos comerciales. 

- Open Source (MIT, Apache, BSD)
MIT: Una licencia permisiva que permite el uso, modificación y distribución del software, incluso en proyectos comerciales, sin requerir que el código derivado sea de código abierto. Es una de las licencias más populares debido a su flexibilidad. 

Apache: Similar a la MIT, pero con algunas diferencias en los términos de patente. La Licencia Apache 2.0, por ejemplo, incluye una cláusula de patente que protege contra demandas relacionadas con patentes. 

BSD: También una licencia permisiva, con varias versiones, que permiten un amplio rango de usos, incluyendo la incorporación en software propietario. 

- Comparación entre licencias (actividad práctica guiada con tabla comparativa).

| Característica                 | Propietaria      | GPL | LGPL             | MIT | Apache 2.0 | BSD |
| ------------------------------ | ---------------- | --- | ---------------- | --- | ---------- | --- |
| ¿Es libre?                     | ❌                | ✅   | ✅                | ✅   | ✅          | ✅   |
| ¿Permite modificar?            | ❌                | ✅   | ✅                | ✅   | ✅          | ✅   |
| ¿Permite redistribución?       | ❌                | ✅   | ✅                | ✅   | ✅          | ✅   |
| ¿Obliga a liberar cambios?     | ❌                | ✅   | Solo bibliotecas | ❌   | ❌          | ❌   |
| ¿Apta para uso comercial?      | Bajo condiciones | ✅   | ✅                | ✅   | ✅          | ✅   |
| ¿Incluye cláusula de patentes? | ❌                | ❌   | ❌                | ❌   | ✅          | ❌   |

- Rol de las licencias en entornos corporativos.
Consideraciones clave:
- Cumplimiento legal: El uso incorrecto puede derivar en sanciones legales o auditorías de cumplimiento (ej. BSA).
- Presupuesto: Las licencias comerciales implican costos recurrentes. Las licencias libres pueden reducir costos.
- Compatibilidad: Algunas licencias no son compatibles entre sí. Ej. GPL no es compatible con ciertas licencias cerradas.
- Soporte: El software con licencias propietarias suele incluir soporte oficial. El software libre depende de la comunidad o soporte pago.
## 3. Actividad práctica en grupo (8:00 – 8:30)
Casos reales: elegir software y analizar su licencia.
- Uso de sitios como ChooseALicense o GitHub.
## 4. Laboratorio en AWS Academy (8:30 – 9:45)
- Acceder a una instancia EC2 con Linux.
- Verificar la distribución y versión del sistema operativo.
- Consultar la licencia del software instalado (cat /etc/*release, man, etc.).
- Investigar qué herramientas GNU vienen instaladas y su tipo de licencia.
# 5. Evaluación Acumulativa 6 (9:45 – 10:15)
- Breve cuestionario en línea.
# 6. Cierre (10:15 – 10:30)
- Revisión de aprendizajes clave.
- Introducción a la siguiente clase: gestión de archivos y directorios en Linux.