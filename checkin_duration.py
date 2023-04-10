from flask import Flask,jsonify,request,session,Blueprint
from . import app
from datetime import datetime,timedelta
import random
import string


app.secret_key = 'my_secret_key'

gc = Blueprint('generate_checkin_code', __name__, url_prefix='/generate')

@gc.route('/checkin',methods=['post'])
def checkin():
    if not session.get('checkin_code'):
        session['checkin_code'] = generate_checkin_code()
        session['checkin_expiry'] = datetime.now() + timedelta(minutes=20)
        session.permanent = True
    else:
        #Check if checkin code has expired
        if checkin_expired():
            #Generate new check_in code
            session['checkin_code'] = generate_checkin_code()
            session['checkin_expiry'] = datetime.now()+ timedelta(minutes=20)
    return jsonify({'checkin_code': session['checkin_code'],'expiry_time': session['checkin_expiry'].strftime('%Y-%m-%d %H:%M:%S')})
@gc.route('/generate-checkin-code',methods=[' post'])
def generate_checkin_code():
    #Code to generate a random 6-characterr check_in code
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
@gc.route('/checkin-expired',methods=['post'])
def checkin_expired():
    #Check if check-in code has expired
    if session.get('checkin_expiry'):
        return datetime.now() > session['checkin_expiry']
    else:
        return True
    

    