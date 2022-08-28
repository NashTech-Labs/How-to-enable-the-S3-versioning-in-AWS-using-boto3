# MuZakkir Saifi
# import the boto3 which will use to interact  with the aws

import boto3

REGION = input("Enter the REGION Name")
BUCKET_NAME = input("Enter the bucket name")

resource_for_s3 = boto3.resource("s3", region_name=REGION)

def enable(bucket_name):
    versioning = resource_for_s3.BucketVersioning(bucket_name)
    versioning.enable()

    print(f'Wow, Your versioning is enabled for S3 Bucket: {versioning.status}')

enable(BUCKET_NAME)