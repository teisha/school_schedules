

import os
import services.dynamodb_service as db
from _datetime  import datetime

service = db.DynamoService(os.environ["DYNAMO_TABLE"])


def get_daily_calendar(year: str, kid: str):
    pk = "|".join([ 'KID_SCHEDULE', year, kid ])
    result = service.queryOnPrimaryKey(pk)
    return  list(map(lambda x: convert_to_schedule_object(x) , result  ) )


def save_calendar(virtual_calendar: dict):
    if not is_valid(virtual_calendar):
        return {
            'statusCode': 400, 
            'message': "Malformed Request"
        }
    result = service.put_data(convert_to_db_object(virtual_calendar)) 
    print(result)
    message = f'Successfully Saved: {virtual_calendar.get("student")} daily calendar' if result.get('http_status') == 200 else \
        f'An error occurred while saving {virtual_calendar.get("student")} daily calendar'
    return { 'statusCode': result.get("http_status", 500),
        'message': message}   


def is_valid(schedule: str):
    valid: bool = True
    if schedule.get("student", None) == None or \
        schedule.get("year", None) == None:
        valid=False
    return valid

def get_class_info(class_name: str, class_data: dict):
    return dict(
        term_name=class_name.replace('TERMS|Nine Weeks ', ''),
        class_name=class_data.get('Class'),
        category_name=class_data.get('Category')
    )

def convert_to_schedule_object(schedule_data: dict): 
    pk = schedule_data.get("pk").split("|")
    sk = schedule_data.get("sk").split("|")
    class_list =[get_class_info(key_name, schedule_data[key_name]) for key_name in schedule_data.keys() if key_name.startswith('TERMS|') ]
    return dict(
        student=pk[2],
        year=pk[1],
        period=sk[1],
        start_time=schedule_data.get("start"),
        end_time=schedule_data.get("end"),
        term=class_list
    )

def convert_to_db_object(schedule_data: dict):
    schedule_object = dict ( 
        pk="|".join(["KID_SCHEDULE", schedule_data.get("year"), schedule_data.get("student")]),
        sk="|".join(["PERIOD", schedule_data.get("period")]),
        start=schedule_data.get("start_time"),
        end=schedule_data.get("end_time"),
    )   
    for term in schedule_data.get('term'):
        term_name = "".join(["TERMS|Nine Weeks ", term.get('term_name')])
        description = dict(
            Class=term.get('class_name'),
            Category=term.get('category_name')
        )
        schedule_object.update({ term_name : description })
    return schedule_object



