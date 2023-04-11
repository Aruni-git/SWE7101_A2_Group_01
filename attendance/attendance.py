#Author name: Jeffrey
#Purpose: Accept only code P to mark attendance present
#Date: April 01, 2023
from flask import request, jsonify, Blueprint
from ..check_in import check_in_code
from ..models.model import Timetable_Event, Attendance
from .. import db

at = Blueprint('attendance', __name__, url_prefix='/register-attendance')


@at.route('/<int:timetable_event_id>', methods=['POST'])
def attendance(timetable_event_id):

    check_in = request.json.get('check_in_code')

    # the checkin code should be generated and stored in the timetable event table by the tutor
    #check_in_code = Timetable_Event.query.filter_by(check_in_code=check_in, timetable_event_id=timetable_event_id).first()
    #if check_in_code:
    register_attendance = Attendance(timetable_event_id=timetable_event_id, student_id=1, status="P")
    db.session.add(register_attendance)
    db.session.commit()

    return jsonify ({"success" : "Attendance Has Been Marked"})
    # else:
    #     return jsonify ({"error":"Invalid Input, Attendance Has Not Been Marked"})

