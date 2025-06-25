- Algunos estudiantes experimentan problemas con el inicio de los laboratorios y la descarga de los archivos PEM y PPK cuando utilizan Microsoft Internet Explorer o Edge. Si tiene este problema, la solución es utilizar los navegadores Firefox o Chrome. 

- La mayoría de los problemas de acceso al curso están relacionados con el navegador que se utiliza. Actualice siempre el navegador a la versión más reciente. No se recomienda Safari para el acceso móvil ni el de escritorio. 

- Visite este enlace para descargar o actualizar el navegador 

- Si utiliza Safari, habilite las cookies y desactive la opción “Evitar el seguimiento entre sitios”.Links to an external site. 

- Si recibe el mensaje “Las credenciales del enlace de inicio de sesión no son válidas. Contacte con su administrador.”, haga clic en la palabra “aquí” del error para cerrar la sesión y reiniciar el laboratorio. 

# ✅ AWS CONFIGURE 
C:\Users\Rodrigo>aws configure AWS Access Key ID [****************c.cl]: AKIAW64X3ENDW5MQAYJA AWS Secret Access Key [****************014.]: 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 Default region name [us-east-2]: us-east-1 Default output format [json]: 

# ✅ Ver listado de AMI 
aws ec2 describe-images  --owners amazon  --filters "Name=name,Values=Windows_Server-2022-English-Full-Base-*"  "Name=platform,Values=windows"  --query "Images[*].[ImageId,Name]"  --output table 

# ✅ Crear el grupo de seguridad 
aws ec2 create-security-group ^ 

  --group-name WindowsSG ^ 

  --description "Permitir RDP para Windows Server" ^ 

  --vpc-id vpc-0f7e8f633c1f01538 

# ✅ Crear un nuevo par de claves
aws ec2 create-key-pair --key-name MiClaveWindows --query 'KeyMaterial' --output text > MiClaveWindows.pem

# ❌ Abrir el puerto RDP (3389) desde tu IP pública 
aws ec2 authorize-security-group-ingress ^ 
  --group-id sg-0123456789abcdef0 ^ 
  --protocol tcp ^ 
  --port 3389 ^ 
  --cidr 192.168.1.147/32 

# ✅ Opción abierta a todo el mundo (no recomendado salvo pruebas): 
aws ec2 authorize-security-group-ingress ^
  --group-id sg-0a2991d36ea558353 ^
  --protocol tcp ^
  --port 3389 ^
  --cidr 0.0.0.0/0

![alt text](image.png)

# ✅ Ver Group ID 

aws ec2 describe-security-groups --group-names sg-0a2991d36ea558353 --query "SecurityGroups[*].GroupId" --output text 

# ✅ Correr instancia
aws ec2 run-instances ^
  --image-id ami-0345f44fe05216fc4 ^
  --instance-type t3.medium ^
  --key-name MiClaveWindows ^
  --security-group-ids sg-0a2991d36ea558353 ^
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=WindowsServerCLI}]"

# Obtén la IP pública de tu instancia (necesaria para RDP): 44.203.162.184
aws ec2 describe-instances --instance-ids i-0266a97a0c701a232 --query "Reservations[*].Instances[*].PublicIpAddress" --output text

# Obtén la contraseña del usuario administrador (Administrator)
aws ec2 get-password-data --instance-id i-0266a97a0c701a232 --priv-launch-key MiClaveWindows.pem --query PasswordData --output text | base64 --decode > password.txt

# Conéctate por RDP
Usuario: Administrator
IP: la IP pública obtenida (44.203.162.184)
Contraseña: la que obtuviste en password.txt

#   Verifica que tu instancia está en estado running
aws ec2 describe-instances --instance-ids i-0266a97a0c701a232 --query "Reservations[*].Instances[*].State.Name" --output text

# Confirma que usas la clave privada correcta y sin modificar