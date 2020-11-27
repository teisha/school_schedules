import os
import pytest
import services.dynamodb_service as dbs
import boto3
session = boto3.session.Session(profile_name='power-user')

os.environ["TABLE_NAME"] = 'visual-schedules-data-table'
os.environ["SECRET"] = "SyqT8jTGkyBUNBH1IFrcqb"
os.environ["ALG"] = 'HS256'
os.environ["LOGGING_LEVEL"] = 'DEBUG'

@pytest.fixture(scope="module")
def get_db():
    table_name = 'visual-schedules-data-table'
    return dbs.DynamoService(table_name)