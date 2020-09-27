import json
import os
import sys
import logging
from _datetime import datetime, timedelta
from schedule_calculator import Calculator 


logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ["LOGGING_LEVEL"]) )


def handler(event: any, context: any):
    logger.info("event: {}".format(json.dumps(event) ))

    person_name = event["name"]
    schedule_date = event["date"]

    return getSchoolSchedule(person_name, schedule_date)


def getSchoolSchedule(person_name: str, schedule_date: datetime):
    logger.info("Gathering schedule for {} on {}".format(person_name, schedule_date))
    try:
        calculator = Calculator(person_name)
        date_to_get =  datetime.strptime(schedule_date, '%m/%d/%Y')
        return calculator.is_there_school(date_to_get)
    except ValueError as e:
        print("ERROR in schedule call!")
        print(e)
        print(sys.exc_info()[0])
        return ({"message": "I'm sorry.  I could not find a schedule for {} on {}".format(person_name, schedule_date)})

   
