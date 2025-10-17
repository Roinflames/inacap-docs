# Ejemplo de Red Neuronal Convolucional (CNN) con TensorFlow y Keras
# Este ejemplo muestra cómo construir y entrenar una CNN para clasificar imágenes del conjunto de datos CIFAR-10.

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 1. Cargar y preprocesar el conjunto de datos CIFAR-10
# CIFAR-10 contiene 60,000 imágenes en color de 32x32 en 10 clases, con 6,000 imágenes por clase.
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

# Normalizar los valores de los píxeles a un rango entre 0 y 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# 2. Construir el modelo de la CNN
# El modelo es una pila de capas Conv2D y MaxPooling2D, seguidas de capas densas (fully connected).
model = models.Sequential()
# Capa convolucional con 32 filtros de 3x3, función de activación ReLU
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# Capa de max-pooling para reducir la dimensionalidad
model.add(layers.MaxPooling2D((2, 2)))
# Otra capa convolucional y de max-pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
# Y una más
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Aplanar la salida de las capas convolucionales para pasarla a las capas densas
model.add(layers.Flatten())
# Capa densa con 64 neuronas
model.add(layers.Dense(64, activation='relu'))
# Capa de salida con 10 neuronas (una para cada clase) y activación softmax
model.add(layers.Dense(10))

# Imprimir un resumen del modelo
model.summary()

# 3. Compilar y entrenar el modelo
# Se utiliza el optimizador Adam, la función de pérdida SparseCategoricalCrossentropy (adecuada para clasificación multiclase con etiquetas enteras)
# y se monitorea la precisión.
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo durante 10 épocas
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# 4. Evaluar el modelo
# Se evalúa el rendimiento del modelo con el conjunto de datos de prueba.
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(f"\nPrecisión en el conjunto de prueba: {test_acc}")

# 5. Visualizar los resultados del entrenamiento
# Se grafica la precisión y la pérdida a lo largo de las épocas.
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()
