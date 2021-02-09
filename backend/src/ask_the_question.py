import os
from _datetime import datetime, timedelta
from schedule_calculator import Calculator



class Questioner:
    def __init__(self):
        print(" ")
        self.today = datetime.now()
        os.environ["DYNAMO_TABLE"] = 'prod-visual-schedules-data-table'

    def what_is_my_schedule(self, student: str, date: datetime) :
        calculator = Calculator(student)
        print('What is the School Schedule for {} ?'.format( calculator.name) )
        try:
            sched = calculator.is_there_school(date)
            # print (sched)
            print ("  ===================== {} School Schedule For {} ========================================".format(sched.get("name"), date.strftime("%A, %b %d, %Y")))
            if sched.get("schedule") != None:
                schedule = sched.get("schedule")
                calculator.print_schedule(schedule)
            else:
                print(sched.get("message"))
            print("            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except ValueError as e:
            print("COULD NOT FIND SCHEDULE!")
            print(e)
        



if __name__ == "__main__":
    question = Questioner()

    question.what_is_my_schedule("Delia", (datetime.now() + timedelta(days=1)))
    question.what_is_my_schedule("Kiera", (datetime.now() + timedelta(days=1)))
    question.what_is_my_schedule("Kiera", (datetime.now() + timedelta(days=24)))
    question.what_is_my_schedule("Delia", datetime.now() )
    question.what_is_my_schedule("Kiera", datetime.now() )