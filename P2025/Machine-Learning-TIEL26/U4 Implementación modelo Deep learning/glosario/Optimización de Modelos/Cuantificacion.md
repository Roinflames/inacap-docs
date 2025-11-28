# Cuantificación de Modelos (Quantization)

La **cuantificación** es una de las técnicas de optimización y compresión de modelos más importantes y efectivas. Consiste en **reducir la precisión numérica** utilizada para representar los pesos y/o las activaciones de una red neuronal.

En lugar de almacenar estos valores como números de punto flotante de 32 bits (FP32), que es el estándar durante el entrenamiento, se convierten a formatos de menor precisión, como punto flotante de 16 bits (FP16) o, más comúnmente, enteros de 8 bits (INT8).

---

## ¿Cómo Funciona la Cuantificación?

La idea central es mapear un rango de valores de alta precisión (continuos, en FP32) a un rango de valores de baja precisión (discretos, en INT8).

Un entero de 8 bits puede representar 256 valores distintos (de -128 a 127 o de 0 a 255). El proceso de cuantificación debe encontrar la mejor manera de asignar el rango completo de pesos de una capa del modelo a estos 256 niveles.

Esto se logra mediante una fórmula de mapeo lineal simple:

`valor_real ≈ (valor_entero - punto_cero) * escala`

- **Escala (Scale):** Un factor de punto flotante que define el tamaño de cada "paso" en el rango cuantificado.
- **Punto Cero (Zero-Point):** Un valor entero que asegura que el número real `0.0` se mapee exactamente a un valor entero. Esto es crucial, ya que operaciones como el padding con ceros son muy comunes.

Tanto la escala como el punto cero se calculan para cada capa (o incluso para cada canal de una capa) y se almacenan junto con el modelo para poder realizar la de-cuantificación cuando sea necesario.

---

## Beneficios de la Cuantificación

1.  **Reducción del Tamaño del Modelo:**
    - Es el beneficio más directo. Al pasar de 32 bits a 8 bits por parámetro, el tamaño del modelo se reduce en un factor de **4x**. Un modelo de 400 MB en FP32 pasa a ocupar solo 100 MB en INT8.

2.  **Menor Latencia (Mayor Velocidad de Inferencia):**
    - Los procesadores modernos (CPUs y GPUs) y, especialmente, el hardware especializado (TPUs, NPUs en móviles) son mucho más rápidos realizando cálculos con enteros que con punto flotante.
    - Esto puede resultar en una aceleración de la inferencia de **2x a 4x** o más.

3.  **Menor Consumo de Energía:**
    - Las operaciones con enteros consumen menos energía que las de punto flotante. Esto es vital para dispositivos que funcionan con batería.

4.  **Menor Ancho de Banda de Memoria:**
    - Al ser más pequeños, se necesita mover menos datos desde la memoria principal hacia las unidades de cómputo, reduciendo cuellos de botella.

---

## Métodos de Cuantificación

Existen dos enfoques principales para aplicar la cuantificación:

### 1. Cuantificación Post-Entrenamiento (Post-Training Quantization - PTQ)

- **¿Qué es?:** Es el método más simple y común. Se toma un modelo ya entrenado en FP32 y se convierte a INT8 sin necesidad de re-entrenar.
- **¿Cómo funciona?:** Se necesita un pequeño conjunto de datos de "calibración" (unas 100-500 muestras representativas). El modelo se ejecuta con estos datos para registrar el rango de valores de las activaciones. Con los rangos de los pesos (que son fijos) y de las activaciones, TFLite (o el framework correspondiente) calcula los parámetros de `escala` y `punto_cero` óptimos.
- **Ventajas:** Rápido y fácil de implementar.
- **Desventajas:** Puede haber una pequeña pérdida de precisión, especialmente en modelos más pequeños o sensibles.

### 2. Entrenamiento Consciente de la Cuantificación (Quantization-Aware Training - QAT)

- **¿Qué es?:** Se introduce la simulación de la cuantificación (el error de redondeo) directamente en el grafo del modelo **durante el proceso de entrenamiento** (o durante una fase de fine-tuning).
- **¿Cómo funciona?:** El modelo "aprende" a ser robusto frente a los efectos de la cuantificación, ajustando sus pesos para minimizar la pérdida de precisión que ocurrirá después de la conversión.
- **Ventajas:** Generalmente, se obtiene una **mayor precisión** que con PTQ, muy cercana a la del modelo FP32 original.
- **Desventajas:** Es un proceso más complejo que requiere re-entrenamiento o fine-tuning del modelo.

La cuantificación es una técnica esencial para el despliegue eficiente de modelos y es un pilar fundamental de **TensorFlow Lite** y **TinyML**.
