import sys

import boto3

# consts
AWS_ACCESS_KEY = 'test-key'
AWS_SECRET_ACCESS_KEY = 'test-access-key'
AWS_ENDPOINT_URL = 'http://0.0.0.0:9878'


def main() -> None:
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        endpoint_url=AWS_ENDPOINT_URL,
    )

    bucket = sys.argv[1]
    replica_name = sys.argv[2]
    path_to_file = sys.argv[3]

    s3_client.upload_file(path_to_file, bucket, replica_name)


if __name__ == '__main__':
    main()