import json
from _datetime import datetime
from contextlib import suppress
import sys, os
print(sys.path)
from services.dynamodb_service import DynamoService

class SchoolCalendar:
    fisd_schedule = dict()
    def __init__(self, school: str, yearStr: str):
        self.yearStr = yearStr
        self.school_name = school
        with suppress(FileNotFoundError):
            with open('calendars/config/fisd_calendar.json') as f:
                self.fisd_schedule = json.load(f) 
        self.start_date = self.fisd_schedule.get("StartDate")
        # print(self.fisd_schedule)           

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

    '''
        ~~~~~~~~ DYNAMO IMPLEMENTATION ~~~~~~~~~~
    '''        

    def get_dynamo_calendar(self):
        service = DynamoService(os.environ.get("SCHOOL_TABLE_NAME") )
        key = "SCHOOL|{year}|{school}".format(year=self.yearStr, school=self.school_name)
        self.fisd_schedule = service.queryOnPrimaryKey(key)  
        self.start_date =  next( (item.get('start', None) for item in self.fisd_schedule if item['sk'] == 'SCHEDULE'), 
            None) 
        self.is_holiday = self.is_date_holiday
        self.get_term = self.get_term_name


    def is_date_holiday(self, holiday_date: datetime):
        if not self.is_date_in_schedule(holiday_date):
            return "School is not in session on {}".format(holiday_date.strftime("%b %d"))
        if holiday_date.strftime("%A") in ["Saturday", "Sunday"]:
            return "No school on {}".format(holiday_date.strftime("%A")) 
            
        str_date = holiday_date.strftime('%m/%d/%Y')
        holiday_rec = next( (item for item in self.fisd_schedule \
            if item["sk"].startswith("HOLIDAY") and item["start"] == str_date), None)
        print("HOLIDAY REC {}".format(holiday_rec))
        return holiday_rec if holiday_rec == None else \
            "NO SCHOOL: {}.".format(holiday_rec.get('sk').replace('HOLIDAY|', ''))

    def is_date_in_schedule(self, date: datetime): 
        schedule = next( (item for item in self.fisd_schedule if item['sk'] == 'SCHEDULE'), 
            None)        
        return date_in_term(date, schedule)
       
    def get_term_name(self, date: datetime):
        current_term = next((term.get("sk").replace("TERMS|", "") \
            for term in self.fisd_schedule  \
            if term["sk"].startswith("TERMS") and date_in_term(date, term)), None) 
        return current_term


def date_in_term(date: datetime, term: dict):
    start_of_term = datetime.strptime(term.get("start"), "%m/%d/%Y" )
    end_of_term = datetime.strptime(term.get("end"), "%m/%d/%Y" )
    return start_of_term.date() <= date.date() and end_of_term.date() >= date.date()

