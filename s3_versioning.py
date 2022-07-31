# import the boto3 which will use to interact  with the aws

import boto3

AWS_REGION = input("Enter the AWS_REGION Name")
BUCKET_NAME = input("Enter the bucket name")

s3_resource = boto3.resource("s3", region_name=AWS_REGION)

def enable(bucket_name):
    versioning = s3_resource.BucketVersioning(bucket_name)
    versioning.enable()

    print(f'Wow, Your versioning is enabled for S3 Bucket: {versioning.status}')

enable(BUCKET_NAME)