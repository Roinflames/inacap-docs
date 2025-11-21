# ONNX: Interoperabilidad y Ejecución Acelerada en GPU

**ONNX** y **ONNX Runtime** son dos tecnologías clave que resuelven problemas fundamentales en el despliegue de modelos de Machine Learning: la interoperabilidad entre frameworks y la optimización del rendimiento en diferentes tipos de hardware, especialmente en GPUs.

---

## ONNX (Open Neural Network Exchange)

**ONNX** es un **formato de archivo abierto y estándar** para representar modelos de Machine Learning. Su objetivo principal es la **interoperabilidad**: permitir que un modelo entrenado en un framework (como PyTorch, TensorFlow o Keras) se pueda ejecutar en otro.

### ¿Cómo Funciona?

1.  **Entrenamiento:** Un científico de datos entrena su modelo utilizando su framework preferido (e.g., PyTorch).
2.  **Exportación:** Una vez entrenado, el modelo se exporta al formato `.onnx`. La mayoría de los frameworks modernos tienen funciones nativas para esta exportación (e.g., `torch.onnx.export`).
3.  **Representación Gráfica:** El archivo `.onnx` no guarda código de Python, sino una representación estática del grafo computacional del modelo. Define cada operación (convolución, multiplicación de matrices, etc.) y las conexiones entre ellas de una manera estandarizada.

### Ventajas de ONNX:

- **Libertad de Framework:** Desacopla el entrenamiento de la inferencia. Puedes entrenar en PyTorch y desplegar en un entorno que solo soporta TensorFlow, o viceversa.
- **Preparado para el Futuro:** Si surge un nuevo framework o hardware de inferencia, mientras soporte ONNX, tus modelos seguirán siendo compatibles.
- **Optimización:** Al tener una representación estática del grafo, es más fácil aplicar optimizaciones de alto rendimiento antes de la ejecución.

---

## ONNX Runtime: Ejecución de Alto Rendimiento

**ONNX Runtime** es un motor de inferencia de código abierto, multiplataforma y de alto rendimiento creado por Microsoft. Está diseñado específicamente para ejecutar modelos en formato ONNX de la manera más eficiente posible.

### ¿Cómo Funciona con GPUs?

ONNX Runtime utiliza **Proveedores de Ejecución (Execution Providers - EPs)** para acelerar la inferencia en hardware específico. Un EP es una capa de abstracción que permite a ONNX Runtime comunicarse con las librerías de bajo nivel del fabricante del hardware.

Para la ejecución en GPUs, los EPs más importantes son:

1.  **CUDA Execution Provider:**
    - Es el proveedor principal para GPUs **NVIDIA**.
    - Utiliza las librerías **CUDA** y **cuDNN** para ejecutar las operaciones del modelo directamente en la GPU, aprovechando su masiva capacidad de procesamiento en paralelo.
    - Para usarlo, se debe instalar el paquete `onnxruntime-gpu` y tener los drivers de NVIDIA y el toolkit de CUDA correctamente configurados.

2.  **TensorRT Execution Provider:**
    - También para GPUs **NVIDIA**, ofrece un rendimiento aún mayor.
    - **TensorRT** es un SDK de NVIDIA para la optimización de inferencia de alto rendimiento.
    - Cuando se usa este EP, ONNX Runtime delega la ejecución del grafo (o partes de él) a TensorRT. Éste aplica optimizaciones avanzadas como:
        - **Fusión de Capas:** Combina varias operaciones en una sola para reducir la sobrecarga.
        - **Cuantificación:** Utiliza tipos de datos de menor precisión (INT8, FP16) que son mucho más rápidos en el hardware de NVIDIA.
        - **Selección de Kernel:** Elige el kernel de CUDA más optimizado para cada operación y la GPU específica.

### Flujo de Trabajo para Inferencia en GPU

1.  **Exportar Modelo:** Exportar el modelo entrenado a formato `.onnx`.
2.  **Instalar ONNX Runtime para GPU:** `pip install onnxruntime-gpu`.
3.  **Crear Sesión de Inferencia:** En el código de Python, al crear la `InferenceSession` de ONNX Runtime, se especifica el proveedor de ejecución que se desea utilizar.

    ```python
    import onnxruntime as ort

    # Opciones para la sesión
    sess_options = ort.SessionOptions()

    # Crear la sesión de inferencia con el proveedor de ejecución de CUDA
    session = ort.InferenceSession(
        "mi_modelo.onnx",
        providers=['CUDAExecutionProvider']
    )

    # Ejecutar la inferencia
    # (los datos de entrada se transferirán automáticamente a la GPU)
    outputs = session.run(None, {"input_name": input_data})
    ```

4.  **Ejecución:** ONNX Runtime se encarga de mover los datos a la memoria de la GPU, ejecutar el modelo y devolver los resultados a la CPU.

En resumen, la combinación de **ONNX** para la portabilidad y **ONNX Runtime** con sus proveedores de ejecución para GPU permite desplegar modelos de Machine Learning de una manera estandarizada y con un rendimiento excepcional.
