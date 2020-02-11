import boto3 as bt
import botocore

BUCKET_NAME = 'cloud25555555' # replace with your bucket name
KEY = 'hello5.txt' # replace with your object key
namefile ='textfiledownload.txt'
s3 = bt.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, namefile)
    print("Donwload file: ", KEY, "and his name is: ", namefile)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise