# Edge Computing y TinyML

El **Edge Computing** (Computación en el Borde) es un paradigma de computación distribuida que acerca el procesamiento de datos y la toma de decisiones al lugar donde se originan los datos. En el contexto de Machine Learning, esto se conoce como **Edge AI** o **TinyML**.

En lugar de enviar todos los datos a un servidor centralizado en la nube para su procesamiento, los modelos de ML se ejecutan directamente en dispositivos de borde (*edge devices*).

## ¿Qué es un Dispositivo de Borde?

Es cualquier pieza de hardware con capacidad de cómputo que se encuentra en el "borde" de la red, cerca del usuario o de la fuente de datos. Ejemplos:

- **Dispositivos móviles:** Smartphones, tabletas.
- **Dispositivos IoT:** Sensores inteligentes, cámaras de seguridad, electrodomésticos conectados.
- **Sistemas embebidos:** Microcontroladores (como Arduino, ESP32), computadoras de placa única (como Raspberry Pi).
- **Gateways industriales:** Equipos que conectan la maquinaria de una fábrica a la red.

## Ventajas del Edge AI / TinyML

- **Baja Latencia:** Las decisiones se toman en milisegundos, ya que no hay que esperar una respuesta de la nube. Es crucial para aplicaciones en tiempo real como vehículos autónomos o robótica.
- **Privacidad y Seguridad:** Los datos sensibles (e.g., imágenes de una cámara de seguridad) se procesan localmente y no necesitan salir del dispositivo, mejorando la privacidad.
- **Ancho de Banda Reducido:** Solo se envía a la nube información relevante o agregada, en lugar de flujos de datos brutos, ahorrando costos de comunicación.
- **Funcionamiento Offline:** Las aplicaciones pueden seguir funcionando incluso sin conexión a internet, lo cual es vital para zonas remotas o aplicaciones críticas.
- **Eficiencia Energética:** Procesar datos en el borde puede ser más eficiente energéticamente que transmitirlos constantemente a la nube.

## Desafíos

- **Recursos Limitados:** Los dispositivos de borde tienen una capacidad de cómputo, memoria y energía muy limitada en comparación con los servidores en la nube.
- **Complejidad del Modelo:** No es posible ejecutar modelos de gran tamaño (como los grandes modelos de lenguaje o LLMs) directamente en dispositivos de borde simples. Los modelos deben ser pequeños y altamente optimizados.

## TinyML: Machine Learning para Microcontroladores

**TinyML** es un campo especializado del Edge AI que se enfoca en ejecutar modelos de ML en dispositivos de muy baja potencia, como los microcontroladores. Esto requiere técnicas avanzadas de **optimización de modelos**, como:

- **Cuantificación:** Reducir la precisión de los pesos del modelo (e.g., de 32-bit a 8-bit) para que ocupe menos espacio y se ejecute más rápido.
- **Pruning (Poda):** Eliminar conexiones neuronales (pesos) que tienen poco impacto en el rendimiento del modelo.
- **Frameworks Especializados:** Utilizar librerías como **TensorFlow Lite** o **PyTorch Mobile** para convertir y optimizar modelos para su ejecución en el borde.

Gracias a TinyML, es posible tener inteligencia artificial en dispositivos que cuestan unos pocos dólares y pueden funcionar con una batería durante meses o años.
