import boto3
import os
from boto3.dynamodb.conditions import Key


class DynamoDbService:
    def __init__(self):
        dynamoDb = boto3.resource("dynamodb")
        self._table = dynamoDb.Table(os.environ["DYNAMO_TABLE"])

    def queryOnPrimaryKey(self, key):
        return self._table.query(
            KeyConditionExpression=Key("key").eq(key)
        )["Items"]

    def getItem(self, key, sort):
        return self._table.get_item(
            Key={
                'key': key,
                'id': sort
            }
        )["Item"]

    def queryTypeIndex(self, type, itemId=None):
        if itemId is None:
            return self._table.query(IndexName="typeIndex",
                                     Select="ALL_ATTRIBUTES",
                                     KeyConditionExpression=Key("type").eq(type))["Items"]
        else:
            return self._table.query(IndexName="typeIndex",
                                     Select="ALL_ATTRIBUTES",
                                     KeyConditionExpression=Key("type").eq(type) & Key("id").eq(itemId))["Items"]

    def putItem(self, item):
        print("Writing Item to table")
        print(item)
        self._table.put_item(Item=item)

        # Return the "new" item for convience/confirmation
        return item

    def deleteItem(self, key, sort):
        print("Deleting Item from table")
        print(key, sort)
        self._table.delete_item(Key={
            "key": key,
            "id": sort
        })
