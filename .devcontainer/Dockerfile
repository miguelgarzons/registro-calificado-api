FROM python:3.11-slim

# Carpeta de trabajo
WORKDIR /app

# Dependencias del sistema (incluyendo git)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    bash \
    dos2unix \
    git \
    ssh \
    && rm -rf /var/lib/apt/lists/*

# Copiar entrypoint y convertir finales de línea
COPY entrypoint.sh /app/entrypoint.sh
RUN dos2unix /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar ipython, debugpy (para VS Code debugging)
RUN pip install ipython debugpy

# Copiar el proyecto
COPY . .

EXPOSE 8000

# Usar bash como shell por defecto
SHELL ["/bin/bash", "-c"]

# Definir el entrypoint usando bash explícitamente
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
