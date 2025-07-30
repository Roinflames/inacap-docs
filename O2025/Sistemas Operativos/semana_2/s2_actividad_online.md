# Enunciado
Tienes asignada la red principal 192.168.100.0/24. Debes subdividirla en subredes VLSM para atender los siguientes requerimientos de número de hosts:

| Subred         | Nº de hosts requeridos |
| -------------- | ---------------------: |
| Departamento A |             Fifty (50) |
| Departamento B |       Twenty‑five (25) |
| Departamento C |            Twelve (12) |
| Departamento D |                Six (6) |
| Departamento E |                Two (2) |

## Tareas:

1. Ordena las subredes de mayor a menor por cantidad de hosts.
2. Asigna bloques contiguos dentro de 192.168.100.0/24 usando VLSM.
3. Para cada subred, determina:

- Máscara de subred en notación decimal y CIDR.
- Rango de hosts válidos.
- Dirección de broadcast.

## Solución paso a paso
### 1. Ordenar por tamaño
A (50), B (25), C (12), D (6), E (2).

### 2. Calcular tamaños mínimo de bloque

- Para ≥50 hosts → necesitamos al menos /26 → 62 hosts
- Para ≥25 hosts → /27 → 30 hosts
- Para ≥12 hosts → /28 → 14 hosts
- Para ≥6 hosts → /29 → 6 hosts
- Para ≥2 hosts → /30 → 2 hosts

### 3. Asignación VLSM

| Subred     | Bloque asignado    | Máscara               | Rango de hosts                    | Broadcast       |
| ---------- | ------------------ | --------------------- | --------------------------------- | --------------- |
| **A (50)** | 192.168.100.0/26   | 255.255.255.192 (/26) | 192.168.100.1 – 192.168.100.62    | 192.168.100.63  |
| **B (25)** | 192.168.100.64/27  | 255.255.255.224 (/27) | 192.168.100.65 – 192.168.100.94   | 192.168.100.95  |
| **C (12)** | 192.168.100.96/28  | 255.255.255.240 (/28) | 192.168.100.97 – 192.168.100.110  | 192.168.100.111 |
| **D (6)**  | 192.168.100.112/29 | 255.255.255.248 (/29) | 192.168.100.113 – 192.168.100.118 | 192.168.100.119 |
| **E (2)**  | 192.168.100.120/30 | 255.255.255.252 (/30) | 192.168.100.121 – 192.168.100.122 | 192.168.100.123 |

Nota: Tras asignar E, el siguiente bloque libre empieza en 192.168.100.124/30.

## Explicación rápida
- Un bloque /26 ofrece 64 direcciones totales (62 útiles para hosts).
- Un /27 ofrece 32 (30 útiles), un /28 16 (14 útiles), un /29 8 (6 útiles) y un /30 4 (2 útiles).
- Siempre empiezas con la subred de mayor requerimiento en el primer bloque libre y vas asignando bloques contiguos hacia arriba.

Con esto cubres la asignación VLSM, maximizando el aprovechamiento del espacio y evitando desperdicios. Si quieres más práctica o un caso distinto, ¡dime!