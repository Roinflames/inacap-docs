
# Ejemplo de Autoencoder con TensorFlow y Keras
# Este ejemplo muestra cómo construir y entrenar un autoencoder para eliminar el ruido de imágenes de dígitos manuscritos del conjunto de datos MNIST.

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar y preprocesar el conjunto de datos MNIST
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()

# Normalizar las imágenes a un rango de [0, 1]
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))
x_test = np.reshape(x_test, (len(x_test), 28, 28, 1))

# 2. Añadir ruido a las imágenes
# Se crea una versión ruidosa de las imágenes para entrenar el autoencoder a eliminarl el ruido.
noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)

x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)

# 3. Construir el Autoencoder
# El autoencoder consta de un codificador (encoder) y un decodificador (decoder).
input_img = tf.keras.Input(shape=(28, 28, 1))

# Codificador
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
encoded = layers.MaxPooling2D((2, 2), padding='same')(x)

# En este punto, la representación codificada es (7, 7, 32)

# Decodificador
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(encoded)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
decoded = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

# Crear el modelo del autoencoder
autoencoder = models.Model(input_img, decoded)

# Compilar el modelo
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Imprimir un resumen del modelo
autoencoder.summary()

# 4. Entrenar el Autoencoder
# Se entrena el modelo para reconstruir las imágenes originales a partir de las imágenes ruidosas.
autoencoder.fit(x_train_noisy, x_train, 
                epochs=10, 
                batch_size=128, 
                shuffle=True, 
                validation_data=(x_test_noisy, x_test))

# 5. Visualizar los resultados
# Se muestran las imágenes ruidosas de entrada y las imágenes reconstruidas por el autoencoder.
decoded_imgs = autoencoder.predict(x_test_noisy)

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    # Mostrar imagen original ruidosa
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test_noisy[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Mostrar imagen reconstruida
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
