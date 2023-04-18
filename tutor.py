# Author: Aruni
#Purpose: To Fetch The List of modules by tutor
#Date; April 8, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Course, courses_schema

#course route
cs = Blueprint('course', __name__, url_prefix='/course')


@cs.route("/")
def course():
    return jsonify({"Welcome": "Course Page"})

# This allows all courses to be regsitered via Isomnia
@cs.route("/register", methods= ["POST"])
def reg_course():
    course_title = request.json.get("course_title")
    course_code = request.json.get("course_code")
    course_description = request.json.get("course_description")
    course_level = request.json.get("course_level")
    course_credits = request.json.get("course_credits")

    course = Course(course_title = course_title, course_code=course_code, course_description = course_description,course_level= course_level, course_credits = course_credits)
    db.session.add(course)
    db.session.commit()


    print(course_title)
    

    return jsonify({"message": "success"}), 201



# This allows each courses regsitered to be fetched via Isomnia
@cs.route("/get-course")
def get_course():
    get_courses = Course.query.all()

    print(list(get_courses))
    return courses_schema.dump(get_courses)

# Author: Yusuf
#Purpose: To Fetch The List of Courses(id, forename, lastname, email, category) and save in DB
#Date; April 8, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Course, courses_schema

#course route
cs = Blueprint('course', __name__, url_prefix='/course')


@cs.route("/")
def course():
    return jsonify({"Welcome": "Course Page"})

# This allows all courses to be regsitered via Isomnia
@cs.route("/register", methods= ["POST"])
def reg_course():
    course_title = request.json.get("course_title")
    course_code = request.json.get("course_code")
    course_description = request.json.get("course_description")
    course_level = request.json.get("course_level")
    course_credits = request.json.get("course_credits")

    course = Course(course_title = course_title, course_code=course_code, course_description = course_description,course_level= course_level, course_credits = course_credits)
    db.session.add(course)
    db.session.commit()


    print(course_title)
    

    return jsonify({"message": "success"}), 201



# This allows each courses regsitered to be fetched via Isomnia
@cs.route("/get-course")
def get_course():
    get_courses = Course.query.all()

    print(list(get_courses))
    return courses_schema.dump(get_courses)

