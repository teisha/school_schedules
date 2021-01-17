from _datetime import datetime
import pytest, os
from schedule_calculator import Calculator
os.environ["LOGGING_LEVEL"] ="DEBUG"
import alexa_get_schedule as lambda_get_schedule

class MockCalculator:
    def __init__ (self, name: str):
        self.name = "mock_%s" % name
    def is_there_school(self, day: datetime):
        return dict(schedule={'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True},
            name=self.name, message=None)

lambda_get_schedule.Calculator = MockCalculator
# @pytest.fixture()
# def mock_calendar (monkeypatch):
#     monkeypatch.settattr(Calendar, "", MockCalculator)


def test_get_schedule():
    student = "Kiera"
    schedule_date= '11/12/2020'
    expected_schedule ={'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}

    returned = lambda_get_schedule.getSchoolSchedule(student, schedule_date)
    print(returned)
    assert returned.get("message") == None
    assert returned.get("name") == "mock_Kiera" 
    assert returned.get("schedule") == expected_schedule


'''
Generating schedule for  Wednesday, 09. September 2020 12:00AM
Schedule for TERM:  Nine Weeks 1
{'sync': ['English', 'Science', 'Elective'], 'sk': 'WEEK2|Wednesday', 'async': ['Math', 'Social Studies', 'World Language', 'Fine Arts', 'PE'], 'pk': 'VIRTUAL_SCHEDULE|2020|Kiera'}
{'schedule': {'1': {'Class': 'Pre AP English 2', 'Category': 'English', 'StartTime': '08:45', 'StopTime': '09:35', 'virtual_option': 'SYNCHRONOUS', 'has_class': True}, '2': {'Class': 'AP World History', 'Category': 'Social Studies', 'StartTime': '9:42', 'StopTime': '10:32', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, '3': {'Class': 'Chemistry', 'Category': 'Science', 'StartTime': '10:39', 'StopTime': '11:32', 'virtual_option': 'SYNCHRONOUS', 'has_class': True}, '4': {'Class': 'Small Animal Management', 'Category': 'Elective', 'StartTime': '12:09', 'StopTime': '12:59', 'virtual_option': 'SYNCHRONOUS', 'has_class': True}, '5': {'Class': 'French 2', 'Category': 'World Language', 'StartTime': '13:06', 'StopTime': '13:56', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, '6': {'Class': 'Concert Band 2', 'Category': 'Fine Arts', 'StartTime': '14:03', 'StopTime': '14:54', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, '7': {'Class': 'Pre AP Geometry', 'Category': 'Math', 'StartTime': '15:01', 'StopTime': '15:53', 'virtual_option': 'ASYNCHRONOUS', 'has_class': True}, '8': {'Class': 'French On Skype', 'Category': 'External Lessons', 'StartTime': '16:00', 'StopTime': '17:00', 'has_class': False}}, 'message': None, 'name': 'Kiera'}
'''    