Este repositorio cuenta con 2 Pipfile:

- Exterior: Para versionamiento con DVC.
- P2025/Machine Learning (TIEL26): Para ejemplos del curso de Machine Learning - INACAP Ñuñoa 2025.

# Parte A
# 1. Instalar DVC usando Pipenv
pipenv install dvc
## Google Drive
pipenv install "dvc[gdrive]"
## AWS S3
pipenv install "dvc[s3]"
## Azure
pipenv install "dvc[azure]"
## SSH
pipenv install "dvc[ssh]"

# 2. Entrar al entorno virtual de Pipenv
pipenv shell

# 3. Inicializar DVC en tu repositorio
dvc init
git add .
git commit -m "Inicializa DVC"

# 4. Agregar tus archivos/carpetas a DVC (ejemplo)
dvc add "P2025/Machine Learning (TIEL26)/U4 Implementación modelo Deep learning/modelo_entrenado"
dvc add "P2025/Machine Learning (TIEL26)/U4 Implementación modelo Deep learning/results"
git add .
git commit -m "Seguimiento DVC a modelo entranado y resultados"

# Parte B
# PASO 1 — Entrar a Google Cloud Console
# PASO 2 — Crear un proyecto nuevo
# PASO 3 — Habilitar la API de Google Drive
# PASO 4 — Crear la Service Account
# PASO 5 — Crear la llave JSON
# PASO 6 — Compartir tu carpeta de Google Drive con la Service Account
# PASO 7 — Configurar DVC para usar la Service Account
# PASO 8 — Probar

# Parte C
# Instalar el soporte para Google Drive en tu entorno Pipenv
pipenv install dvc-gdrive
# 1. Verifica si tienes un remoto configurado
dvc remote list
- Si NO tienes remoto configurado, sigue el paso 2.
# 2. Configurar un remoto (solo una vez)
- Crea una carpeta en Google Drive
- Copia el ID de la carpeta
- Configura el remoto:
dvc remote add -d gdrive gdrive://<ID_DE_LA_CARPETA>
dvc remote modify gdrive gdrive_use_service_account false
# 3. Hacer el PUSH
dvc push
# 4. Commit al repo (solo metadatos)
git add .
git commit -m "Subo primeras versiones de datos/modelos vía DVC"
git push
