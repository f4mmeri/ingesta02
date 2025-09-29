# Usa una imagen base con Python
FROM python:3-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /programas/ingesta

# Instala las dependencias necesarias
RUN pip3 install boto3 mysql-connector-python

# Copia todos los archivos del directorio actual al contenedor
COPY . .

# COPY ~/.aws /root/.aws

# Comando para ejecutar el script
CMD [ "python3", "./ingesta.py" ]
