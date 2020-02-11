import boto3 as bt

client = bt.client('s3')

response = client.create_bucket(Bucket="cloud25555555")
print(response)

