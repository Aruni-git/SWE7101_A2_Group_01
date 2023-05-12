#Author name: Ammar, Jeffrey and Likitha
#Purpose: Accept only code P to mark attendance present, Checkin_duration
#Date: April 01, 2023
from flask import request, jsonify, Blueprint
from ..models.model import Timetable_Event, Attendance
from .. import db
from datetime import datetime, timedelta

at = Blueprint('attendance', __name__, url_prefix='/api/register-attendance')

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
            register_attendance = Attendance(timetable_event_id=timetable_event_id, student_id= id, status="P") #P is set as a placeholder for the code of A/O/N/P/C functionality, and 1 is a placeholder till the student has been committed into database
            db.session.add(register_attendance)
            db.session.commit()

            return jsonify ({"success" : "Attendance Has Been Marked"}),201
        else:
            return jsonify ({"error":"Invalid Input, Attendance Has Not Been Marked"}),400
        
    else:
        return jsonify ({"error":"You are late, Attendance Has Not Been Marked"})

    
@at.route('/bulk-attendance-with-status-code/<int:timetable_event_id>', methods=['POST'])
def bulk_reg(timetable_event_id):
    valid_status_codes = ['A', 'O', 'P', 'N', 'C']
    invalid_codes = []
    students = request.json.get("students")

    for student in students:
        id = student["student_id"]
        status = student["attendance_status"]
        if status not in valid_status_codes:
            invalid_codes.append({"student_id": id, "attendance_status": status})
            continue
        try:
                register_all = Attendance(timetable_event_id=timetable_event_id, student_id=id, status=status)
                db.session.add(register_all)
                db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"success": "Students attendance has been marked" ,"invalid_codes": invalid_codes}),201 
     
@at.route('/amend-attendance/<int:student_id>', methods=['PUT'])
def amend(student_id):
    stat = request.json.get("attendance_status")

    change = Attendance.query.filter_by(status=stat)
    if student_id:
            Attendance.status = stat
            db.session.commit()
            return jsonify ({"success":"attendance has been updated"}),200
    
    else:
         return jsonify({"error":"attendance has already been marked"})

@at.route("amend-attendance-prev-semester/<int:course_id>/students/<int:student_id>", methods=["PUT"])
def update_module_lesson_attendance(module_lesson_id, student_id):
    stat = request.json.get("student_id")
    try:
        attendance = db.session.execute(db.select(Attendance).where(Attendance.module_lesson_id == module_lesson_id).where(Attendance.student_id == student_id)).scalar_one()
        
        module = db.session.execute(db.select(module).where(module.id == module.module_id)).scalar_one()
        
        semester = db.session.execute(db.select(module).where(module.id == module.semester_id)).scalar_one()

        if semester.is_active:
            status = request.json.get("status", None)
            valid_status_codes = ["A", "O", "P", "N", "C"]
            if status not in valid_status_codes:
                return jsonify({"invalid": "Invalid Status Code"}), 401
            
            attendance.attendance_status = status
            db.session.commit()
            
            return jsonify({"success": "Attendance Updated Successfully"}), 200
        else:
            return jsonify({"msg": "Amendment prior to current semester not allowed"}), 401
        
    except Exception as e:
        return jsonify(str(e)), 401
