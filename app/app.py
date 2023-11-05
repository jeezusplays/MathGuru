# app.py

from flask import Flask, render_template, request, jsonify
from AIHelper import *
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

# load_dotenv()
PORT = os.getenv('FLASK_PORT')
# print(PORT)


# TODO
@app.route('/question/clean',methods = ["POST"])
def cleanQuestions():
    # Convert the request data to JSON (assuming it's sent as JSON)
    """
    {
        "questions": list[list[string]],
        "level":int
    }
    """
    data = request.get_json()

    if not data:
        return jsonify({"message":"Error - json not provided"},400)
    if "questions" not in data or "level" not in data:
        return jsonify({"message":"Error - wrong json keys"},400)
    
    quesitons = data['questions']
    level = data['level']

    clean_questions = textToQuestions(quesitons,level)

    print("Received data:", clean_questions)

    return jsonify(clean_questions),200

# TODO
@app.route('/question/generate',methods = ["POST"])
def getReading():
    # Convert the request data to JSON (assuming it's sent as JSON)
    """
    JSON structure
    {
        "questions": [{
                        "ocr_question": list["Original question"],
                        "metadata" : {
                            "level": 5,
                            "topics": ["Word Problems", "Multiplication", "Division"],
                            "difficulty": "Medium"
                        }
                    }]
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"message":"Error - json not provided"},400)
    if "questions" not in data:
        return jsonify({"message":"Error - wrong json keys"},400)
    questions = data['questions']

    new_questions = generateQuestions(questions)

    print("Received data:", new_questions)

    return jsonify(new_questions),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
