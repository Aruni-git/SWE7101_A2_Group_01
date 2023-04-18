from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

#Endpoint to get attendance marks for a particular student
@app.route('/students/<int:student_id>/attendance',methods = ['GET'])
def attendance(student_id):
    #Connect to SQLite database
    conn = sqlite3.connect('attendance.db')
    
    #Create a cursor to execute database queries
    cursor = conn.cursor()
    
    #Get attendance marks for the student
    cursor.execute('SELECT timetable_event_id,attendance_mark FROM attendance WHERE student_id =?',(student_id,))
    attendance_data = [{'timetable_event_id': row[0], 'attendance_mark': row[1]} for row in cursor.fetchall()]
    
    #Close database connection
    cursor.close()
    conn.close()
    
    return jsonify({'attendance': attendance_data})

if __name__ == '__main__':
    app.run()