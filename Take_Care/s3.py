import boto3
import logging
from botocore.exceptions import ClientError

def listing_s3_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket["Name"])

# listing_s3_buckets()
    
def creating_s3_bucket(bucket_name, region):
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        return True
    except ClientError as e:
        logging.error(e)
        return False
    
creating_s3_bucket('x23176245-s3-bucket', 'eu-west-1')

def upload_file(file, bucket_name, file_key, content_type):
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_fileobj(Fileobj=file, Bucket=bucket_name, Key=file_key, ExtraArgs={'ContentType': content_type})
        object_url = f"https://{bucket_name}.s3.amazonaws.com/{file_key}"
        return { 'object_url': object_url, 'file_key': file_key }
    except ClientError as e:
        logging.error(e)
        return False
    
def delete_file(bucket_name, file_key):
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_object(Bucket=bucket_name, Key=file_key)
        return True
    except ClientError as e:
        logging.error(e)
        return False