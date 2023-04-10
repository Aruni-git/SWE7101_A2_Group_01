#Author name: Jeffrey
#Purpose: Accept only code P to mark attendance present
#Date: April 01, 2023
from flask import Flask, request, make_response, jsonify, Blueprint
from app import app
from check_in import check_in_code 
app = Flask(__name__)

@app.route('/check-in', methods=['GET', 'POST'])
def attendance():
    checkIn = request.json.get['check_in_code']
    if checkIn == check_in_code:
        return jsonify ({"Attendance Has Been Marked"})
    if checkIn != check_in_code:
        return jsonify ({"error":"Invalid Input, Attendance Has Not Been Marked"})

