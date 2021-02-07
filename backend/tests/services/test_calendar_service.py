import services.daily_calendar_service as daily
import services.district_calendar_service as district
import services.virtual_calendar_service as virtual
import lambda_scheduler_api as apilambda

# Run tests from src directory /c/git/school_schedules/backend/src
# ../venv_linux/bin/python -m pytest -s ../tests/services/test_calendar_service.py


DailyDbItem={
    'pk':  'KID_SCHEDULE|2020|Kiera',
    'sk':  'PERIOD|1',
    'start':  '08:45',
    'end': '09:35',
    'TERMS|Nine Weeks 1':  {
        'Class': 'Pre AP English 2',
        'Category': 'English'
    },
    'TERMS|Nine Weeks 2':  {
        'Class': 'Pre AP English 2',
        'Category': 'English'
    },
    'TERMS|Nine Weeks 3':  {
        'Class': 'Pre AP English 2',
        'Category': 'English'
    },
    'TERMS|Nine Weeks 4':  {
        'Class': 'Pre AP English 2',
        'Category': 'English'
    },                                    
}

DailyDataItem={
    'student': 'Kiera',
    'year': '2020',
    'period': '1',
    'start_time': '08:45',
    'end_time': '09:35',
    'term': [
        {'term_name': '1', 'class_name':'Pre AP English 2','category_name':'English'},
        {'term_name': '2', 'class_name':'Pre AP English 2','category_name':'English'},
        {'term_name': '3', 'class_name':'Pre AP English 2','category_name':'English'},
        {'term_name': '4', 'class_name':'Pre AP English 2','category_name':'English'},
    ]
}

def test_convert_to_data_item():
    data_item = daily.convert_to_schedule_object(DailyDbItem)
    assert data_item  == DailyDataItem

def test_convert_to_db_item():
    db_item = daily.convert_to_db_object(DailyDataItem)
    assert db_item == DailyDbItem




DistrictDbItem1={
    'pk':  "SCHOOL|2020|FISD",
    'sk':  "SCHEDULE",
    'start':  "08/31/2020",
    'end':  "05/27/2021"
    }  
DistrictDbItem2={
    'pk':  "SCHOOL|2020|FISD",
    'sk':  "HOLIDAY|Labor Day",
    'start':  "09/07/2020"
}

DistrictDataItem1={
    'school': 'FISD',
    'year': '2020',
    'type': "SCHEDULE", 
    'start': "08/31/2020",
    'end': "05/27/2021"
    }  
DistrictDataItem2={
    'school': 'FISD',
    'year': '2020',
    'type': "HOLIDAY",
    'name': 'Labor Day',
    'start': "09/07/2020"
}

def test_convert_to_data_item1():
    data_item = district.convert_to_schedule_object(DistrictDbItem1)
    assert data_item  == DistrictDataItem1
def test_convert_to_data_item2():
    data_item = district.convert_to_schedule_object(DistrictDbItem2)
    assert data_item  == DistrictDataItem2

def test_convert_to_db_item():
    db_item = district.convert_to_db_object(DistrictDataItem1)
    assert db_item == DistrictDbItem1
def test_convert_to_db_item2():
    db_item = district.convert_to_db_object(DistrictDataItem2)
    assert db_item == DistrictDbItem2

VirtualDbItem1={
    'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
    'sk':  "SETTINGS",
    'num_weeks':  1,
    }
VirtualDbItem2={
    'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
    'sk':  "WEEK1|Monday",
    'sync':  ["Math", "Social Studies", "English", "Elective"],
    'async': [ "World Language", "Science", "PE", "Fine Arts"]
    }

VirtualDataItem1={
    'student': 'Kiera',
    'year': '2020',
    'day': 'SETTINGS',
    'num_weeks': 1
}
VirtualDataItem2={
    'student': 'Kiera',
    'year': '2020',
    'day': 'Monday',
    'num_weeks': 1,
    'sync_categories': ["Math", "Social Studies", "English", "Elective"],
    'async_categories': [ "World Language", "Science", "PE", "Fine Arts"]
}    

def test_convert_to_data_item1():
    data_item = virtual.convert_to_schedule_object(VirtualDbItem1)
    assert data_item  == VirtualDataItem1
def test_convert_to_data_item2():
    data_item = virtual.convert_to_schedule_object(VirtualDbItem2)
    assert data_item  == VirtualDataItem2

def test_convert_to_db_item():
    db_item = virtual.convert_to_db_object(VirtualDataItem1)
    assert db_item == VirtualDbItem1
def test_convert_to_db_item2():
    db_item = virtual.convert_to_db_object(VirtualDataItem2)
    assert db_item == VirtualDbItem2


def test_schedule_lambda(get_db):
    service = get_db
    body = {
        'kidname': 'Kiera',
        'year': '2020',
        'district': 'FISD'
    }
    schedule = apilambda.get_full_calendar(body)
    print(body)

    print(schedule)
    assert schedule != None
