# Author: Yusuf
#Purpose: To Fetch The List of Lessons in the past and current and save in DB
#Date; April 20, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Timetable_Event, timetable_event_schema
from datetime import datetime

#timetable route
ttb = Blueprint('Timetable Event', __name__, url_prefix='/timetable_event')


# This allows all lessons timetables to be regsitered via Isomnia
@ttb.route("/register_timetable_event", methods= ["POST"])
def reg_timetable_event():
    timetable_event_day = request.json.get("timetable_event_day")
    timetable_event_description = request.json.get("timetable_event_description")
    timetable_event_timestart = request.json.get("timetable_event_timestart")
    timetable_event_duration = request.json.get("timetable_event_duration")
    timetable_event_room = request.json.get("timetable_event_room")
    module_id = request.json.get("module_id")


    # Convert the timestart which is in string into datetime format 
    lesson_date = datetime.strptime(timetable_event_timestart, "%d/%m/%Y %H:%M:%S")


    timetable = Timetable_Event(timetable_event_day = timetable_event_day, timetable_event_description=timetable_event_description, 
                                timetable_event_timestart = lesson_date, timetable_event_duration= timetable_event_duration,
                                  timetable_event_room = timetable_event_room, module_id=module_id)
    db.session.add(timetable)
    db.session.commit()

    return jsonify({"message": "success"}), 201



# This allows each lessons regsitered to be fetched via Isomnia
@ttb.route("/get-current-semester-lesson")
def get_semester_lesson():
    get_semester_lesson = Timetable_Event.query.all()

    print(list(get_semester_lesson))
    return timetable_event_schema.dump(get_semester_lesson)

