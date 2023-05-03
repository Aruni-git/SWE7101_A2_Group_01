# Author: Aruni
#Purpose: To Fetch The List of modules by tutor
#Date; April 8, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Module, modules_schema, Timetable_Event, timetable_event_schemas
from datetime import datetime
from sqlalchemy import and_


#tutor route
tt = Blueprint('tutor', __name__, url_prefix='/api')


@tt.route("/")
def tutor():
    return jsonify({"Welcome": "Tutor Page"})

@tt.route('/lessons', methods = ['GET'])
def fetchLessonsByTutor(): 
    args = request.args['tutor_id']
    fetch_lessons = Module.query.filter_by(tutor_id=args)

    print(list(fetch_lessons))
    return modules_schema.dump(fetch_lessons)

# Fetch current lessons for the semester
@tt.route('/current-semester-lessons/<tutor_id>', methods = ['GET'])
def fetch_Current_semester_lesson(tutor_id): 
    
    fetch_modules = Module.query.filter_by(tutor_id=tutor_id, semester_is_active=True)

    module_id_list=[]
    current_lessons = []

    for each_module_id in fetch_modules:
        module_id_list.append(each_module_id.module_id)

    for each_module in module_id_list:
        module = Module.query.filter_by(module_id=each_module).first()
        fetch_lessons = Timetable_Event.query.filter_by(module_id=each_module)

        data = {
            "module_name" : module.module_title,
            "module_lessons" : timetable_event_schemas.dump(fetch_lessons)

        } 
        current_lessons.append(data) 
    return current_lessons

# Fetch previous lessons for each semester
@tt.route('/previous-lessons/<tutor_id>', methods = ['GET'])
def fetch_past_lesson(tutor_id): 
    today = datetime.now()
    
    fetch_modules = Module.query.filter_by(tutor_id=tutor_id)

    module_id_list=[]
    past_lessons = []

    for each_module_id in fetch_modules:
        module_id_list.append(each_module_id.module_id)

    for each_module in module_id_list:
        module = Module.query.filter_by(module_id=each_module).first()
        fetch_lessons = Timetable_Event.query.filter(and_(Timetable_Event.module_id == each_module,
                                     Timetable_Event.timetable_event_timestart <= today)).all()

        data = {
            "module_name" : module.module_title,
            "module_lessons" : timetable_event_schemas.dump(fetch_lessons)
        } 
        past_lessons.append(data) 
    return past_lessons
