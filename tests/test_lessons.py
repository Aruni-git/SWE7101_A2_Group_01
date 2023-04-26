# Author: Aruni
#Purpose: To write unit tests
#Date: April 23, 2023

import requests

def test_get_lessons_by_tutor():
    
    url = "http://127.0.0.1:5000/tutor/lessons/2"
    
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    