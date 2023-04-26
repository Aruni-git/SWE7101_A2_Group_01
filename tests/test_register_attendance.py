# Author: Jeffrey
#Purpose: To test registering attendance
#Date: April 23, 2023

import requests
import json
    
def test_register_students():   
   
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data={
            "check_in_code":"yyyyy"
        }

    
    url = "http://127.0.0.1:5000/register-attendance/1"

    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    