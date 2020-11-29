#  create user
#  get user
#  add students
#  deactivate user
import os
import services.dynamodb_service as db
from _datetime  import datetime

service = db.DynamoService(os.environ["DYNAMO_TABLE"])


def get_user(username: str, email: str):
    return service.get_user(f'USER|{username}', email)

def save_user(user_data: dict):
    if user_data.get("username") == None or user_data.get("email") == None:
        return {'statusCode': 400, 'message': "Malformed Request"}
    
    result = service.put_data( 
        pk=f'USER|{user_data.get("username")}',
        sk=user_data.get("email"),
        start=datetime.utcnow().isoformat(),
        status='active',
        students=[],
        firstname=user_data.get("firstname"),                      
        lastname=user_data.get("lastname") 
    )
    print(result)
    message = f'Successfully Saved: {user_data.get("username")}' if result.get('http_status') == 200 else \
        f'An error occurred while saving {user_data.get("username")}'
    return { 'statusCode': result.get("http_status", 500),
        'message': message}


     