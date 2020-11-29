#  create user
#  get user
#  add students
#  deactivate user
import dynamo_service as db

service = db.DynamodbService(os.environ["DYNAMO_TABLE"])

def create_user(user_data: dict):

    Item={
            'pk':  user_data,
            'sk':  "PERIOD|1",
            'start':  "08:45",
            'end': "09:35",
                                               
        }