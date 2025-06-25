# Paso a paso para crear una instancia Windows Server en AWS usando CLI, con un par de claves nuevo y acceso RDP
1️⃣ ✅ Crear un nuevo par de claves (y descargar el archivo .pem)
aws ec2 create-key-pair --key-name MiClaveWindowsNueva --query 'KeyMaterial' --output text > MiClaveWindowsNueva.pem

2️⃣ ✅ Crear un grupo de seguridad con regla para RDP (puerto 3389)
aws ec2 create-security-group --group-name WindowsSG2 --description "Grupo para Windows Server" --vpc-id vpc-0f7e8f633c1f01538

Luego abre el puerto RDP para tu IP:
aws ec2 authorize-security-group-ingress --group-id sg-0545c28f8e980ca5f --protocol tcp --port 3389 --cidr 0.0.0.0/0

3️⃣ ✅ Buscar la AMI oficial de Windows Server 2022

4️⃣ ✅ Lanzar la instancia
aws ec2 run-instances --image-id ami-0345f44fe05216fc4 --instance-type t3.medium --key-name MiClaveWindowsNueva --security-group-ids sg-0545c28f8e980ca5f --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=WindowsServerCLI}]"

5️⃣ ✅ Esperar que la instancia esté en estado running
aws ec2 describe-instances --instance-ids i-01a648647e18ae34b --query "Reservations[*].Instances[*].State.Name" --output text

6️⃣ ✅ Obtener la IP pública (34.229.7.169)
aws ec2 describe-instances --instance-ids i-01a648647e18ae34b --query "Reservations[*].Instances[*].PublicIpAddress" --output text

7️⃣ Obtener la contraseña del administrador
aws ec2 get-password-data --instance-id i-01a648647e18ae34b --priv-launch-key .\MiClaveWindowsNueva.pem --query PasswordData --output text
aws ec2 get-password-data --instance-id i-01a648647e18ae34b --priv-launch-key .\MiClaveWindows2.pem --query PasswordData --output text

$instanceId = "i-01a648647e18ae34b"
$keyPath = ".\MiClaveWindowsNueva.pem"
$base64 = aws ec2 get-password-data --instance-id $instanceId --priv-launch-key $keyPath --query PasswordData --output text

if ($base64) {
    $password = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($base64))
    Write-Host "Contraseña obtenida: $password"
} else {
    Write-Host "La contraseña aún no está disponible, espera unos minutos e intenta de nuevo."
}

https://report-uri.com/home/pem_decoder

8️⃣ Conectarte por RDP
Presiona Win + R y escribe mstsc y presiona Enter.
En el campo Equipo, escribe la IP pública que obtuviste en el paso 1.
Haz clic en Conectar.

Usa la IP pública:
34.229.7.169

Usuario: 
Administrator 

Contraseña: la que obtuviste en el paso anterior. 
\x0a;6c0a6e67-73da-4f10-aa55-86b37bb21cb9