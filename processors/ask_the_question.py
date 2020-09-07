from _datetime import datetime, timedelta

import importlib
from importlib import machinery 
loader = importlib.machinery.SourceFileLoader('calc', 'processors/schedule_calculator.py')
calc = loader.load_module('calc')



class Questioner:
    def __init__(self):
        print(" ")
        self.today = datetime.now()

    def what_is_my_schedule(self, student: str, date: datetime) :
        calculator = calc.Calculator(student)
        print('What is the School Schedule for {} ?'.format( calculator.name) )
        try:
            sched = calculator.is_there_school(date)
            # print (sched)
            print ("  ===================== {} School Schedule For {} ========================================".format(sched.get("name"), date.strftime("%A, %b %d, %Y")))
            if sched.get("schedule") != None:
                schedule = sched.get("schedule")
                for key in sorted(schedule):
                    class_info = schedule.get(key)
                    print ("Period {}: {}, is {} and starts at {} ".format( key , class_info.get("Class"),
                        class_info.get("virtual_option"), class_info.get("StartTime") ) )
            else:
                print(sched.get("message"))
            print("            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except ValueError as e:
            print("COULD NOT FIND SCHEDULE!")
            print(e)
        



if __name__ == "__main__":
    question = Questioner()
    question.what_is_my_schedule("kb", (datetime.now() + timedelta(days=3)))
    question.what_is_my_schedule("db", (datetime.now() + timedelta(days=3)))