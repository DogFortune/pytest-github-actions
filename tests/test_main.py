import pytest
import boto3
import os
from create_param import main

os.environ["AWS_ACCESS_KEY_ID"] = "AKIAIOSFODNN7EXAMPLE"
os.environ["AWS_SECRET_ACCESS_KEY"] = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = os.getenv("AWS_REGION", "ap-northeast-1")
ENDPOINT = os.getenv("LOCALSTACK_ENDPOINT", "http://localhost:4566")


@pytest.fixture(scope="session")
def s3_local():
    s3 = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT)
    return s3


@pytest.fixture()
def setup_s3(s3_local):
    """
    S3へのテストデータ作成

    :param s3_local: _description_
    :type s3_local: _type_
    """
    bucket_name = "sample"
    object_key = "dummy.txt"

    s3_local.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "ap-northeast-1"},
    )
    s3_local.put_object(Bucket=bucket_name, Key=object_key)

    yield

    s3_local.delete_object(Bucket=bucket_name, Key=object_key)
    s3_local.delete_bucket(Bucket=bucket_name)


def test_local_stack(setup_s3, s3_local):
    s3_local.head_object(
        Bucket="sample",
        Key="dummy.txt",
    )


def test_main():
    actual = main.main(3, 4)
    assert actual == 7
