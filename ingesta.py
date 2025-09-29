import mysql.connector
import csv
import boto3

# Conexión con la base de datos MySQL
db_config = {
    'host': 'localhost',  # Cambiar por tu host
    'user': 'root',       # Cambiar por tu usuario
    'password': 'admin123',  # Cambiar por tu contraseña
    'database': 'data'  # Cambiar por el nombre de tu base de datos
}

# Conectar a la base de datos
db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

# Consulta para obtener los registros
cursor.execute("SELECT * nombre_tabla")  # Cambiar por la tabla de tu base de datos

# Obtener todos los registros
registros = cursor.fetchall()

# Escribir los registros en un archivo CSV
with open("data.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir los encabezados (nombre de las columnas)
    writer.writerow([i[0] for i in cursor.description])
    # Escribir los datos
    writer.writerows(registros)

# Cerrar la conexión con la base de datos
cursor.close()
db_connection.close()

# Subir el archivo CSV al bucket S3
ficheroUpload = "data.csv"
nombreBucket = "f4mmeri-storage-s2"  # Cambiar por tu bucket S3

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "ingesta/" + ficheroUpload)
print(response)

print("Ingesta completada")
