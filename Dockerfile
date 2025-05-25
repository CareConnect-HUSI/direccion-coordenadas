# Imagen base
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que corre FastAPI
EXPOSE 8001

# Comando para arrancar el servidor
CMD ["uvicorn", "direccionACoord:app", "--host", "0.0.0.0", "--port", "8001"]
