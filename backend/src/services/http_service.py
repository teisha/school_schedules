import json

def format_response(status: int, body: dict=None):
    response = {}
    response["statusCode"] = status
    response["headers"] = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
        "Access-Control-Allow-Headers": 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with',
        "Content-Type": "application/json"   
        # Access-Control-Allow-Origin       integration.response.body.Origin
        # Access-Control-Allow-Credentials  'true'
        # Access-Control-Allow-Methods      'GET'        
    }

    if body:
        response["body"] = json.dumps(body)

    return response