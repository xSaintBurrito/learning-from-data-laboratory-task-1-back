from flask import Flask, session, request
from flask_session import Session
import json
app = Flask(__name__)
app.secret_key = '786dsadhalhd7sady8asdhyaksdnas9'
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.route('/saveUser', methods=['POST'])
def saveUser():
    data = request.get_json()
    if "users" in session:
        print(session["users"])
        session["users"].append(data)
    else:
        session["users"] = []
    return ""

@app.route('/flushSession', methods=['GET'])
def flushSession():
    if "users" in session:
        session["users"] = []
    else:
        session["users"] = []
    return ""


@app.route('/getUsersInfo', methods=['GET'])
def getUserInfo():
    if "users" in session:
        return json.dumps(session["users"])
    else:
        return ""



app.run(port=5001,host="0.0.0.0")