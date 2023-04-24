# Author: Aruni
#Purpose: To test fetch current semester lessons by tutotr id functionality
#Date: April 23, 2023

import requests

def test_get_lessons_by_tutor():
    
    url = "http://127.0.0.1:5000/tutor//current-semester-lessons/3"
    
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"