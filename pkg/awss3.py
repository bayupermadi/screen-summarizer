import logging
import boto3
from botocore.exceptions import ClientError
import os

s3_client = boto3.client('s3')

def upload(file_name, bucket):
    object_name = os.path.basename(file_name)

    # Upload the file
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def delete_file(file_name, bucket):
    # Delete the file
    try:
        response = s3_client.delete_object(Bucket=bucket, Key=file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True