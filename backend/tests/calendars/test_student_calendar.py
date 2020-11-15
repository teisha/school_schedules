import sys, os
from calendars import student_calendar
from _datetime import datetime

mock_calendar = []
expected_schedule = {'1': {'Class': 'Pre AP English 2', 'Category': 'English', 'StartTime': '08:45', 'StopTime': '09:35'}, 
'2': {'Class': 'AP World History', 'Category': 'Social Studies', 'StartTime': '9:42', 'StopTime': '10:32'}, 
'3': {'Class': 'Chemistry', 'Category': 'Science', 'StartTime': '10:39', 'StopTime': '11:32'}, 
'4': {'Class': 'Small Animal Management', 'Category': 'Elective', 'StartTime': '12:09', 'StopTime': '12:59'}, 
'5': {'Class': 'French 2', 'Category': 'World Language', 'StartTime': '13:06', 'StopTime': '13:56'}, 
'6': {'Class': 'Concert Band 2', 'Category': 'Fine Arts', 'StartTime': '14:03', 'StopTime': '14:54'}, 
'7': {'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53'}, 
'8': {'Class': 'French On Skype', 'Category': 'External Lessons', 'StartTime': '16:00', 'StopTime': '17:00'}} 
os.environ["SCHOOL_TABLE_NAME"] = 'visual-schedules-data-table'


# {'1': {'Class': 'Pre AP English 2', 'Category': 'English', 'StartTime': '08:45', 'StopTime': '09:35'},
#  '2': {'Class': 'AP World History', 'Category': 'Social Studies', 'StartTime': '9:42', 'StopTime': '10:32'},
#  '3': {'Class': 'Pre AP Chemistry', 'Category': 'Science', 'StartTime': '10:39', 'StopTime': '11:32'},
#  '4': {'Class': 'Small Animal Management', 'Category': 'Elective', 'StartTime': '12:09', 'StopTime': '12:59'},
#  '5': {'Class': 'French 2', 'Category': 'World Language', 'StartTime': '13:06', 'StopTime': '13:56'},
#  '6': {'Class': 'Concert Band 2', 'Category': 'Fine Arts', 'StartTime': '14:03', 'StopTime': '14:54'},
#  '7': {'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53'},
#  '8': {'Class': 'French On Skype', 'Category': 'External Lessons', 'StartTime': '16:00', 'StopTime': '17:00'}}

# Run tests from src directory /c/git/school_schedules/backend/src
#  ../venv_linux/bin/python -m pytest -s ../tests/calendars/test_student_calendar.py >> printout.txt
class TestClass:
    cal = student_calendar.StudentCalendar("Kiera", "2020")
    cal.daily_schedule = mock_calendar

    def test_dynamo_call_uses_correct_data(self):
      self.cal.daily_schedule = []
      self.cal.get_dynamo_calendar()
      
      assert self.cal.get_schedule_for_date( datetime.strptime('11/12/2020', '%m/%d/%Y'), "Nine Weeks 2") == \
        expected_schedule

    # def test_week1_wednesday(self):
    #   assert self.cal.get_schedule_for_day(datetime.strptime('11/12/2020', '%m/%d/%Y')) == \
    #     {'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK1|Thursday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'} 


'''
[
{
  'pk': 'KID_SCHEDULE|2020|Kiera', 
  'sk': 'PERIOD|1', 
  'start': '08:45', 
  'end': '09:35', 
  'TERMS|Nine Weeks 4': {'Class': 'Pre AP English 2', 'Category': 'English'}, 
  'TERMS|Nine Weeks 3': {'Class': 'Pre AP English 2', 'Category': 'English'},
  'TERMS|Nine Weeks 2': {'Class': 'Pre AP English 2', 'Category': 'English'},
   TERMS|Nine Weeks 2
  'TERMS|Nine Weeks 1': {'Class': 'Pre AP English 2', 'Category': 'English'},
},
{
  'TERMS|Nine Weeks 4': {'Class': 'AP World History', 'Category': 'Social Studies'}, 'TERMS|Nine Weeks 3': {'Class': 'AP World History', 'Category': 'Social Studies'}, 'sk': 'PERIOD|2', 'TERMS|Nine Weeks 2': {'Class': 'AP World History', 'Category': 'Social Studies'}, 'end': '10:32', 'TERMS|Nine Weeks 1': {'Class': 'AP World History', 'Category': 'Social Studies'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '9:42'}, {'TERMS|Nine Weeks 4': {'Class': 'Pre AP Chemistry', 'Category': 'Science'}, 'TERMS|Nine Weeks 3': {'Class': 'Pre AP Chemistry', 'Category': 'Science'}, 'sk': 'PERIOD|3', 'TERMS|Nine Weeks 2': {'Class': 'Pre AP Chemistry', 'Category': 'Science'}, 'end': '11:32', 'TERMS|Nine Weeks 1': {'Class': 'Pre AP Chemistry', 'Category': 'Science'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '10:39'}, {'TERMS|Nine Weeks 4': {'Class': 'Equine Science', 'Category': 'Elective'}, 'TERMS|Nine Weeks 3': {'Class': 'Equine Science', 'Category': 'Elective'}, 'sk': 'PERIOD|4', 'TERMS|Nine Weeks 2': {'Class': 'Small Animal Management', 'Category': 'Elective'}, 'end': '12:59', 'TERMS|Nine Weeks 1': {'Class': 'Small Animal Management', 'Category': 'Elective'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '12:09'}, {'TERMS|Nine Weeks 4': {'Class': 'French 2', 'Category': 'World Language'}, 'TERMS|Nine Weeks 3': {'Class': 'French 2', 'Category': 'World Language'}, 'sk': 'PERIOD|5', 'TERMS|Nine Weeks 2': {'Class': 'French 2', 'Category': 'World Language'}, 'end': '13:56', 'TERMS|Nine Weeks 1': {'Class': 'French 2', 'Category': 'World Language'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '13:06'}, {'TERMS|Nine Weeks 4': {'Class': 'Concert Band 2', 'Category': 'Fine Arts'}, 'TERMS|Nine Weeks 3': {'Class': 'Concert Band 2', 'Category': 'Fine Arts'}, 'sk': 'PERIOD|6', 'TERMS|Nine Weeks 2': {'Class': 'Concert Band 2', 'Category': 'Fine Arts'}, 'end': '14:54', 'TERMS|Nine Weeks 1': {'Class': 'Concert Band 2', 'Category': 'Fine Arts'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '14:03'}, {'TERMS|Nine Weeks 4': {'Class': 'Pre AP Geometry', 'Category': 'Math'}, 'TERMS|Nine Weeks 3': {'Class': 'Pre AP Geometry', 'Category': 'Math'}, 'sk': 'PERIOD|7', 'TERMS|Nine Weeks 2': {'Class': 'Pre AP Geometry', 'Category': 'Math'}, 'end': '15:53', 'TERMS|Nine Weeks 1': {'Class': 'Pre AP Geometry', 'Category': 'Math'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '15:01'}, 
  
  {'TERMS|Nine Weeks 4': {'Class': 'French On Skype', 'Category': 'External Lessons'}, 'TERMS|Nine Weeks 3': {'Class': 'French On Skype', 'Category': 'External Lessons'}, 'sk': 'PERIOD|8', 'TERMS|Nine Weeks 2': {'Class': 'French On Skype', 'Category': 'External Lessons'}, 'end': '17:00', 'TERMS|Nine Weeks 1': {'Class': 'French On Skype', 'Category': 'External Lessons'}, 'pk': 'KID_SCHEDULE|2020|Kiera', 'start': '16:00'}]
'''

      

