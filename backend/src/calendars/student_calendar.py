import json
import os
from _datetime import datetime
from services.dynamodb_service import DynamoService

class StudentCalendar:
    def __init__(self, user:str, yearStr: str):
        self.yearStr = yearStr
        self.name = user
        # op=os.system("date && ps -raxxxo pid,%cpu,%mem,vsize,time,command | grep -E 'java|gui' ")
        # print( ' -------- ')
        # print(os.getcwd())
        # print( os.listdir(os.getcwd()) )

        # daily_filename = 'calendars/config/{}_daily.json'.format(user)
        # with open(daily_filename) as f:
        #     self.daily_schedule = json.load(f)
        # # print(self.daily_schedule)
        # self.name = self.daily_schedule.get("name")
        # print("Loaded daily schedule for ", self.name)


    def get_schedule_for_date(self, date: datetime, term_name:str):
        times = self.daily_schedule.get("Times")
        term_schedule = self.daily_schedule.get(term_name)
        complete_schedule = dict()
        for class_period in term_schedule:
            # print(class_period)
            time = times.get(class_period)
            term_schedule.get(class_period).update(time)
        # print("Final schedule" , term_schedule)
        return term_schedule

    '''
        ~~~~~~~~ DYNAMO IMPLEMENTATION ~~~~~~~~~~
    '''  
    def get_dynamo_calendar(self):
        service = DynamoService(os.environ.get("DYNAMO_TABLE") )
        # KID_SCHEDULE|2020|Kiera
        key = "KID_SCHEDULE|{year}|{name}".format(year=self.yearStr, name=self.name)
        self.daily_schedule = service.queryOnPrimaryKey(key) 
        # print(self.daily_schedule) 
        self.get_schedule_for_date = self.get_schedule

    def get_schedule(self, date: datetime, term_name:str):
        complete_schedule = dict()
        for class_period in self.daily_schedule:
            class_desc = class_period.get("TERMS|{}".format(term_name))
            if class_desc != None:
                times = {class_period.get("sk").replace("PERIOD|", ""): {
                        "Class": class_desc.get("Class"),
                        "Category": class_desc.get("Category"),
                        "StartTime": class_period.get("start"),
                        "StopTime": class_period.get("end")
                    }} 
                complete_schedule.update(times)  
        # print(complete_schedule)            
        return complete_schedule    

