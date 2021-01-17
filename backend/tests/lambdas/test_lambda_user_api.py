import lambda_user_api
import json

def test_get_user():
    username = 'laimaB'
    mock_event = {
        "resource": "/users/{username}",
        "httpMethod": "GET",
        "pathParameters": {
            "username" : username
        }
    }
    response = lambda_user_api.router(mock_event)
    print (f"RESPONSE: {response}")
    assert response.get("statusCode") == 200
    actual_user = json.loads(json.loads(response.get("body") ) )
    print (f"ACTUAL USER: {actual_user}")
    print (type(actual_user))
    assert actual_user.get("lastname") == None
    assert actual_user.get("status") == "active"
    assert actual_user.get("firstname") == "Laima"
    assert actual_user.get("username") == username
    assert actual_user.get("email") == "ahsiet4@yahoo.com"
    