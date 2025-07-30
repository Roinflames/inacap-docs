# ☁️ OPCIÓN 1: Usar otra máquina EC2 en AWS (recomendado para práctica de laboratorio)
✅ Ventajas:
- Está en la misma red (VPC y subred) que el servidor.
- No necesitas configurar VPN ni túneles.
- Conectividad entre cliente y servidor es directa.
- Rápido para pruebas con múltiples usuarios.

🧭 Pasos:
- Crea otra instancia EC2 con Windows 10 o 11.
- Configura una IP privada fija (ej. 172.31.90.65).
- Usa como DNS el IP del Domain Controller (172.31.90.64 en tu caso).
- Cambia el nombre del equipo.
- Une al dominio (midominio.local) desde Sistema > Cambiar configuración.
- Usa credenciales del dominio.

# 💻 OPCIÓN 2: Usar tu PC local (solo si tienes VPN o túnel)
⚠️ Requiere:
- Que tu computador local esté en la misma red privada que el DC.
Para eso necesitas:
- Una VPN site-to-site o
- Un túnel (como WireGuard o SoftEther VPN) o
- AWS Client VPN configurado correctamente.

Además, tu máquina debe usar como DNS la IP privada del servidor en AWS.

🚫 Sin VPN:
- Tu equipo local no podrá ver el dominio ni resolver midominio.local, porque:
- Estás fuera de la VPC.
- No puedes usar la IP privada de EC2 directamente.

🎯 Conclusión
| Opción              | Recomendado para | Conectividad           | Configuración |
| ------------------- | ---------------- | ---------------------- | ------------- |
| **Otra EC2 en AWS** | Laboratorio      | Fácil (misma VPC)      | Sencilla      |
| **Tu PC local**     | Avanzado / real  | Difícil (requiere VPN) | Compleja      |

