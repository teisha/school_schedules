import sys, os
from calendars import virtual_calendar
from _datetime import datetime

mock_calendar = [{'pk': 'VIRTUAL_SCHEDULE|2020|Kiera', 'sk': 'SETTINGS', 'num_weeks':2}, 
{'sync': ['Math', 'Social Studies', 'World Language', 'Fine Arts'], 'sk': 'WEEK1|Monday', 'async': ['English', 'Science', 'Elective', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['English', 'Science', 'Elective', 'External Lessons'], 'sk': 'WEEK1|Tuesday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['Math', 'Social Studies', 'World Language', 'Fine Arts'], 'sk': 'WEEK1|Wednesday', 'async': ['English', 'Science', 'Elective', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK1|Thursday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['Math', 'Social Studies', 'World Language', 'Fine Arts'], 'sk': 'WEEK1|Friday', 'async': ['English', 'Science', 'Elective', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 

{'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK2|Monday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'External Lessons'], 'sk': 'WEEK2|Tuesday', 'async': ['English', 'Science', 'Elective', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK2|Wednesday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}]
{'sync': ['Math', 'Social Studies', 'World Language', 'Fine Arts'], 'sk': 'WEEK2|Thursday', 'async': ['English', 'Science', 'Elective', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 
{'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK2|Friday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}, 

expected_schedule = {'1': {'Class': 'Pre AP English 2', 'Category': 'English', 'StartTime': '08:45', 'StopTime': '09:35', 'virtual_option': 'SYNCHRONOUS', 'has_class': True}, 
  '2': {'Class': 'AP World History', 'Category': 'Social Studies', 'StartTime': '9:42', 'StopTime': '10:32', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, 
  '3': {'Class': 'Pre AP Chemistry', 'Category': 'Science', 'StartTime': '10:39', 'StopTime': '11:32', 'virtual_option': 'SYNCHRONOUS', 'has_class': True}, 
  '4': {'Class': 'Small Animal Management', 'Category': 'Elective', 'StartTime': '12:09', 'StopTime': '12:59', 'virtual_option': 'SYNCHRONOUS', 'has_class': True}, 
  '5': {'Class': 'French 2', 'Category': 'World Language', 'StartTime': '13:06', 'StopTime': '13:56', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, 
  '6': {'Class': 'Concert Band 2', 'Category': 'Fine Arts', 'StartTime': '14:03', 'StopTime': '14:54', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, 
  '7': {'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, 
  '8': {'Class': 'French On Skype', 'Category': 'External Lessons', 'StartTime': '16:00', 'EndTime': '17:00', 'has_class': False}}

os.environ["SCHOOL_TABLE_NAME"] = 'visual-schedules-data-table'

# Run tests from src directory /c/git/school_schedules/backend/src
#  ../venv_linux/bin/python -m pytest -s ../tests/calendars/test_virtual_calendar.py >> printout.txt

cal = virtual_calendar.VirtualCalendar("Kiera", "2020")
cal.virtual_schedule = mock_calendar

def test_dynamo_call_uses_correct_data():
  cal.virtual_schedule = []
  cal.get_dynamo_calendar("08/31/2020")
  assert cal.virtual_schedule.count({
        'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
        'sk':  "SETTINGS",
        'num_weeks':  2,
        }) == 1
  assert cal.start_date == datetime.strptime("08/31/2020", "%m/%d/%Y")
  assert cal.week_one == 35
  assert cal.weeks_in_rotation == 2   

  schedule = {'1': {'Class': 'Pre AP English 2', 'Category': 'English', 'StartTime': '08:45', 'StopTime': '09:35'}, '2': {'Class': 'AP World History', 'Category': 'Social Studies', 'StartTime': '9:42', 'StopTime': '10:32'}, '3': {'Class': 'Pre AP Chemistry', 'Category': 'Science', 'StartTime': '10:39', 'StopTime': '11:32'}, '4': {'Class': 'Small Animal Management', 'Category': 'Elective', 'StartTime': '12:09', 'StopTime': '12:59'}, '5': {'Class': 'French 2', 'Category': 'World Language', 'StartTime': '13:06', 'StopTime': '13:56'}, '6': {'Class': 'Concert Band 2', 'Category': 'Fine Arts', 'StartTime': '14:03', 'StopTime': '14:54'}, '7': {'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53'}, '8': {'Class': 'French On Skype', 'Category': 'External Lessons', 'StartTime': '16:00', 'EndTime': '17:00'}} 
  assert cal.add_virtual_week_to_schedule( datetime.strptime('11/12/2020', '%m/%d/%Y'), schedule) == \
    expected_schedule

def test_week1_wednesday():
  assert cal.get_schedule_for_day(datetime.strptime('11/12/2020', '%m/%d/%Y')) == \
    {'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK1|Thursday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'} 




      

