from flask import  jsonify, request,Blueprint
from . import db
from .models.model import Timetable_Event,Attendance,Student, attendances_schema
gm = Blueprint('get_attendance_mark',__name__,url_prefix='/get-attendance')

#Endpoint to get attendance marks for a particular student
@gm.route('/student-attendance')
def attendance():
    #Connect to SQLite database    
    #Query the attendance table by the Student ID
    cursor = Attendance.query.filter_by(student_id = 1)
    #Dump all attendance records for the Student ID queried in the cursor variable
    attendance = attendances_schema.dump(cursor)
    #return the attendance records of the student ID that has been queried
    return jsonify({'attendance': attendance})
