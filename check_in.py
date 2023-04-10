from flask import jsonify, Blueprint
#check in route
ci = Blueprint('check_in', __name__, url_prefix='/check-in')

check_in_code =12345

@ci.route('/')
def check_in():
  return jsonify({"check-in code is ":check_in_code})