# Metodología CRISP-DM: Guía para Proyectos de Machine Learning

**CRISP-DM** (Cross-Industry Standard Process for Data Mining) es un ciclo de vida estándar y probado para estructurar proyectos de machine learning y ciencia de datos. Proporciona un marco de trabajo que ayuda a planificar, ejecutar y entregar proyectos de manera eficiente y con un enfoque en los objetivos del negocio.

El proceso es **iterativo** y consta de 6 fases principales.

---

## Las 6 Fases de CRISP-DM

![Ciclo CRISP-DM](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/CRISP-DM_Process_Diagram.png/1200px-CRISP-DM_Process_Diagram.png)

### 1. Comprensión del Negocio (Business Understanding)

**Objetivo:** Entender qué quiere lograr el negocio. Es la fase más importante, ya que un modelo técnicamente perfecto es inútil si no resuelve el problema correcto.

- **Tareas Clave:**
  - **Definir el objetivo de negocio:** ¿Qué se quiere mejorar? (Ej: reducir la pérdida de clientes, aumentar las ventas, predecir fallos en maquinaria).
  - **Evaluar la situación actual:** ¿Cómo se hace esto ahora? ¿Qué recursos hay disponibles?
  - **Definir los criterios de éxito:** ¿Cómo mediremos si el proyecto es un éxito? (Ej: lograr una precisión del 80%, reducir los costos en un 15%).
  - **Traducir el objetivo de negocio a un problema de machine learning:** (Ej: "reducir la pérdida de clientes" se convierte en "predecir qué clientes tienen alta probabilidad de abandonar el servicio").

**Ejemplo (Titanic):**
- **Objetivo de Negocio:** Entender los factores que influyeron en la supervivencia de los pasajeros para un análisis histórico.
- **Problema de ML:** Construir un modelo que prediga si un pasajero sobrevivió (`Survived`) basándose en sus características (edad, clase, sexo, etc.).
- **Criterio de Éxito:** Lograr una precisión predictiva superior al 75%.

### 2. Comprensión de los Datos (Data Understanding)

**Objetivo:** Familiarizarse con los datos disponibles y evaluar su calidad.

- **Tareas Clave:**
  - **Recopilar datos iniciales:** Obtener acceso a las fuentes de datos.
  - **Describir los datos:** ¿Cuántas filas y columnas hay? ¿Qué significa cada columna?
  - **Explorar los datos (Análisis Exploratorio - EDA):** Calcular estadísticas básicas (promedios, medianas), crear visualizaciones (histogramas, gráficos de barras) para encontrar patrones o anomalías.
  - **Verificar la calidad de los datos:** ¿Hay valores faltantes (NaN)? ¿Hay datos erróneos o inconsistentes?

**Ejemplo (Titanic):**
- **Recopilación:** Cargar el archivo `train.csv`.
- **Descripción:** El dataset tiene 891 filas y 12 columnas como `Age`, `Sex`, `Pclass`, etc.
- **Exploración:** Descubrir que la mayoría de los pasajeros de primera clase sobrevivieron, mientras que la mayoría de los de tercera clase no. Visualizar la distribución de edades.
- **Calidad:** Identificar que la columna `Age` tiene muchos valores faltantes, y `Cabin` tiene aún más.

### 3. Preparación de los Datos (Data Preparation)

**Objetivo:** Transformar los datos crudos en un formato limpio y adecuado para el modelado. Esta fase suele consumir la mayor parte del tiempo del proyecto (hasta un 80%).

- **Tareas Clave:**
  - **Limpieza de datos:** Manejar valores faltantes (imputarlos con la media/mediana o eliminar la fila/columna).
  - **Ingeniería de características (Feature Engineering):** Crear nuevas variables a partir de las existentes (Ej: crear una variable `TamañoFamilia` sumando `SibSp` y `Parch`).
  - **Transformación de datos:** Convertir variables categóricas a numéricas (usando **One-Hot Encoding** o **Label Encoding**).
  - **Formateo:** Asegurarse de que todos los datos estén en el formato correcto.

**Ejemplo (Titanic):**
- **Limpieza:** Rellenar los valores faltantes de `Age` con la mediana de edad.
- **Ingeniería de Características:** No se crean nuevas en este caso simple, pero se seleccionan las más relevantes (`Pclass`, `Sex`, `Age`).
- **Transformación:** Convertir la columna `Sex` (`male`/`female`) a `0`/`1`.

### 4. Modelado (Modeling)

**Objetivo:** Seleccionar, entrenar y ajustar algoritmos de machine learning para encontrar el que mejor funcione.

- **Tareas Clave:**
  - **Seleccionar el algoritmo:** Elegir uno o varios modelos apropiados para el problema (Ej: Regresión Logística, Árbol de Decisión, Random Forest para clasificación).
  - **Diseñar un plan de prueba:** Definir cómo se evaluará el modelo (Ej: usando **validación cruzada**).
  - **Entrenar el modelo:** Alimentar el algoritmo con los datos preparados.
  - **Ajuste de hiperparámetros:** Modificar la configuración del modelo (Ej: la `profundidad máxima` de un árbol de decisión) para mejorar su rendimiento.

**Ejemplo (Titanic):**
- **Selección:** Probar con `LogisticRegression` y `DecisionTreeClassifier`.
- **Plan de Prueba:** Usar validación cruzada con 5 pliegues (k=5).
- **Entrenamiento:** Ejecutar `model.fit(X_train, y_train)`.
- **Ajuste:** Probar con diferentes valores de `max_depth` para el árbol de decisión para evitar el **overfitting**.

### 5. Evaluación (Evaluation)

**Objetivo:** Evaluar qué tan bien funciona el modelo y si cumple con los objetivos de negocio definidos en la primera fase.

- **Tareas Clave:**
  - **Evaluar los resultados:** Usar métricas técnicas (como `accuracy`, `precision`, `recall`) sobre el conjunto de prueba.
  - **Revisar el proceso:** ¿Se ha pasado algo por alto? ¿El modelo es justo y ético?
  - **Determinar los próximos pasos:** Decidir si el modelo está listo para ser desplegado o si necesita más trabajo (volver a fases anteriores).

**Ejemplo (Titanic):**
- **Evaluación:** El modelo de Árbol de Decisión con `max_depth=4` logra una precisión promedio de ~81% en la validación cruzada, superando el criterio de éxito del 75%.
- **Revisión:** El modelo parece tener sentido y no muestra sesgos obvios.
- **Próximos Pasos:** El modelo se considera aceptable para el análisis histórico.

### 6. Despliegue (Deployment)

**Objetivo:** Poner el modelo en producción para que pueda ser utilizado por el negocio y generar valor.

- **Tareas Clave:**
  - **Planificar el despliegue:** ¿Cómo se integrará el modelo en los sistemas existentes? (Ej: como una API, en una app, en un dashboard).
  - **Monitorear y mantener:** Vigilar el rendimiento del modelo a lo largo del tiempo y re-entrenarlo cuando sea necesario para que no quede obsoleto.
  - **Generar un reporte final:** Documentar el proyecto y sus resultados.

**Ejemplo (Titanic):**
- **Despliegue:** Como es un análisis histórico, el "despliegue" podría ser un informe final o un dashboard interactivo que muestre las predicciones y los factores de supervivencia más importantes. No se requiere una aplicación en tiempo real.
- **Monitoreo:** No aplica en este caso, ya que los datos son históricos y no cambiarán.
