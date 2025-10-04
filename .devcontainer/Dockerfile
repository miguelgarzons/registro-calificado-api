FROM python:3.11-slim

# Carpeta de trabajo
WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar ipython, debugpy (para VS Code debugging)
RUN pip install ipython debugpy

# Copiar el proyecto
COPY . .

EXPOSE 8000
