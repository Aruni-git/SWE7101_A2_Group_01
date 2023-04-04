#Author name: Aruni
#Purpose: Create app.py
#Date: March 14, 2023


from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

import os
#import jsonpickle

app = Flask(__name__)

# the name of the database; add path if necessary
db_name = 'student.db'

# these two lines added to mac os support
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_name)

#support for windows
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home_route():
    return "Welcome to our Stuedent Management System"
