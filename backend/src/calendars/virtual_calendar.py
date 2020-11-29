
from _datetime import datetime
from enum import Enum
from decimal import Decimal
import sys, os, json
# print(sys.path)
import copy
from services.dynamodb_service import DynamoService

Weekdays: Enum = Enum('Weekdays', [('mon' , "Monday"),('tue', "Tuesday"),
    ('wed', "Wednesday"),('thu', "Thursday"),('fri', "Friday")] )
Categories: Enum = Enum('Categories', [('mat', "Math"), ('eng', "English"),
    ('soc', "Social Studies"), ('sci',"Science"), ('ele','Elective'), 
    ('lan','World Language'), ('fin',"Fine Arts"), ('pe','PE'),
    ('que', 'Quest')])    

class VirtualCalendar:
    calendar = [dict()]

    def __init__(self, user: str, yearStr: str):
        self.yearStr = yearStr
        self.name = user
        # virtual_filename = 'calendars/config/{}_virtual.json'.format(user)
        # with open(virtual_filename) as f:
        #     self.virtual_schedule = json.load(f)        


    def set_week_one(self, school_start: str) :
        start_date = datetime.strptime(school_start, "%m/%d/%Y")
        self.start_date : datetime = start_date
        self.week_one :int = int(start_date.strftime("%U") )


    # def set_name(self, user_name):
    #     self.name = user_name
    #     # print ("Set calendar name to ", self.name)

    # def get_week_schedule(self, date: datetime):
    #     day_of_week = date.strftime("%A")
    #     week_num: int = int(date.strftime("%U") )
    #     if date.year > self.start_date.year:
    #         week_num = 53 + int(date.strftime("%U"))
    #     week = "week1"            
    #     if ( week_num - self.week_one ) % 2 == 1:
    #         week = "week2"
    #         print("week2")
    #     week_sched = self.virtual_schedule.get(week)
    #     return week_sched.get(day_of_week)

    def add_virtual_week_to_schedule(self, date: datetime, schedule):
        virtual_schedule = copy.deepcopy(schedule)
        virtual_options = self.get_week_schedule(date)
        print (virtual_options)
        for period in virtual_schedule:
            category = schedule.get(period).get("Category")
            async_list = virtual_options.get("async")
            sync_list = virtual_options.get("sync")
            if category in async_list:
                virtual_schedule.get(period).update({"virtual_option": "ASYNCHRONOUS", "has_class": True})
            elif category in sync_list:
                virtual_schedule.get(period).update({"virtual_option": "SYNCHRONOUS", "has_class": True})   
            else:
                virtual_schedule.get(period).update({"has_class": False})                           
            # print(virtual_schedule.get(period), virtual_options)                
        # print (virtual_schedule)
        return virtual_schedule            

    '''
        ~~~~~~~~ DYNAMO IMPLEMENTATION ~~~~~~~~~~
    '''  
    def get_dynamo_calendar(self, school_start: str):
        service = DynamoService(os.environ.get("DYNAMO_TABLE") )
        # VIRTUAL_SCHEDULE|2020|Kiera
        key = "VIRTUAL_SCHEDULE|{year}|{name}".format(year=self.yearStr, name=self.name)
        self.virtual_schedule = service.queryOnPrimaryKey(key) 
        self.start_date: datetime = datetime.strptime(school_start, "%m/%d/%Y")
        self.week_one :int = int(self.start_date.strftime("%U") )
        self.weeks_in_rotation: int = next((item.get("num_weeks") for item in self.virtual_schedule \
            if item["sk"] == "SETTINGS"), 0)
        self.get_week_schedule = self.get_schedule_for_day    

    def get_schedule_for_day(self, date: datetime):
        day_of_week = date.strftime("%A")
        week_num: int = int(date.strftime("%U") )
        if date.year > self.start_date.year:
            week_num = 53 + int(date.strftime("%U"))        
        week = (( week_num - self.week_one ) % 2 ) + 1
        # print("Day of week: {}, Week Number: {}, week: {}".format(day_of_week, week_num, week))
        week_schedule = next( (item for item in self.virtual_schedule \
            if item["sk"] == "WEEK{week}|{dow}".format(week=week,dow=day_of_week )) )
        return week_schedule

    '''
        ~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~
    '''  


    # not used yet - thinking this would be for data entry
    def add_day(self, day_name: str, week_number: int, category_name: str, synch: bool):  
        day = next((weekday for weekday in Weekdays if weekday.value == day_name), None)    
        if day == None:
            raise ValueError('Could not add day: {}'.format(day_name))

        category = next((cat for cat in Categories if cat.value == category_name), None)    
        if category == None:
            raise ValueError('Could not add class category: {}'.format(category_name))

        if len(self.calendar) < week_number - 1:
            week = self.calendar[week_number-1]
            current_schedule = week.get(day)
            if current_schedule == None:
                current_schedule.update({day,[{category,synch}]})
            else:
                current_day = current_schedule.get(day) 
                current_day.append({category:synch})             
        else:
            raise ValueError('Could not add week {}.  There are only {} weeks defined'.format(week_number, len(self.calendar)))

        print ("Current Calendar for week:" )
        print (self.calendar[week_number-1])

    def add_week(self):
        self.calendar.append(dict())

