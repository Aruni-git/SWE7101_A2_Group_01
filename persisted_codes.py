#Author name: Likitha
#Purpose: If code already persists,API returning error message
#Date: April 11, 2023

from flask import Flask,request,jsonify

app = Flask(__name__)

#Sample list of codes that have already been persisted
persisted_codes = ['VSO654','FTE321','HGY967']

@app.route('/check_in', methods = ['POST'])
def check_in():
    #Extract the code from the request data
    code = request.json.get('code')
    
    #Check if the code already exists in the persisted codes list
    if code in persisted_codes:
        return jsonify({'message': 'Code already exists'}),400
    else:
        return jsonify ({'message': 'Code does not exist'}),404
    
if __name__ == '__main__':
    app.run()
    
