import boto3 as bt

s3 = bt.resource('s3')

bucketname = "cloud25555555"
bucket = s3.Bucket(bucketname)

print("\n")
print("Archivos contenedor: ",bucketname)
for my_bucket_object in bucket.objects.all():
    if my_bucket_object != None:
        print("¿Esta seguro que desea borrar el elemento",my_bucket_object.key," del bucket ", bucketname, " s / n")
        respuesta = input()
        if respuesta == "s" or "S":
            print("\n")
            print(my_bucket_object.key)
            filedel = s3.Object(bucketname, my_bucket_object.key)
            filedel.delete()
bucket.delete()
print("\n")   


