# Author: Yusuf
#Purpose: To Fetch The List of Students(id, forename, lastname, email, category) and save in DB
#Date; April 8, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Student, students_schema

#student route
st = Blueprint('student', __name__, url_prefix='/student')


@st.route("/")
def student():
    return jsonify({"Welcome": "Student Dashboard"})

# This allow the student to be registered via Isomnia
@st.route("/register", methods= ["POST"])
def reg_student():
    student_forename = request.json.get("student_forename")
    student_lastname = request.json.get("student_lastname")
    student_email = request.json.get("student_email")
    student_category = request.json.get("student_category")

    student = Student(student_forename=student_forename, student_lastname=student_lastname,student_email=student_email, student_category = student_category)
    db.session.add(student)
    db.session.commit()


    return jsonify({"message": "success"}), 201


# This allow the list of students registered to be fetched via Isomnia
@st.route("/get-students")
def get_student():
    get_students = Student.query.all()

    print(list(get_students))
    return students_schema.dump(get_students)

