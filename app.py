# import the Flask class from the flask library
from flask import Flask,jsonify
# create an instance of the Flask class and assign to app
# __name__ refers to the default path of the package
app = Flask(__name__)
# decorator @ is used to determine path and trigger proceeding function
@app.get("/")
def hello_world():
 return "<p>Hello, Welcome to our student management system!</p>"
 
@app.get("/get-json")
def get_json():
 response = [{"forename":"Aruni"},{"surname":"Gunapala"}]
 return jsonify (response)