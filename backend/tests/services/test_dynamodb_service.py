import sys , os
print(sys.path)
from src.services.dynamodb_service import DynamoService
import boto3
session = boto3.session.Session(profile_name='power-user')

test_item = {
    'pk': "IAMATEST|ITEM",
    'sk': "DESCRIBES|NOTHING",
    'start': '10/1/2001',
    'end': '12/12/2012',
    'databit': 'empty'
}

item={
    'pk':  "KID_SCHEDULE|2020|Delia",
    'sk':  "PERIOD|8",
    'start':  "15:11",
    'end': "15:55"
}
# python -m pytest -s tests/services/test_dynamodb_service.py >> printout.txt
class TestDynamoService:
    table_name = 'visual-schedules-data-table'
    service = DynamoService(table_name)

    def test_get_data(self):
        actual_item = self.service.get_data('KID_SCHEDULE|2020|Delia', 'PERIOD|8')
        # runThis = galvestonCounty.GalvestonCountyRunner()
        # runThis.get_friendswood_detail()
        # print ('Gathering Friendswood Data')
        print(actual_item)
        assert actual_item == item           

    def test_put_data(self):
        pk = test_item.get('pk')
        sk = test_item.get('sk')
        self.service.delete_data(pk, sk)
        assert self.service.get_data(pk, sk) == None

        self.service.put_data(pk, sk, start='10/1/2001', end='12/12/2012', databit='empty')
        assert self.service.get_data(pk, sk) == test_item