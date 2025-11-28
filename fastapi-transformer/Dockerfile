# Imagen base oficial de Python
FROM python:3.10-slim

# Evita preguntas interactivas
ENV DEBIAN_FRONTEND=noninteractive

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements primero (mejor cache)
COPY requirements.txt .

# Instalar PyTorch CPU (sin GPU)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Instalar el resto de dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY . .

# Ejecutar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]