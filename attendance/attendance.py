#Author name: Jeffrey and Likitha
#Purpose: Accept only code P to mark attendance present, Checkin_duration
#Date: April 01, 2023
from flask import request, jsonify, Blueprint
from ..models.model import Timetable_Event, Attendance 
from .. import db
from datetime import datetime, timedelta

at = Blueprint('attendance', __name__, url_prefix='/register-attendance')

@at.route('/<int:timetable_event_id>', methods=['POST'])
def attendance(timetable_event_id):

    check_in = request.json.get('check_in_code')
    now = datetime.now()
    # the checkin code should be generated and stored in the timetable event table by the tutor
    check_in_code = Timetable_Event.query.filter_by(check_in_code=check_in, timetable_event_id=timetable_event_id).first()
    event_time = check_in_code.timetable_event_datetime
    event_time_plus = event_time + timedelta(minutes = 20)
    if event_time_plus > now:
        if check_in_code:
            register_attendance = Attendance(timetable_event_id=timetable_event_id, student_id= 1, status="P") #P is set as a placeholder for the code of A/O/N/P functionality, and 1 is a placeholder till the student has been committed into database
            db.session.add(register_attendance)
            db.session.commit()

            return jsonify ({"success" : "Attendance Has Been Marked"})
        else:
            return jsonify ({"error":"Invalid Input, Attendance Has Not Been Marked"})
        
    else:
        return jsonify ({"error":"You are late, Attendance Has Not Been Marked"})

    
@at.route('/bulk-attendance/<int:timetable_event_id>', methods=['POST'])
def bulk_reg(timetable_event_id):
    students = request.json.get("students")
    for student in students:
        id = student["student_id"]
        status = student["attendance_status"]
        register_all = Attendance(timetable_event_id=timetable_event_id, student_id=id, status=status)
        db.session.add(register_all)
        db.session.commit()

    return jsonify ({"success":"Students Attendance Has Been marked"})
     
@at.route('amend-attendance/<int:timetable_event_id>', methods=['PUT'])
def amend(timetable_event_id):
    stat = request.json.get("student_id")

    change = Attendance.query.filter_by(timetable_event_id, student_id=stat)
    if change.status is not "P":
            stat = "P"
            db.session.commit()
            return jsonify ({"success":"attendance has been updated"})
    
    else:
         return jsonify({"error":"attendance has already been marked"})