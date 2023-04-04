#Author name: Aruni
#Purpose: Create app.py
#Date: April 04, 2023

from flask import Flask,jsonify
# Marshmallow is an object serialization/deserialization library
from marshmallow import Schema

from models.model import Tutor

#Create tutor schema
class TutorSchema(Schema):
    class Meta:
        fields = ('tutor_id','tutor_forename','tutor_surname','tutor_email','tutor_category','module_id')
        
# Init schema
tutor_schema = TutorSchema(many =True)

@app.route('/getLessons', methods = ['GET'])
def tefetchLessonsByTutorst():
    
    lessons = Tutor.query.all()
    results = tutor_schema.dump(lessons)
    
    return jsonify( results)
   # return  jsonpickle.encode(tutor,unpicklable=False)
