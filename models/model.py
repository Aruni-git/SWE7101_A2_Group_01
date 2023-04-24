
#Author name: Yusuf
#Purpose: Create each tables with its attributes in the database
#Date: March 29, 2023

from .. import db, ma



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
    student_lastname = db.Column(db.String(80), nullable=False)
    student_email = db.Column(db.String(80), nullable=False)
    student_category = db.Column(db.String(80), nullable=False)


    def __repr__(self) -> str:
        return self.student_forename
    
 # Create Student Schema  
class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("student_id","student_forename", "student_lastname", "student_email", "student_category")

# for a single instance of student 
student_schema = StudentSchema()
# for many instancves of student
students_schema = StudentSchema(many=True)




# Create table for Course
class Course(db.Model):
    course_id = db.Column(db.Integer(), primary_key=True)
    course_code = db.Column(db.Integer(), nullable = False)
    course_title = db.Column(db.String(80), nullable=False)
    course_description = db.Column(db.String(120), nullable=False)
    course_level = db.Column(db.Integer(), nullable=False)
    course_credits = db.Column(db.Integer(), nullable=False)

    def __repr__(self) -> str:
        return self.course_title
    
# Create Course Schema
class CourseSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("course_id","course_code", "course_title", "course_description", "course_level", "course_credits")

# for a single instance of course 
course_schema = CourseSchema()
# for many instancves of courses
courses_schema = CourseSchema(many=True)




# Create table for Module
class Module(db.Model):
    module_id = db.Column(db.Integer(), primary_key=True)
    module_title = db.Column(db.String(80), nullable=False)
    module_description = db.Column(db.String(80), nullable=False)
    module_level = db.Column(db.Integer(), nullable=False)
    module_credits = db.Column(db.Integer(), nullable=False)
    course_id = db.Column(db.String(120), db.ForeignKey('course.course_id'), nullable=False)
    tutor_id = db.Column(db.String(120), db.ForeignKey('tutor.tutor_id'), nullable=False)
    student_enrole_module = db.relationship('Student_Enrole_Module', backref='module')
    semester_is_active = db.Column (db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return self.module_title
    
# Create Module Schema
class ModuleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("course_id","module_id","module_title", "module_description", "module_level", "module_credits",'tutor_id')

# for a single instance of module 
module_schema = ModuleSchema()
# for many instancves of modules
modules_schema = ModuleSchema(many=True)



#Create a table for the students enrolled in a module
class Student_Enrole_Module(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    module_id = db.Column(db.Integer,  db.ForeignKey('module.module_id'), nullable=False)
    student_id = db.Column(db.Integer,  db.ForeignKey('student.student_id'), nullable=False)

    def __repr__(self) -> str:
        return f" module student {self.student_id}"

# Create Module Enrolment Schema
class EnroleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","module_id", "student_id")

# for a single instance of enrol module 
enrol_schema = EnroleSchema()
# for many instances of enrol modules
enrols_schema = EnroleSchema(many=True)


# Create table for Timetable Event
class Timetable_Event(db.Model):
    timetable_event_id = db.Column(db.Integer(), primary_key=True)
    timetable_event_day = db.Column(db.String(80), nullable=False)
    timetable_event_description = db.Column(db.String(80), nullable=False)
    timetable_event_timestart = db.Column(db.DateTime, nullable=False)
    timetable_event_duration = db.Column(db.Integer(), nullable=False)
    timetable_event_room = db.Column(db.String(80), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.module_id'), nullable=False)



    def __repr__(self) -> str:
        return self.timetable_event_day
    
# Create Module Enrolment Schema
class TimetableEventSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("timetable_event_id","timetable_event_day", 
                  "timetable_event_description", "timetable_event_timestart", 
                  "timetable_event_duration", "timetable_event_room",
                   "module_id" )

# for a single instance of enrol module 
timetable_event_schema = TimetableEventSchema()
# for many instances of enrol modules
timetable_event_schemas = TimetableEventSchema(many=True)
    