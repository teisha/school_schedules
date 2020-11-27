import pytest
import bcrypt
from _datetime import datetime
import lambda_authenticate as la

# don't need backend - use Cognito service

FAKE_HASH = b'$2b$12$mwSIOyxLJid1jFLgnU0s0.'
def sub_hashpw(password, salt):
    return FAKE_HASH
@pytest.fixture()
def patch_hashpw(monkeypatch):
    monkeypatch.setattr(bcrypt, 'hashpw', sub_hashpw)            


# FAKE_TIME = datetime.datetime(2020, 12, 25, 17, 5, 55)
# @pytest.fixture
# def patch_datetime_now(monkeypatch):
#     class mydatetime:
#         @classmethod
#         def now(cls):
#             return FAKE_TIME
#         @classmethod
#         def utcnow(cls):
#             return FAKE_TIME
#     monkeypatch.setattr(datetime, 'datetime', mydatetime)
# E           botocore.exceptions.ClientError: An error occurred (InvalidSignatureException) when calling the DeleteItem operation: Signature not yet current: 20201226T000000Z is still later than 20201122T215827Z (20201122T214327Z + 15 min.)

# Run tests from src directory /c/git/school_schedules/backend/src
# python -m pytest -s tests/test_authenticate_api.py >> printout.txt
# @freeze_time("Dec 26th, 2020")

username = 'mock_user'
password = 'mock_password'

def test_create_new_user(get_db, patch_hashpw):
    service = get_db
    service.delete_data('USER', username)
    assert service.get_data('USER', username) == None

    response = la.create_user(username, password)

    assert response.get("success") == True
    expected_lifecycle = datetime.now().strftime("%Y-%b-%d")
    assert service.get_data('USER', username) == {
        'pk':"USER", 
        'sk': username, 
        'start':"Active",
        'password':"$2b$12$mwSIOyxLJid1jFLgnU0s0.",
        'lifecycle': {'created' : f"{expected_lifecycle}" },
        'is_active':True,
        'kids':[f"{username}"]
    }
        
def test_login_successful(get_db):
    service = get_db
    service.delete_data('USER', username)
    la.create_user(username, password)
    response = la.login(username, password)

    assert response.get("success") == True
    assert response.get("message") == None

def test_login_user_doesnt_exist(get_db):
    service = get_db
    service.delete_data('USER', username)
    response = la.login(username, password)

    assert response.get("success") == False
    assert response.get("message") == "No Data Found"
    assert  la.authenticate_session(username, password) == None

def test_login_bad_password(get_db):
    bad_password = "bad password"
    service = get_db
    service.delete_data('USER', username)
    la.create_user(username, password)
    response = la.login(username, bad_password)

    assert response.get("success") == False
    assert response.get("message") == "Passwords Not Matched"
    assert  la.authenticate_session(username, bad_password) == None


def test_authenticate_and_issue_token(get_db):
    service = get_db
    service.delete_data('USER', username)
    la.create_user(username, password)

    resp_token = la.authenticate_session(username, password)
    assert resp_token != None
    assert resp_token.get("token") != None


def delete_user(username: str):
    service.delete_data('USER', username)

def add_user_to_db(username: str, password: str):
    item={
        'start':  "",
        'password': encrypted_password,
        'is_active': True,
        'kids': ['Kiera','Delia']
    }
    service.put_data('USER', username, item)
