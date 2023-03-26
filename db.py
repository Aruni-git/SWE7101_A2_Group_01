# Author: Yusuf
# Objective: Using SQLAlchemy for API development.
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Instantiate db obj
db = SQLAlchemy(app)
 