import services.user_service as userv

class MockDynamo:
    def __init__ (self, name: str):
        self.table_name = "mock_%s" % name
    def put_data(self, pk: str, sk: str, **attributes):
        return dict(statusCode=200,message='')
    def get_data(self, pk: str, sk: str):
        return dict()

# lambda_get_schedule.Calculator = MockCalculator
# Run tests from src directory /c/git/school_schedules/backend/src
# ../venv_linux/bin/python -m pytest -s ../tests/services/test_user_service.py

test_user = dict(username="laimaB",email="ahsiet4@yahoo.com",firstname="Laima")

def test_save_data_without_key_returns_400():
    result = userv.save_user( dict() )
    print(result)
    assert result == {'statusCode': 400, 'message': "Malformed Request"}

def test_save_data_successfully(get_db):
    service = get_db
    result = userv.save_user( test_user )
    print(result)
    assert result == {'statusCode': 200, 'message': 'Successfully Saved: laimaB'}   

    pk= 'USER'
    sk=test_user.get("username")

    actual_user = service.get_data(pk, sk)
    assert actual_user.get('pk') == 'USER'
    assert actual_user.get('sk') == test_user.get("username")
    assert actual_user.get('start') == test_user.get("email")
    assert actual_user.get('status') == 'active'
    assert actual_user.get('students') == []
    assert actual_user.get('firstname') == test_user.get("firstname")
    assert actual_user.get('lastname') == None


