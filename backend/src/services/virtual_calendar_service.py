

import os
import services.dynamodb_service as db
from _datetime  import datetime

service = db.DynamoService(os.environ["DYNAMO_TABLE"])


def get_virtual_calendar(year: str, kid: str):
    pk = "|".join([ 'VIRTUAL_SCHEDULE', year, kid ])
    result = service.queryOnPrimaryKey(pk)
    return  list(map(lambda x: convert_to_schedule_object(x) , result  ) )


def save_calendar(virtual_calendar: dict):
    if not is_valid(virtual_calendar):
        return {
            'statusCode': 400, 
            'message': "Malformed Request"
        }
    db_object = convert_to_db_object(virtual_calendar)
    result = service.put_data(db_object.get('pk'), db_object.get('sk'), 
        **{'sync':db_object.get('sync'), 'async': db_object.get('async')} ) 
    print(result)
    message = f'Successfully Saved: {virtual_calendar.get("student")} virtual calendar' if result.get('http_status') == 200 else \
        f'An error occurred while saving {virtual_calendar.get("student")} virtual calendar'
    return { 'statusCode': result.get("http_status", 500),
        'message': message}   


def is_valid(schedule: str):
    valid: bool = True
    if schedule.get("student", None) == None or \
        schedule.get("year", None) == None:
        valid=False
    return valid

def convert_to_schedule_object(schedule_data: dict): 
    pk = schedule_data.get("pk").split("|")
    sk = schedule_data.get("sk").split("|")
    data = dict(
        student=pk[2],
        year=pk[1],
        num_weeks= sk[0].replace('WEEK','') if len(sk)> 1 else str(schedule_data.get("num_weeks") ),
        day=sk[1] if len(sk)> 1 else 'SETTINGS',
    )
    if schedule_data.get('sk', 'SETTINGS') != 'SETTINGS':
        data.update({ 'sync_categories': schedule_data.get("sync") }),
        data.update({ 'async_categories': schedule_data.get("async") })
    return data    

def convert_to_db_object(schedule_data: dict):
    sk = "|".join(["".join(['WEEK', str(schedule_data.get("num_weeks"))]), schedule_data.get("day")]) if \
        schedule_data.get("day", None) != 'SETTINGS' else 'SETTINGS'
    db_object = dict ( 
        pk="|".join(["VIRTUAL_SCHEDULE", schedule_data.get("year"), schedule_data.get("student")]),
        sk=sk
        # **{'async':schedule_data.get("async_categories")}
    )   
    if schedule_data.get("day", None) == 'SETTINGS':
        db_object.update( num_weeks=schedule_data.get("num_weeks"))
    else:
        db_object.update({ 'sync': schedule_data.get("sync_categories") })   
        db_object.update({ 'async':schedule_data.get("async_categories") })
    print(db_object)        
    return db_object