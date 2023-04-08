# Author: Yusuf
#Purpose: To Fetch The List of Modules (id, forename, lastname, email, category) and save in DB
#Purpose: To Fetch The List of Students(id, forename, lastname, email, category) Enrolled on the Module and save in DB

#Date; April 8, 2023


from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Module, modules_schema, Student_Enrole_Module, enrols_schema, Student, students_schema

# module route
md = Blueprint('module', __name__, url_prefix='/module')


@md.route("/")
def module():
    return jsonify({"Welcome": "Module Page"})

# This allow each module to be registered via Isomnia
@md.route("/register", methods= ["POST"])
def reg_module():
    module_title = request.json.get("module_title")
    module_description = request.json.get("module_description")
    module_level = request.json.get("module_level")
    module_credits = request.json.get("module_credits")
    course_id = request.json.get("course_id")
    

    module = Module(module_title = module_title, module_description = module_description, module_level = module_level, module_credits = module_credits, course_id = course_id)
    db.session.add(module)
    db.session.commit()


    print(module_title)
    

    return jsonify({"message": "success"}), 201



# This allow all modules regsitered to be fetched via Isomnia
@md.route("/get-module")
def get_module():
    get_modules = Module.query.all()

    print(list(get_modules))
    return modules_schema.dump(get_modules)

# This allows student to be enrolled in each module via Isomnia
@md.route("/enrole-student-module",  methods= ["POST"])
def student_enroll_module():
    module_id = request.json.get("module_id")
    student_id = request.json.get("student_id")

    student_enrol_module = Student_Enrole_Module(module_id = module_id, student_id = student_id)
    db.session.add(student_enrol_module)
    db.session.commit()

    return jsonify({"message": "success"}), 201

# This allows each student enrolled in the module to be fetched via Isomnia.
@md.route("/get-module_student/<int:id>")
def get__module_student(id):
    get_student_enrole_modules = Student_Enrole_Module.query.filter_by(module_id=id)

    student_list =[]
    for student_id in get_student_enrole_modules:
        student = Student.query.filter_by(student_id=student_id.student_id).first()
        student_list.append(student)

    data  = {
        "Number of students enrolled in the module are" : len(student_list),
       "students": students_schema.dump(student_list)
    }
    print(student_list)


    return jsonify(data)
    

