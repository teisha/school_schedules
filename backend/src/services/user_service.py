#  create user
#  get user
#  add students
#  deactivate user
import os
import services.dynamodb_service as db
from _datetime  import datetime

service = db.DynamoService(os.environ["DYNAMO_TABLE"])


def get_user(username: str):
    result = service.get_data('USER', username)
    return convert_to_user_object(result)

def save_user(user_data: dict):
    if user_data.get("username") == None :
        return {'statusCode': 400, 'message': "Malformed Request"}
    result = service.put_data(
        pk='USER',
        sk=user_data.get("username"),
        start=user_data.get("email"),    # Index exists on this field
        date_created=datetime.utcnow().isoformat(),
        status='active',
        students=user_data.get("students"),
        firstname=user_data.get("firstname"),                      
        lastname=user_data.get("lastname") 
    )
    print(result)
    message = f'Successfully Saved: {user_data.get("username")}' if result.get('http_status') == 200 else \
        f'An error occurred while saving {user_data.get("username")}'
    return { 'statusCode': result.get("http_status", 500),
        'message': message}


def convert_to_user_object(db_user):     
    return dict(
        username=db_user.get("sk"),
        status=db_user.get("status"),
        firstname=db_user.get("firstname"),
        lastname=db_user.get("lastname"),
        email=db_user.get("start"),
        students=db_user.get("students"),
        date_created=db_user.get("date_created")
    )

def convert_to_db_object(user_data: dict):
    return dict ( 
        pk='USER',
        sk=user_data.get("username"),
        start=user_data.get("email"),    # Index exists on this field
        date_created=datetime.utcnow().isoformat(),
        status='active',
        students=[],
        firstname=user_data.get("firstname"),                      
        lastname=user_data.get("lastname") 
    )
