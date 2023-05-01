#Author name: Ammar and Likitha
#Purpose: Checkin_duration
#Date: April 04, 2023

from flask import Flask,jsonify,request,session,Blueprint
from . import app,db
from datetime import datetime,timedelta
import random
import string
from .models.model import Timetable_Event

app.secret_key = 'my_secret_key'

gc = Blueprint('generate_checkin_code', __name__, url_prefix='/api/generate')

# @gc.route('/',methods=['post'])
# def checkin():
#     if not session.get('checkin_code'):
#         session['checkin_code'] = generate_checkin_code()
#         session['checkin_expiry'] = datetime.now() + timedelta(minutes=20)
#         session.permanent = True
        
#     else:
#         #Check if checkin code has expired
#         if checkin_expired():
#             #Generate new check_in code
#             session['checkin_code'] = generate_checkin_code(timetable_event_id)
#             session['checkin_expiry'] = datetime.now()+ timedelta(minutes=20)
#     return jsonify({'checkin_code': session['checkin_code'],'expiry_time': session['checkin_expiry'].strftime('%Y-%m-%d %H:%M:%S')})

@gc.route('/generate-checkin-code/<int:timetable_event_id>',methods=['PATCH'])
def generate_checkin_code(timetable_event_id):
    #Code to generate a random 6-characterr check_in code
    
    checkin_in_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    timetable_event = Timetable_Event.query.filter_by(timetable_event_id=timetable_event_id).first()
    timetable_event.check_in_code = checkin_in_code
    db.session.commit()


    return jsonify({"msg": "Checkin code generated successfully", "checkin code": checkin_in_code})

@gc.route('/checkin-expired',methods=['post'])
def checkin_expired():
    #Check if check-in code has expired
    if session.get('checkin_expiry'):
        return datetime.now() > session['checkin_expiry']
    else:
        return True
    

    