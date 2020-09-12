import json
import os
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
        return calculator.is_there_school(schedule_date)
    except:
        return ({"message": "I'm sorry.  I could not find a schedule for {} on {}".format(person_name, schedule_date)})

   
