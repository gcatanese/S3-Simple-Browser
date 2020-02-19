import boto3

def get_client():

    session = boto3.session.Session()

    s3 = session.client(
        service_name='s3',
        aws_access_key_id='aws01',
        aws_secret_access_key='aws01',
        endpoint_url='http://localhost:4572'
    )

    return s3