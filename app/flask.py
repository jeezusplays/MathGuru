# app.py

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv()
PORT = os.getenv('FLASK_PORT')
print(PORT)



@app.route('/parse/questions',methods = ["POST"])
def getReading():
    # Convert the request data to JSON (assuming it's sent as JSON)
    data = request.json
    quesitons = data['questions']
    level = data['level']


    print("Received data:", data)

    return jsonify({"message": "Data received successfully!"}),200

@app.route('/generate/questions',methods = ["GET"])
def getReading():
    # Convert the request data to JSON (assuming it's sent as JSON)
    data = request.json
    quesitons = data['questions']
    level = data['level']



    print("Received data:", data)

    return jsonify({"message": "Data received successfully!"}),200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
