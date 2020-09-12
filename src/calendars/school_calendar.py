import json
from _datetime import datetime

class SchoolCalendar:
    def __init__(self):
        with open('conf/fisd_calendar.json') as f:
            self.fisd_schedule = json.load(f) 
        self.start_date = self.fisd_schedule.get("StartDate")           

    def is_holiday(self, date: datetime):
        if not self.is_in_school_year(date):
            return "School is not in session on {}".format(date.strftime("%b %d"))
        if date.strftime("%A") in ["Saturday", "Sunday"]:
            return "No school on {}".format(date.strftime("%A")) 
        holiday = self.get_holiday_in_list(date.strftime("%m/%d/%Y"))    
        if holiday != None:
            return "NO SCHOOL: {}.".format(holiday.get("name"))
        else:
            return None                      

    def get_holiday_in_list(self, date_string:str):
        holiday_name = next((stat for stat in self.fisd_schedule.get('Holidays') if date_string == stat.get("date")), None)
        return holiday_name

    def is_in_school_year(self, date: datetime):
        school_start = datetime.strptime(self.fisd_schedule.get("StartDate"), "%m/%d/%Y" )
        school_end = datetime.strptime(self.fisd_schedule.get("EndDate"), "%m/%d/%Y" )
        return school_start.date() < date.date() and school_end.date() > date.date()

    def get_term(self, date: datetime):
        term_defs = self.fisd_schedule.get("Nine Weeks")
        current_term = next((term for term in term_defs if date_in_term(date, term)), None)  
        return current_term

def date_in_term(date: datetime, term: dict):
    start_of_term = datetime.strptime(term.get("start"), "%m/%d/%Y" )
    end_of_term = datetime.strptime(term.get("end"), "%m/%d/%Y" )
    if start_of_term.date() < date.date() and end_of_term.date() > date.date():
        return True
    else:
        return False
