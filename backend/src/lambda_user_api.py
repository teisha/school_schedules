import json
import os
import logging
from _datetime import datetime, timedelta
from services import user_service, http_service


logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ["LOGGING_LEVEL"]) )


def handler(event: any, context: any):
    logger.info("event: {}".format(json.dumps(event) ))
    return router(event) 


def router (event, service=user_service)  
    resource = event["resource"]
    method = event["httpMethod"]

    if resource == "/users/{username}":
        # Get Districts
        if method == "GET":
            user_response = service.get_user(event["body"].get("username"))
            return http_service.format_response(200, json.dumps(user_response))
        if method == "PUT":
            user_response = service.save_user(json.loads(event["body"]))
            return http_service.format_response(user_response.get('statusCode'), user_response.get("message"))

        return apiGatewayResponse(404, "Not Found")



