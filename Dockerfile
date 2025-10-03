# Dockerfile
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el proyecto
COPY . /app/

# Comando por defecto (lo sobreescribiremos en docker-compose si hace falta)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
