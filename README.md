## How to enable the  AWS S3 versioning using boto3.

#### Versioning in Amazon S3 is a means of keeping multiple variants of an object in the same bucket. You can use the S3 Versioning feature to preserve, retrieve, and restore every version of every object stored in your buckets. With versioning you can recover more easily from both unintended user actions and application failures. After versioning is enabled for a bucket, if Amazon S3 receives multiple write requests for the same object simultaneously, it stores all of those objects. You can follow this [link](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) to know more.

-------------

**Files:** 
```
      s3_versioning.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to enable the versioning.

        python3 s3_versioning.py

















