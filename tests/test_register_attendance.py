import json
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask.testing import FlaskClient
import pytest
from .. import attendance
from .. import db
from ..models.model import Timetable_Event, Attendance

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(attendance)
    with app.test_client() as client:
        yield client

def test_attendance(client):
    now = datetime.now()

    # Test valid attendance registration
    valid_data = {'check_in_code': '12345'}
    response = client.post('/api/register-attendance/1', json=valid_data)
    assert response.status_code == 201
    assert b'"success": "Attendance Has Been Marked"' in response.data

    # Test invalid attendance registration due to wrong check-in code
    invalid_data = {'check_in_code': '54321'}
    response = client.post('/api/register-attendance/1', json=invalid_data)
    assert response.status_code == 400
    assert b'"error":"Invalid Input, Attendance Has Not Been Marked"' in response.data

    # Test invalid attendance registration due to being late
    late_check_in = (now - timedelta(minutes=25)).strftime('%Y-%m-%d %H:%M:%S')
    with attendance.app_context():
        timetable_event = Timetable_Event(timetable_event_id=1, check_in_code='12345', timetable_event_datetime=late_check_in)
        db.session.add(timetable_event)
        db.session.commit()
    response = client.post('/api/register-attendance/1', json=valid_data)
    assert response.status_code == 400
    assert b'"error":"You are late, Attendance Has Not Been Marked"' in response.data

