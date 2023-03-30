# import the Flask class from the flask library
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

# create an instance of the Flask class and assign to app
# __name__ refers to the default path of the package
app = Flask(__name__)

# decorator @ is used to determine path and trigger proceeding function
@app.get("/")
def hello_world():
 return "<p>Hello, Welcome to our student management system!</p>"
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

 
# Instantiate db obj
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

# @app.get("/home")
# def test_route():
#     return "Test the app"
 
@app.get("/get-json")
def get_json():
 response = [{"forename":"Aruni"},{"surname":"Gunapala"}]
 return jsonify (response)
