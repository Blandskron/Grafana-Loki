FROM python:3.12

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo log.py al contenedor
COPY log.py .

# Comando para ejecutar el script
CMD ["python", "log.py"]
