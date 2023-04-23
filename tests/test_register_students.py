# Author: Aruni
#Purpose: To write unit tests
#Date: April 23, 2023

import requests
import json
    
def test_register_students():   
   
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data={
        "student_category": "PG",
        "student_email": "John@bolton.uk",
        "student_forename": "John",
        "student_lastname": "Doe"
        }

    
    url = 'http://127.0.0.1:5000/student/register'

    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    