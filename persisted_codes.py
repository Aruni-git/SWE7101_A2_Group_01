#Author name: Likitha
#Purpose: If code already persists,API returning error message
#Date: April 11, 2023

from flask import Flask,request,jsonify,Blueprint

pc = Blueprint('persisted_codes', __name__, url_prefix='/persisted-code')

#Sample list of codes that have already been persisted
persisted_codes = ['A', 'O', 'P', 'N', 'C']

@pc.route('/<int:timetable_event_id>', methods = ['POST'])
def check_in():
    #Extract the code from the request data
    code = request.json.get('code')
    
    #Check if the code already exists in the persisted codes list
    if code in persisted_codes:
        return jsonify({'message': 'Code already exists'}),400
    else:
        return jsonify ({'message': 'Code does not exist'}),404