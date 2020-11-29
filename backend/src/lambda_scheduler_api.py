import json
import os
import logging
from _datetime import datetime, timedelta
from services import schedule_service, http_service


logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ["LOGGING_LEVEL"]) )


def handler(event: any, context: any):
    dynamo_service = db.DynamodbService()
    logger.info("event: {}".format(json.dumps(event) ))
    res = {}
    res["statusCode"] = 404
    res["headers"] = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials" : True,
        "Content-Type": "application/json"
    }
    res["body"] = "Not implemented"

    return res
def schedule_router (event, schedules: schedule_service)  
    resource = event["resource"]
    method = event["httpMethod"]

    if resource == "/scheduler":
        # Get Districts
        if method == "GET":
            districtsResponse = schedules.getDistricts()
            return http_service.format_response(200, districtsResponse)
