import boto3 as bt

s3 = bt.resource('s3')

bucketname = "cloud25555555"
buckernamedest = "cloudbuck192322"
namefile ="hello.txt"
namefiledest ="hello.txt"
copy_source ={
    'Bucket': bucketname,
    'Key': namefile
}
        
s3.meta.client.copy(copy_source,buckernamedest,namefiledest)
filedel = s3.Object(bucketname, namefile)
filedel.delete()