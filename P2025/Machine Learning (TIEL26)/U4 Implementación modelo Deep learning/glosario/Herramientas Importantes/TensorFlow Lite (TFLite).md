# TensorFlow Lite (TFLite)

**TensorFlow Lite (TFLite)** es un conjunto de herramientas de código abierto de Google, diseñado específicamente para **desplegar y ejecutar modelos de Machine Learning en dispositivos de borde (edge devices)**. Es una pieza fundamental del ecosistema de TensorFlow para llevar la IA a aplicaciones móviles, sistemas embebidos y dispositivos IoT.

El flujo de trabajo no es entrenar modelos en TFLite, sino **convertir** modelos ya entrenados con TensorFlow a un formato optimizado para la inferencia en el borde.

---

## ¿Para Qué Sirve TFLite?

El objetivo principal de TFLite es permitir que los modelos de ML se ejecuten de manera eficiente en dispositivos con recursos limitados, como:

- **Smartphones** (Android y iOS)
- **Microcontroladores** (Arduino, ESP32, etc.)
- **Computadoras de placa única** (Raspberry Pi, Coral Dev Board)
- **Dispositivos IoT** y otros sistemas embebidos.

Esto se logra a través de un proceso de **conversión y optimización** que hace que los modelos sean:

- **Más Pequeños:** Reduce significativamente el tamaño del archivo del modelo, facilitando su almacenamiento en dispositivos con memoria limitada.
- **Más Rápidos:** Disminuye la latencia de la inferencia (el tiempo que tarda en hacer una predicción).
- **Menos Exigentes en Energía:** Reduce el consumo de batería, algo crucial para dispositivos móviles y autónomos.

---

## El Flujo de Trabajo de TensorFlow Lite

El proceso consta de tres pasos principales:

### 1. Conversión del Modelo

Se toma un modelo estándar de TensorFlow (guardado en formato `SavedModel` o un modelo de Keras) y se utiliza el **Conversor de TensorFlow Lite**.

```python
import tensorflow as tf

# Cargar un modelo de Keras
model = tf.keras.applications.MobileNetV2()

# Crear un objeto conversor a partir del modelo
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Aplicar optimizaciones (ver más abajo)
# ...

# Convertir el modelo
tflite_model = converter.convert()

# Guardar el modelo convertido en un archivo .tflite
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)
```

El resultado es un archivo con extensión `.tflite`, que es un formato de buffer plano (flat-buffer) altamente eficiente.

### 2. Optimización (Opcional pero Recomendado)

Durante la conversión, TFLite puede aplicar varias técnicas de optimización para reducir aún más el tamaño y la latencia del modelo. La más común es la **cuantificación**.

- **Cuantificación Post-Entrenamiento:** Es la técnica más sencilla. Convierte los pesos del modelo de punto flotante de 32 bits (float32) a enteros de 8 bits (int8). Esto puede reducir el tamaño del modelo en **4 veces** y acelerar la inferencia en **2-3 veces** en hardware compatible, con una pérdida mínima de precisión.

```python
# Dentro del flujo de conversión
converter.optimizations = [tf.lite.Optimize.DEFAULT]
```

### 3. Despliegue e Inferencia

Una vez que se tiene el archivo `.tflite`, se utiliza el **Intérprete de TensorFlow Lite** para ejecutarlo en el dispositivo de destino. El intérprete es una librería ligera y de alto rendimiento que carga el modelo y realiza las predicciones.

TFLite proporciona librerías para múltiples plataformas y lenguajes:
- **Java/Kotlin** para Android.
- **Swift/Objective-C** para iOS.
- **C++** para Linux (Raspberry Pi) y sistemas embebidos/microcontroladores.
- **Python** para facilitar las pruebas y el prototipado.

```python
# Ejemplo de inferencia en Python
import tensorflow as tf
import numpy as np

# Cargar el intérprete de TFLite
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Obtener detalles de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Preparar datos de entrada (deben tener el mismo shape y tipo)
input_data = np.array(..., dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

# Ejecutar la inferencia
interpreter.invoke()

# Obtener los resultados
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
```

En resumen, TFLite es la solución estándar del ecosistema de TensorFlow para hacer que los modelos de ML sean prácticos y eficientes para el mundo real de los dispositivos móviles y de borde.
