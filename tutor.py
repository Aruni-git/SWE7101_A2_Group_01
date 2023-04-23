# Author: Aruni
#Purpose: To Fetch The List of modules by tutor
#Date; April 8, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Module, modules_schema

#tutor route
tt = Blueprint('tutor', __name__, url_prefix='/tutor')


@tt.route("/")
def tutor():
    return jsonify({"Welcome": "Tutor Page"})

@tt.route('/lessons/<tutor_id>', methods = ['GET'])
def fetchLessonsByTutor(tutor_id): 
    
    fetch_lessons = Module.query.filter_by(tutor_id=tutor_id)

    print(list(fetch_lessons))
    return modules_schema.dump(fetch_lessons)
