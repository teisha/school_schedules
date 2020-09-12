import sys
sys.path.insert(0, 'calendars')
from _datetime import datetime

from calendars.school_calendar import SchoolCalendar
from calendars.student_calendar import StudentCalendar
from calendars.virtual_calendar import VirtualCalendar
# import importlib
# from importlib import machinery 
# loader1 = importlib.machinery.SourceFileLoader('student_loader', 'calendars/student_calendar.py')
# student_loader = loader1.load_module('student_loader')
# loader2 = importlib.machinery.SourceFileLoader('virtual_loader', 'calendars/virtual_calendar.py')
# virtual_loader = loader2.load_module('virtual_loader')
# loader3 = importlib.machinery.SourceFileLoader('school_loader', 'calendars/school_calendar.py')
# school_loader = loader3.load_module('school_loader')


class Calculator:
    def __init__(self, user:str):
        self.user = user
        self.daily_calendar = StudentCalendar(user)
        self.virtual_calendar = VirtualCalendar(user)
        self.school_calendar = SchoolCalendar()
        self.name = self.daily_calendar.name 
        self.virtual_calendar.set_name(self.name)    
        self.virtual_calendar.set_week_one(self.school_calendar.start_date)      
        # print ("Loaded calendars for ", self.name)   

    def is_there_school(self, date: datetime):
        print("Generating schedule for ", date.strftime("%A, %d. %B %Y %I:%M%p"))
        is_holiday = self.school_calendar.is_holiday(date)
        if is_holiday != None:
            return dict(schedule=None, message=is_holiday, name=self.name)

        self.term = self.school_calendar.get_term(date)
        print ("Schedule for TERM: ", self.term.get("name"))
        schedule = None
        try:
            schedule = self.daily_calendar.get_schedule_for_date(date, self.term.get("name"))
            schedule = self.virtual_calendar.add_virtual_week_to_schedule(date, schedule)
        except:
            raise RuntimeError("Could not derive schedule for {}".format(self.name))

        if schedule != None:
            return dict(schedule=schedule, message=None, name=self.name)
        else:
            raise ValueError("Could not determine schedule for {}".format(self.name))

    def print_schedule(self, schedule: dict):
        noclass = []
        for key in sorted(schedule):
            class_info = schedule.get(key)
            if class_info.get("has_class") == True:
                print ("Period {}: {}, is {} and starts at {} ".format( key , class_info.get("Class"),
                    class_info.get("virtual_option"), class_info.get("StartTime") ) )
            else:
                noclass.append(class_info.get("Class"))   
        if len(noclass) > 0:
            print(" **  Not on schedule today: ")                         
            for classname in noclass:
                print("  No {} class today".format( classname ))
