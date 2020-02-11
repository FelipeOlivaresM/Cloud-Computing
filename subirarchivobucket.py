import boto3 as bt

s3 = bt.resource('s3')
bucketname = "cloud25555555"
s3.meta.client.upload_file('./hello1.txt', bucketname, 'hello2.txt')
print("File Upload Successfully")