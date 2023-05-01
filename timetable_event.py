# Author: Jeff
#Purpose: To Fetch The List of timetable events and save in db
#Date; April 13, 2023

from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Timetable_Event, timetable_event_schema
from datetime import datetime

#course route
tt = Blueprint('timetable_event', __name__, url_prefix='/api/timetable-event')


@tt.route("/")
def timetable_event():
    return jsonify({"Welcome": "Timetable Event Page"})

# This allows all Timetable events to be regsitered via Isomnia or Postman
@tt.route("/event", methods= ["POST"])
def reg_event():
    timetable_event_datetime = request.json.get("timetable_event_datetime")
    timetable_event_description = request.json.get("timetable_event_description")
    timetable_event_duration = request.json.get("timetable_event_duration")
    timetable_event_room = request.json.get("timetable_event_room")
    module_id = request.json.get("module_id")

    date = datetime.strptime(timetable_event_datetime, "%m-%d-%Y, %H:%M:%S")


    event = Timetable_Event(timetable_event_datetime = date, timetable_event_description=timetable_event_description, timetable_event_duration = timetable_event_duration, timetable_event_room= timetable_event_room, module_id = module_id)
    db.session.add(event)
    db.session.commit()    

    return jsonify({"message": "success"}), 201



# This allows each event regsitered to be fetched via Isomnia or Postman
@tt.route("/get-event")
def get_event():
    get_events = Timetable_Event.query.all()

    print(list(get_events))
    return timetable_event_schema.dump(get_events)

