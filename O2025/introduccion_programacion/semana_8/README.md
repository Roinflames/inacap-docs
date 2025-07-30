Librerías externas y seguras<br>
Script básico con jerarquía de excepciones

🧰 Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. 
XSS attacks occur when an attacker uses a web application to send malicious code, 
generally in the form of a browser side script, to a different end user. 
Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output 
it generates without validating or encoding it.

🧰 Desviación estandar
La desviación estándar mide qué tan dispersos están los datos respecto a su media (promedio).
Es útil para detectar valores atípicos (outliers) o comportamientos sospechosos en seguridad de datos.

🧰 Instalar la extensión "SQLite" en VS Code

Abre VS Code.
Ve al panel de extensiones (ícono de cuadrados o Ctrl+Shift+X).
Busca: SQLite (autor: alexcvzz)

sqlite-viewer
https://marketplace.visualstudio.com/items/?itemName=qwtel.sqlite-viewer

🛡️ Seguridad y Buenas Prácticas con CSV
    Cuando trabajes con archivos CSV, es importante tener en cuenta algunos puntos de seguridad y buenas prácticas:
    Validación de datos: Siempre valida y limpia los datos antes de insertarlos en una base de datos o procesarlos.
        Ejemplo: Verifica que los emails tengan el formato correcto o que los IDs no sean negativos.
    Inyección de código: Aunque CSV no es un formato con inyección SQL directa, siempre asegúrate de sanitizar cualquier entrada antes de utilizarla en bases de datos.
    Manejo de caracteres especiales: Asegúrate de utilizar el parámetro encoding='utf-8' al leer y escribir archivos para evitar problemas con caracteres especiales (acentos, eñes, etc.).

