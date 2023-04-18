#Author name: Aruni
#Purpose: Create app.py
#Date: March 14, 2023


from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
# Marshmallow is an object serialization/deserialization library
from marshmallow import Schema
import os
#import jsonpickle

app = Flask(__name__)

# the name of the database; add path if necessary
db_name = 'student.db'

# these two lines added to mac os support
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_name)

#support for windows
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
db.init_app(app)


# Import each table from model.py to app.py so that Flask can run

from models.model import Attendance
from models.model import Student
from models.model import Tutor
from models.model import Course
from models.model import Module
from models.model import Timetable_Event

with app.app_context():
    db.create_all()

@app.route('/')
def home_route():
    return "Welcome To Student Management System"

#Create tutor schema
class TutorSchema(Schema):
    class Meta:
        fields = ('tutor_id','tutor_forename','tutor_surname','tutor_email','tutor_category','module_id')

#Create module schema
class ModuleSchema(Schema):
    class Meta:
        fields = ('module_id','module_title','module_description','module_credits','course_code','tutor_id')
        
# Init schema
tutor_schema = TutorSchema(many =True)
module_schema = ModuleSchema(many =True)

@app.route('/fetchLessons/<tutor_id>', methods = ['GET'])
def fetchLessonsByTutor(tutor_id):
   #add keyboard input to tutorid
   #remove the hard code value for the tutorid
   #add this in seperate page and make it work
    
    lessons = Module.query.filter_by(tutor_id=tutor_id)
    results = module_schema.dump(lessons)
    
    return jsonify( results)
   
