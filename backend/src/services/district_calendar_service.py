

import os
import services.dynamodb_service as db
from _datetime  import datetime

service = db.DynamoService(os.environ["DYNAMO_TABLE"])

def get_district_from_key(keyRecord: str):
    # Expects format: 'pk':  "SCHOOL|2020|FISD",
    pk = schedule_user.get("pk").split("|")
    return pk[2] if len(pk) > 2 else ""

def get_districts():
    result = service.queryOnSortKey('SCHEDULE')
    # 'pk':  "SCHOOL|2020|FISD",
    # 'sk':  "SCHEDULE",
    return [get_district_from_key(keyRec) for keyRec in result]

def get_district_calendar(year: str, district_name: str):
    print (f"Get District Calendar for year: {year} and district: {district_name}")
    pk = "|".join([ 'SCHOOL', year, district_name ])
    result = service.queryOnPrimaryKey(pk)
    return  list(map(lambda x: convert_to_schedule_object(x) , result  )  ) #result is a list


def save_calendar(district_calendar: dict):
    if not is_valid(district_calendar):
        return {
            'statusCode': 400, 
            'message': "Malformed Request"
        }
    result = service.put_data(convert_to_db_object(district_calendar)) 
    print(result)
    message = f'Successfully Saved: {district_calendar.get("school")} calendar' if result.get('http_status') == 200 else \
        f'An error occurred while saving {district_calendar.get("school")} calendar'
    return { 'statusCode': result.get("http_status", 500),
        'message': message}   


def is_valid(schedule: str):
    valid: bool = True
    if schedule.get("schoool", None) == None or \
        schedule.get("year", None) == None:
        valid=False
    return valid

def convert_to_schedule_object(schedule_data: dict): 
    pk = schedule_data.get("pk").split("|")
    sk = schedule_data.get("sk").split("|")
    data = dict(
        school=pk[2],
        year=pk[1],
        type=sk[0],
        start=schedule_data.get("start"),
    )
    if schedule_data.get("end", None) != None:
        data.update({ 'end': schedule_data.get("end") })
    if len(sk)> 1:
        data.update({ 'name':sk[1] })
    return data    

def convert_to_db_object(schedule_data: dict):
    sk = "|".join([schedule_data.get("type"), schedule_data.get("name")]) if \
        schedule_data.get("name", None) != None else 'SCHEDULE'
    data = dict ( 
        pk="|".join(["SCHOOL", schedule_data.get("year"), schedule_data.get("school")]),
        sk=sk,
        start=schedule_data.get("start"),    # Index exists on this field
    )   
    if schedule_data.get("end", None) != None:
        data.update({ 'end': schedule_data.get("end") })
    return data