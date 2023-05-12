# Author: Jeffrey
#Purpose: To test registering attendance
#Date: April 23, 2023
import requests
import json
    
def test_bulk_attendance():   
   
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    data = {
        "students": [
            {"student_id": 1, "attendance_status": "N"},
            {"student_id": 2, "attendance_status": "N"},
            {"student_id": 3, "attendance_status": "N"}, 
            {"student_id": 4, "attendance_status": "N"}
        ]
    }

    url = 'http://127.0.0.1:5000/api/register-attendance/bulk-attendance-with-status-code/1'
    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"


    