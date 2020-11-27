import sys , os
print(sys.path)


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

# Run tests from src directory /c/git/school_schedules/backend/src
# python -m pytest -s tests/services/test_dynamodb_service.py >> printout.txt
class TestDynamoService:

    def test_get_data(self, get_db):
        self.service = get_db
        actual_item = self.service.get_data('KID_SCHEDULE|2020|Delia', 'PERIOD|8')
        # runThis = galvestonCounty.GalvestonCountyRunner()
        # runThis.get_friendswood_detail()
        # print ('Gathering Friendswood Data')
        print(actual_item)
        assert actual_item == item           

    def test_put_data(self, get_db):
        self.service = get_db
        pk = test_item.get('pk')
        sk = test_item.get('sk')
        self.service.delete_data(pk, sk)
        assert self.service.get_data(pk, sk) == None

        self.service.put_data(pk, sk, start='10/1/2001', end='12/12/2012', databit='empty')
        assert self.service.get_data(pk, sk) == test_item