import json
import os
import logging
from _datetime import datetime, timedelta


logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ["LOGGING_LEVEL"]) )


def handler(event: any, context: any):
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