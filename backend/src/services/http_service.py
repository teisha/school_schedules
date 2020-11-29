import json

def format_response(status: int, body=None):
    response = {}
    response["statusCode"] = status
    response["headers"] = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
        "Content-Type": "application/json"   
    }

    if body:
        response["body"] = json.dumps(body)

    return response