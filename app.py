# import the Flask class from the flask library
from flask import Flask
# create an instance of the Flask class and assign to app
# __name__ refers to the default path of the package
app = Flask(__name__)
# decorator @ is used to determine path and trigger proceeding function
@app.get("/")
def hello_world():
 return "<p>Hello, World!</p>"