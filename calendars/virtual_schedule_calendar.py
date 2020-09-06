
from _datetime import datetime
from enum import Enum


Weekdays: Enum = Enum('Weekdays', [('mon' , "Monday"),('tue', "Tuesday"),
    ('wed', "Wednesday"),('thu', "Thursday"),('fri', "Friday")] )
Categories: Enum = Enum('Categories', [('mat', "Math"), ('eng', "English"),
    ('soc', "Social Studies"), ('sci',"Science"), ('ele','Elective'), 
    ('lan','World Language'), ('fin',"Fine Arts"), ('pe','PE'),
    ('que', 'Quest')])    

class VirtualCalendar:
    calendar = [dict()]

    def __init__(self):
        self.today = datetime.now()

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