# import the Flask class from the flask library
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 

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

    # these two lines added to mac os support
    db_name = 'student.db'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_name)
    

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
    from . import checkin_duration
    from .attendance import attendance
    from . import timetable_event
    from . import previous_attendance
    from . import persisted_codes
    from . import student, course, module,tutor,timetable


    #this registers each of the routes
    app.register_blueprint(student.st)
    app.register_blueprint(course.cs)
    app.register_blueprint(module.md)
    app.register_blueprint(checkin_duration.gc)
    app.register_blueprint(attendance.at)
    app.register_blueprint(timetable_event.tt)
    app.register_blueprint(previous_attendance.gm)
    app.register_blueprint(persisted_codes.pc)

    app.register_blueprint(tutor.tt)
    app.register_blueprint(timetable.ttb)


    with app.app_context():
        # db.drop_all()
        db.create_all()
        

    return app

# decorator @ is used to determine path and trigger proceeding function
@app.get("/api")
def hello_world():
 return "<p>Hello, Welcome to our student management system!</p>"