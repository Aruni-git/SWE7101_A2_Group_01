#Author name: Yusuf
#Purpose: Create each tables with its attributes in the database
#Date: March 29, 2023

from sqlalchemy import ForeignKey, ForeignKeyConstraint
from app import db


# Create table for Attendance
class Attendance(db.Model):
    attendance_id = db.Column(db.Integer(), primary_key=True)
    attendance_date = db.Column(db.String(80), nullable=False)
    timetable_event_id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), primary_key=True)


    def __repr__(self) -> str:
        return self.attendance_date
    
# Create table for Tutor
class Tutor(db.Model):
    tutor_id = db.Column(db.Integer(), primary_key=True)
    tutor_forename = db.Column(db.String(80), nullable=False)
    tutor_surname = db.Column(db.String(80), nullable=False)
    tutor_email = db.Column(db.String(80), nullable=False)
    tutor_category = db.Column(db.String(80), nullable=False)
    module_id = db.Column(db.Integer(), primary_key=True)


    def __repr__(self) -> str:
        return self.tutor_forename

# Create table for Student
class Student(db.Model):
    student_id = db.Column(db.Integer(), primary_key=True)
    student_forename = db.Column(db.String(80), nullable=False)
    student_surname = db.Column(db.String(80), nullable=False)
    student_email = db.Column(db.String(80), nullable=False)
    student_category = db.Column(db.String(80), nullable=False)


    def __repr__(self) -> str:
        return self.student_forename

# Create table for Course
class Course(db.Model):
    course_code = db.Column(db.Integer(), primary_key=True)
    course_title = db.Column(db.String(80), nullable=False)
    course_description = db.Column(db.String(120), nullable=False)
    course_level = db.Column(db.Integer(), nullable=False)
    course_credits = db.Column(db.Integer(), nullable=False)

    def __repr__(self) -> str:
        return self.course_title

# Create table for Module
class Module(db.Model):
    module_id = db.Column(db.Integer(), primary_key=True)
    module_title = db.Column(db.String(80), nullable=False)
    module_description = db.Column(db.String(80), nullable=False)
    module_level = db.Column(db.Integer(), nullable=False)
    module_credits = db.Column(db.Integer(), nullable=False)
    course_code = db.Column(db.String(120), nullable=False)
    student_id = db.Column(db.Integer(), nullable=False)
    tutor_id = db.Column(db.Integer(), nullable=False)


    def __repr__(self) -> str:
        return self.module_title

# Create table for Timetable Event
class Timetable_Event(db.Model):
    timetable_event_id = db.Column(db.Integer(), primary_key=True)
    timetable_event_day = db.Column(db.String(80), nullable=False)
    timetable_event_description = db.Column(db.String(80), nullable=False)
    timetable_event_timestart = db.Column(db.String(80), nullable=False)
    timetable_event_duration = db.Column(db.Integer(), nullable=False)
    timetable_event_room = db.Column(db.String(80), nullable=False)
    module_id = db.Column(db.Integer(), nullable=False)


    def __repr__(self) -> str:
        return self.timetable_event_day
    