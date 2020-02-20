import boto3
import os


def get_client():
    session = boto3.session.Session()

    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    s3_localstack_url = os.getenv('S3_LOCALSTACK_URL')

    if s3_localstack_url is None:
        s3 = session.client(
            service_name='s3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    else:
        s3 = session.client(
            service_name='s3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            endpoint_url=s3_localstack_url
        )

    return s3


def get_download_folder():
    download_folder = "/tmp"

    if os.getenv('DOWNLOAD_FOLDER') is not None:
        download_folder = os.getenv('DOWNLOAD_FOLDER')

    return download_folder
