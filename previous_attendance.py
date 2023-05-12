from flask import  jsonify, request,Blueprint
from . import db
from .models.model import Timetable_Event,Attendance,Student, attendances_schema
gm = Blueprint('get_attendance_mark',__name__,url_prefix='/api/get-attendance')

#Endpoint to get attendance marks for a particular student