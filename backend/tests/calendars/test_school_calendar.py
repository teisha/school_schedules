import sys, os
from src.calendars import school_calendar
from _datetime import datetime

os.environ["SCHOOL_TABLE_NAME"] = 'visual-schedules-data-table'


#  venv_linux/bin/python -m pytest -s tests/calendars/test_school_calendar.py >> printout.txt
class TestClass:
    cal = school_calendar.SchoolCalendar("FISD")
    cal.get_dynamo_calendar()

    def test_get_data(self):
      # print(cal.fisd_schedule)
      assert self.cal.fisd_schedule.count({'sk': 'SCHEDULE', 'end': '05/27/2021', 'pk': 'SCHOOL|2020|FISD', 'start': '08/31/2020'}) == 1

    def test_is_date_holiday(self):
      good_friday = datetime.strptime('04/02/2021', '%m/%d/%Y')
      assert self.cal.is_date_holiday(good_friday) == True
      

'''
{'StartDate': '08/31/2020', 'EndDate': '05/27/2021', 'Holidays': [{'name': 'Labor Day', 'date': '09/07/2020'}, {'name': 'Teacher Professional Day 1', 'date': '10/12/2020'}, {'name': 'Thanksgiving Break Day 1', 'date': '11/23/2020'}, {'name': 'Thanksgiving Break Day 2', 'date': '11/24/2020'}, {'name': 'Thanksgiving Break Day 3', 'date': '11/25/2020'}, {'name': 'Thanksgiving Day', 'date': '11/26/2020'}, {'name': 'Thanksgiving Break Day 5', 'date': '11/27/2020'}, {'name': 'Winter Break Day 1', 'date': '12/21/2020'}, {'name': 'Winter Break Day 2', 'date': '12/22/2020'}, {'name': 'Winter Break Day 3', 'date': '12/23/2020'}, {'name': 'Winter Break Day 4', 'date': '12/24/2020'}, {'name': 'Winter Break Day 5', 'date': '12/25/2020'}, {'name': 'Winter Break Day 6', 'date': '12/28/2020'}, {'name': 'Winter Break Day 7', 'date': '12/29/2020'}, {'name': 'Winter Break Day 8', 'date': '12/30/2020'}, {'name': 'Winter Break Day 9', 'date': '12/31/2020'}, {'name': 'Winter Break Day 10', 'date': '01/01/2021'}, {'name': 'Martin Luther King Jr Day', 'date': '01/18/2021'}, {'name': 'Teacher Professional Day 2', 'date': '02/15/2020'}, {'name': 'Spring Break Day 1', 'date': '03/15/2021'}, {'name': 'Spring Break Day 2', 'date': '03/16/2021'}, {'name': 'Spring Break Day 3', 'date': '03/17/2021'}, {'name': 'Spring Break Day 4', 'date': '03/18/2021'}, {'name': 'Spring Break Day 5', 'date': '03/19/2021'}, {'name': 'Good Friday', 'date': '04/02/2021'}], 'Early Dismissals': [{'date': '12/18/2020'}, {'date': '05/27/2021'}], 'Nine Weeks': [{'name': 'TERM1', 'start': '08/31/2020', 'end': '10/16/2020'}, {'name': 'TERM2', 'start': '10/19/2020', 'end': '12/18/2020'}, {'name': 'TERM3', 'start': '01/04/2021', 'end': '03/12/2021'}, {'name': 'TERM4', 'start': '03/22/2021', 'end': '05/27/2021'}]}
Querying visual-schedules-data-table
[{'pk': 'SCHOOL|2020|FISD', 'sk': 'EARLY_DISMISSAL|1', 'start': '12/18/2020'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'EARLY_DISMISSAL|2', 'start': '05/27/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Good Friday', 'start': '04/02/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Labor Day', 'start': '09/07/2020'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Martin Luther King Jr Day', 'start': '01/18/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Spring Break Day 1', 'start': '03/15/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Spring Break Day 2', 'start': '03/16/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Spring Break Day 3', 'start': '03/17/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Spring Break Day 4', 'start': '03/18/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Spring Break Day 5', 'start': '03/19/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Teacher Professional Day 1', 'start': '10/12/2020'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Teacher Professional Day 2', 'start': '02/15/2021'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Thanksgiving Break Day 1', 'start': '11/23/2020'}, 
{'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Thanksgiving Break Day 2', 'start': '11/24/2020'},
 {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Thanksgiving Break Day 3', 'start': '11/25/2020'}, 
 {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Thanksgiving Break Day 5', 'start': '11/27/2020'},
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Thanksgiving Day', 'start': '11/26/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 1', 'start': '12/21/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 10', 'start': '01/01/2021'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 2', 'start': '12/22/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 3', 'start': '12/23/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 4', 'start': '12/24/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 5', 'start': '12/25/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 6', 'start': '12/28/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 7', 'start': '12/29/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 8', 'start': '12/30/2020'}, 
  {'pk': 'SCHOOL|2020|FISD', 'sk': 'HOLIDAY|Winter Break Day 9', 'start': '12/31/2020'}, 
  {'sk': 'SCHEDULE', 'end': '05/27/2021', 'pk': 'SCHOOL|2020|FISD', 'start': '08/31/2020'}, 
{'sk': 'TERMS|Nine Weeks 1', 'end': '10/16/2020', 'pk': 'SCHOOL|2020|FISD', 'start': '08/31/2020'}, 
{'sk': 'TERMS|Nine Weeks 2', 'end': '12/18/2020', 'pk': 'SCHOOL|2020|FISD', 'start': '10/19/2020'}, 
{'sk': 'TERMS|Nine Weeks 3', 'end': '03/12/2021', 'pk': 'SCHOOL|2020|FISD', 'start': '01/04/2021'}, 
{'sk': 'TERMS|Nine Weeks 4', 'end': '05/27/2021', 'pk': 'SCHOOL|2020|FISD', 'start': '03/22/2021'}]
'''