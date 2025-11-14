Este repositorio cuenta con 2 Pipfile:

- Exterior: Para versionamiento con DVC.
- P2025/Machine Learning (TIEL26): Para ejemplos del curso de Machine Learning - INACAP Ñuñoa 2025.

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