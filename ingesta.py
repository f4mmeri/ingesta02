import boto3

ficheroUpload = "data.csv"
nombreBucket = "f4mmeri-storage-s2"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "ingesta/"+ficheroUpload)
print(response)

print("Ingesta completada")