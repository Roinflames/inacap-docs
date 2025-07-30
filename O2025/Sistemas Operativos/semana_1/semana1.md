# I. Interconexión de dispositivos y redes
## 1.1 Conceptos básicos
- Red, subred, nodo, host
    Red: Conjunto de dispositivos interconectados que comparten recursos.
    Subred: División lógica de una red para segmentar tráfico o mejorar rendimiento.
    Nodo: Cualquier dispositivo que forma parte de la red (puede ser una impresora, PC, router, etc.).
    Host: Dispositivo final con dirección IP (computadoras, teléfonos, etc.).
- LAN, WAN, MAN
    LAN (Local Area Network): Red local dentro de un área limitada (oficina, casa).
    MAN (Metropolitan Area Network): Red que abarca una ciudad o campus.
    WAN (Wide Area Network): Red extensa que interconecta LANs geográficamente dispersas (ejemplo: Internet).
- Topologías de red (estrella, bus, anillo, malla)
    Estrella: Todos los dispositivos conectados a un nodo central (switch).
    Bus: Todos los dispositivos comparten un solo canal de comunicación.
    Anillo: Cada dispositivo tiene dos conexiones formando un círculo.
    Malla: Cada dispositivo se conecta con todos los demás.
- Equipos de interconexión: Switch, Router, Hub, Access Point
    Switch: Conecta dispositivos en una red LAN. Opera en capa 2.
    Router: Conecta diferentes redes. Toma decisiones de encaminamiento (capa 3).
    Hub: Dispositivo obsoleto que reenvía datos a todos los puertos sin filtrado.
    Access Point: Punto de acceso inalámbrico a una red cableada.
## 1.2 Modelo OSI y TCP/IP
- Capas y funciones Modelo OSI
    Aplicación
    Presentación
    Sesión
    Transporte
    Red
    Enlace de datos
    Física
- Capas y funciones Modelo TCP/IP
    Aplicación
    Transporte
    Internet
    Acceso a la red

- Comparación de ambos modelos
| OSI                                          | TCP/IP                          |
| -------------------------------------------- | ------------------------------- |
| 7 capas                                      | 4 capas                         |
| Más académico                                | Más práctico                    |
| Define con precisión la función de cada capa | Basado en protocolos estándares |


## 1.3 Dirección IP
- IPv4 vs IPv6
    IPv4: 32 bits, más usado, agotamiento de direcciones.
    IPv6: 128 bits, más direcciones disponibles, seguridad mejorada.
- Dirección IP: estructura (32 bits), decimal con puntos
    32 bits divididos en 4 octetos (ejemplo: 192.168.1.1)
    Notación decimal con puntos
- Componentes: ID de red y ID de host
    ID de red: Identifica la red.
    ID de host: Identifica un dispositivo dentro de la red.
- Máscara de subred
    Determina qué parte de la IP es red y cuál host.
    Ejemplo: 255.255.255.0 = 24 bits para red, 8 para host

# II. Cálculo de clases de dirección
## 2.1 Clases de direcciones IPv4
Clase	Rango de direcciones	Uso
A	1.0.0.0 - 126.255.255.255	Redes grandes
B	128.0.0.0 - 191.255.255.255	Redes medianas
C	192.0.0.0 - 223.255.255.255	Redes pequeñas
D	224.0.0.0 - 239.255.255.255	Multicast
E	240.0.0.0 - 255.255.255.255	Experimental

Dirección pública vs privada
    Privadas (uso interno):
    Clase A: 10.0.0.0 – 10.255.255.255
    Clase B: 172.16.0.0 – 172.31.255.255
    Clase C: 192.168.0.0 – 192.168.255.255

    Públicas: Asignadas por un ISP, accesibles desde Internet
  
Direcciones reservadas
    127.0.0.1: Loopback (localhost)
    169.254.x.x: APIPA (asignación automática)
    255.255.255.255: Broadcast

## 2.2 Ejercicios
Determinar la clase de una dirección dada
Identificar dirección de red y broadcast

# III. Técnicas de cálculo VLSM (Variable Length Subnet Mask)
## 3.1 ¿Qué es VLSM?
Subneteo con diferentes máscaras
Optimización de direcciones IP

## 3.2 Pasos para aplicar VLSM
Lista de necesidades (cantidad de hosts por subred)
Ordenar de mayor a menor
Asignar bloques según la necesidad
Determinar direcciones de red, broadcast, y rango válido de hosts

## 3.3 Ejercicios de práctica
Subneteo con VLSM para diferentes escenarios de red