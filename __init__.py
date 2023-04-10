# import the Flask class from the flask library
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
  

# create an instance of the Flask class and assign to app
# __name__ refers to the default path of the package
app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)

# Created a class to initiate app so the codes can be organised
def create_app():
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/student.db"
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    # Instantiate db obj
    
    
    db.init_app(app)


    # Import each table from model.py to app.py so that Flask can run
    
    from .models.model import Attendance
    from .models.model import Student
    from .models.model import Tutor
    from .models.model import Course
    from .models.model import Module
    from .models.model import Timetable_Event

    # This import each files of this codebase so it can run in app.
    from . import student, course, module
    from . import check_in
    from .attendance import attendance


    #this registers each of the routes
    app.register_blueprint(student.st)
    app.register_blueprint(course.cs)
    app.register_blueprint(module.md)
    app.register_blueprint(check_in.ci)
    app.register_blueprint(attendance.at)


    with app.app_context():
        #db.drop_all()
        db.create_all()
        

    return app

# decorator @ is used to determine path and trigger proceeding function
@app.get("/")
def hello_world():
 return "<p>Hello, Welcome to our student management system!</p>"