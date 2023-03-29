# Author: Yusuf
# Objective: Using SQLAlchemy for API development.
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
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


 
@app.get("/home")
def test_route():
    return "Test the app"
 
