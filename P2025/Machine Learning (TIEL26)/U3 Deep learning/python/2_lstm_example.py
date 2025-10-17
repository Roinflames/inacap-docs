# Ejemplo de Red Neuronal Recurrente (LSTM) con TensorFlow y Keras
# Este ejemplo muestra cómo construir y entrenar una LSTM para clasificación de sentimientos en el conjunto de datos IMDB.

import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# 1. Cargar y preprocesar el conjunto de datos IMDB
# El conjunto de datos IMDB contiene 50,000 reseñas de películas, divididas en 25,000 para entrenamiento y 25,000 para prueba.
# Las palabras están pre-codificadas como enteros.
num_words = 10000  # Se consideran las 10,000 palabras más frecuentes
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=num_words)

# Las secuencias (reseñas) tienen diferentes longitudes. Se utiliza padding para que todas tengan la misma longitud.
maxlen = 256  # Longitud máxima de las secuencias
train_data = pad_sequences(train_data, maxlen=maxlen)
test_data = pad_sequences(test_data, maxlen=maxlen)

# 2. Construir el modelo LSTM
# El modelo es una secuencia de capas: Embedding, LSTM y Dense.
model = Sequential()
# La capa Embedding convierte los enteros (palabras) en vectores densos de un tamaño fijo.
model.add(Embedding(num_words, 32, input_length=maxlen))
# La capa LSTM procesa las secuencias de vectores.
model.add(LSTM(32))
# La capa de salida es una neurona densa con activación sigmoide para clasificación binaria (sentimiento positivo/negativo).
model.add(Dense(1, activation='sigmoid'))

# Imprimir un resumen del modelo
model.summary()

# 3. Compilar y entrenar el modelo
# Se utiliza el optimizador Adam, la función de pérdida binary_crossentropy (adecuada para clasificación binaria)
# y se monitorea la precisión.
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo durante 10 épocas con un 20% de los datos para validación.
history = model.fit(train_data, train_labels, epochs=10, batch_size=128, validation_split=0.2)

# 4. Evaluar el modelo
# Se evalúa el rendimiento del modelo con el conjunto de datos de prueba.
results = model.evaluate(test_data, test_labels, verbose=2)
print(f"\nPrecisión en el conjunto de prueba: {results[1]}")

# 5. Hacer una predicción
# Para predecir el sentimiento de una nueva reseña, se debe preprocesar de la misma manera que los datos de entrenamiento.
# (Este paso es conceptual, ya que necesitaríamos el diccionario de palabras para una nueva reseña).
word_index = imdb.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in text])

# Ejemplo de predicción con un dato de prueba
prediction = model.predict(test_data[0:1])
print(f"\nReseña de prueba: {decode_review(test_data[0])}")
print(f"Predicción de sentimiento (0=negativo, 1=positivo): {prediction[0][0]}")
