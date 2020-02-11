import boto3 
import botocore

s3 = boto3.resource('s3')
bucketname = "cloud25555555"
bucket = s3.Bucket(bucketname)
print("\n")
print("Archivos contenedor: ",bucketname)
for my_bucket_object in bucket.objects.all():
    print("\n")
    print(my_bucket_object)
print("\n")   