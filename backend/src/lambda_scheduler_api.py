import json
import os
import logging
from _datetime import datetime, timedelta
from services import http_service
import services.daily_calendar_service as daily
import services.district_calendar_service as district
import services.virtual_calendar_service as virtual    


logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ["LOGGING_LEVEL"]) )


def handler(event: any, context: any):
    logger.info("event: {}".format(json.dumps(event) ))
    # res = {}
    # res["statusCode"] = 404
    # res["headers"] = {
    #     "Access-Control-Allow-Origin": "*",
    #     "Access-Control-Allow-Credentials" : True,
    #     "Content-Type": "application/json"
    # }
    # res["body"] = "Not implemented"

    return schedule_router(event) 

def schedule_router (event):
    resource = event["resource"]
    method = event["httpMethod"]

    if resource == "/scheduler":
        # Get Districts
        if method == "POST":
            body = json.loads(event["body"])
            try:
                response = get_full_calendar(body.get("data"))
                return http_service.format_response(200, response)
            except Error as e:
                print("ERROR in schedule api!")
                print(e)
                print(sys.exc_info()[0])
                return  http_service.format_response(500, "Could not find a schedule for {} on {}".format(kidname, year) )



def get_full_calendar(body: dict):
    print(body)
    kidname=body.get('kidname')
    year=body.get('year')
    dist=body.get('district')
    full_calendar = dict()
    full_calendar.update({ 'district': district.get_district_calendar(year, dist) })
    full_calendar.update({ 'virtual': virtual.get_virtual_calendar(year, kidname) })
    full_calendar.update({ 'daily': daily.get_daily_calendar(year, kidname) })
    print(full_calendar)

    return full_calendar
