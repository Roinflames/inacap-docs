# 1.2. NumPy
"""
NumPy es una biblioteca fundamental para la computación científica en Python. 
Proporciona un objeto de matriz multidimensional de alto rendimiento y herramientas para trabajar con estas matrices. 
NumPy es esencial para operaciones numéricas eficientes en Python y es comúnmente utilizado junto con Pandas.
"""
"""
🧠 ¿Qué interpretamos?
La media se distorsionó por el valor 100 (posiblemente un error o intento de sabotaje).
La desviación estándar alta indica que los datos no están agrupados, hay algo raro.

🔐 Aplicación en seguridad:
Ejemplo real: Si la mayoría de los intentos de login vienen desde 3 IPs con 10 accesos, y una IP tiene 500 accesos, la desviación estándar detectará ese outlier.

✅ Tip para tus alumnos:
Si la desviación estándar es muy grande → revisen los datos. Puede haber errores, outliers o incluso ataques.
"""
import numpy as np

edades = np.array([25, 26, 27, 28, 29, 100])  # 👀 ese 100 es sospechoso
media = np.mean(edades)
desviacion = np.std(edades)

print(f"Media: {media}")
print(f"Desviación estándar: {desviacion:.2f}")
