import lambda_scheduler_api
import json
from services import virtual_calendar_service

# Run tests from src directory /c/git/school_schedules/backend/src
# ../venv_linux/bin/python -m pytest -s ../tests/lambdas/test_lambda_scheduler_api.py

def test_get_schedule():
    username = 'laimaB'
    mock_event = {
        "resource": "/scheduler",
        "httpMethod": "POST",
        "body":json.dumps( {
            "data" :  {'kidname': 'Kiera', 'year': '2020', 'district': 'FISD'} 
        } )
    }
    response = lambda_scheduler_api.schedule_router(mock_event)
    print (f"RESPONSE: {response}")
    assert response.get("statusCode") == 200
    full_schedule = json.loads(response.get("body") ) 
    print (f"ACTUAL SCHEDULE: {full_schedule}")
    print (type(full_schedule))
    assert full_schedule.get("district") != None
    assert len(full_schedule.get("district")) == 32
    assert full_schedule.get("virtual") != None
    assert len(full_schedule.get("virtual")) == 11
    assert full_schedule.get("daily") != None
    assert len(full_schedule.get("daily")) == 8


def test_convert_virtual_schedule():
    schedule = { 
        "student":"Kiera",
        "year":"2020",
        "num_weeks":"1",
        "day":"Friday",
        "sync_categories":["English","Math","Elective"],
        "async_categories":["Science","Social Studies","PE","Fine Arts","World Language"]
    }    
    converted_service = virtual_calendar_service.convert_to_db_object(schedule)
    assert converted_service.get('pk') == "VIRTUAL_SCHEDULE|2020|Kiera"
    assert converted_service.get('sk') == "WEEK1|Friday"
    assert converted_service.get('sync') == ["English","Math","Elective"]
    assert converted_service.get('async') == ["Science","Social Studies","PE","Fine Arts","World Language"]


def test_save_virtual_schedule():
    body= {'schedule': {'student': 'Delia', 'year': '2020', 'num_weeks': '1', 'day': 'Tuesday', 'sync_categories': ['Quest', 'OTPT-Speech', 'Calendar'], 'async_categories': ['PE']}}
    result=lambda_scheduler_api.save_virtual_calendar(body)
    assert result.get("statusCode") == 200

def test_convert_json() :
    json_val = [
        {'school': 'FISD', 'year': '2020', 'type': 'EARLY_DISMISSAL', 'start': '12/18/2020', 'name': '1'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'EARLY_DISMISSAL', 'start': '05/27/2021', 'name': '2'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '04/02/2021', 'name': 'Good Friday'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '09/07/2020', 'name': 'Labor Day'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '01/18/2021', 'name': 'Martin Luther King Jr Day'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '03/15/2021', 'name': 'Spring Break Day 1'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '03/16/2021', 'name': 'Spring Break Day 2'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '03/17/2021', 'name': 'Spring Break Day 3'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '03/18/2021', 'name': 'Spring Break Day 4'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '03/19/2021', 'name': 'Spring Break Day 5'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '10/12/2020', 'name': 'Teacher Professional Day 1'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '02/15/2021', 'name': 'Teacher Professional Day 2'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '11/23/2020', 'name': 'Thanksgiving Break Day 1'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '11/24/2020', 'name': 'Thanksgiving Break Day 2'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '11/25/2020', 'name': 'Thanksgiving Break Day 3'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '11/27/2020', 'name': 'Thanksgiving Break Day 5'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '11/26/2020', 'name': 'Thanksgiving Day'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/21/2020', 'name': 'Winter Break Day 1'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '01/01/2021', 'name': 'Winter Break Day 10'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/22/2020', 'name': 'Winter Break Day 2'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/23/2020', 'name': 'Winter Break Day 3'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/24/2020', 'name': 'Winter Break Day 4'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/25/2020', 'name': 'Winter Break Day 5'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/28/2020', 'name': 'Winter Break Day 6'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/29/2020', 'name': 'Winter Break Day 7'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/30/2020', 'name': 'Winter Break Day 8'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'HOLIDAY', 'start': '12/31/2020', 'name': 'Winter Break Day 9'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'SCHEDULE', 'start': '08/31/2020', 'end': '05/27/2021'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'TERMS', 'start': '08/31/2020', 'end': '10/16/2020', 'name': 'Nine Weeks 1'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'TERMS', 'start': '10/19/2020', 'end': '12/18/2020', 'name': 'Nine Weeks 2'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'TERMS', 'start': '01/04/2021', 'end': '03/12/2021', 'name': 'Nine Weeks 3'}, 
        {'school': 'FISD', 'year': '2020', 'type': 'TERMS', 'start': '03/22/2021', 'end': '05/27/2021', 'name': 'Nine Weeks 4'}
        ]
    converted_json = json.dumps(json_val)        
    assert len(json_val) == 32

