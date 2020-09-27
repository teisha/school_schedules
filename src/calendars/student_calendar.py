import json
import os
from _datetime import datetime

class StudentCalendar:
    def __init__(self, user:str):
        daily_filename = 'calendars/conf/{}_daily.json'.format(user)
        # op=os.system("date && ps -raxxxo pid,%cpu,%mem,vsize,time,command | grep -E 'java|gui' ")
        # print( ' -------- ')
        # print(os.getcwd())
        # print( os.listdir(os.getcwd()) )
        with open(daily_filename) as f:
            self.daily_schedule = json.load(f)
        # print(self.daily_schedule)
        self.name = self.daily_schedule.get("name")
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
