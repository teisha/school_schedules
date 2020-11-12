import boto3
import botocore.session
from boto3.dynamodb.conditions import Key

# dynamodb = session.resource('dynamodb' )
dynamodb = boto3.resource("dynamodb")
# tableName = 'visual-schedules-data-table'

class DynamoService:
    def __init__(self, tableName: str):
        self._table = dynamodb.Table(tableName)
        print("Querying {}".format(self._table.table_name) )

    def get_data(self, pk: str, sk: str):
        print("Query for pk:{} sk:{}".format(pk, sk))            
        data = self._table.get_item( Key = { 'pk': pk, 'sk': sk })
        return data.get('Item', None)

    def put_data(self, pk: str, sk: str, **attributes):
        item = {
            'pk': pk,
            'sk': sk
        }
        for param, value in attributes.items():
            item.update({param: value}) 
        print("Add to dynamo:  item:{}".format(item))
        self._table.put_item(Item=item)

    def delete_data(self, pk: str, sk: str):
        self._table.delete_item( Key = { 'pk': pk, 'sk': sk })

    def queryOnPrimaryKey(self, key):
        return self._table.query(
            KeyConditionExpression=Key("pk").eq(key)
        )["Items"]        
