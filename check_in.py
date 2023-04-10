from app import app


from flask import flask, jsonify, Blueprint
#check in route
ci = Blueprint('check_in', __name__, url_prefix='/check-in')

check_in_code =({12345})

@app.route('/check-in')
def check_in():
  return jsonify({"check-in code is ":check_in_code})