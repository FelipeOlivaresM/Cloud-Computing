import boto3 as bt
import botocore

s3 = bt.resource('s3')
def create_bucket(bucketname):
    client = bt.client('s3')

    response = client.create_bucket(Bucket=bucketname)
    print(response)

def uploadfile(bucketname,pathfile,namefile):
    s3.meta.client.upload_file(pathfile, bucketname, namefile)
    print("File Upload Successfully")

def listbucketfiles(bucketname):
    bucket = s3.Bucket(bucketname)
    print("\n")
    print("Archivos contenedor: ",bucketname)
    for my_bucket_object in bucket.objects.all():
        print("\n")
        print(my_bucket_object)
    print("\n")   


def downloadfile(bucketname,filename,filenamedownload):
    s3 = bt.resource('s3')

    try:
        s3.Bucket(bucketname).download_file(filename, filenamedownload)
        print("Donwload file: ", filename, "and his name is: ", filenamedownload)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def deletebucketandfiles(bucketname):
    
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