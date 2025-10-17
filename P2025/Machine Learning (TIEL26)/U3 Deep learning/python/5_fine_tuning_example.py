# Ejemplo de Fine-Tuning (Ajuste Fino) con TensorFlow y Keras
# Este ejemplo muestra cómo utilizar un modelo pre-entrenado (VGG16) y ajustarlo para una nueva tarea de clasificación de imágenes (CIFAR-10).

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import numpy as np

# 1. Cargar y preprocesar el conjunto de datos CIFAR-10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Convertir etiquetas a formato one-hot
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Normalizar imágenes
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# 2. Cargar el modelo base VGG16 pre-entrenado
# Se carga el modelo VGG16 entrenado en ImageNet, sin incluir las capas superiores (clasificador).
# El input_shape se ajusta al tamaño de las imágenes de CIFAR-10 (32x32x3).
# Nota: VGG16 fue entrenado en imágenes más grandes (224x224). Usar 32x32 es un compromiso para este ejemplo.
# Para mejores resultados, se debería redimensionar las imágenes a un tamaño mayor.

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

# 3. Congelar las capas del modelo base
# "Congelar" significa que sus pesos no se actualizarán durante el entrenamiento.
# Se hace esto para reutilizar las características aprendidas por el modelo base.
base_model.trainable = False

# 4. Añadir nuevas capas de clasificación
# Se crea un nuevo modelo que apila las capas congeladas de VGG16 y nuevas capas de clasificación.
model = models.Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax') # 10 clases para CIFAR-10
])

# Imprimir un resumen del modelo
model.summary()

# 5. Compilar y entrenar el modelo (primera fase)
# Se entrena solo el clasificador nuevo. El modelo base está congelado.
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=2e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=5, batch_size=128, validation_data=(x_test, y_test))

# 6. Descongelar algunas capas del modelo base para el ajuste fino
# Ahora que el clasificador está entrenado, se puede descongelar algunas de las capas superiores del modelo base
# para ajustar sus pesos a la nueva tarea.
base_model.trainable = True

# Congelar todas las capas excepto las últimas 4
for layer in base_model.layers[:-4]:
    layer.trainable = False

# 7. Compilar y entrenar el modelo (segunda fase - fine-tuning)
# Se utiliza un learning rate muy bajo para no destruir las características aprendidas.
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history_fine = model.fit(x_train, y_train, epochs=5, batch_size=128, validation_data=(x_test, y_test))

# 8. Evaluar el modelo final
results = model.evaluate(x_test, y_test, verbose=2)
print(f"\nPrecisión final en el conjunto de prueba: {results[1]}")
