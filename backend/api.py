from flask import Flask, jsonify, request

app = Flask(__name__)


users = [
    {'id':1, 'username': 'test'}
]

@app.route("/")
def home():
    return '<h1>Project Tracker API</h1>'

# Endpoint to all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)