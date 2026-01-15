from flask import Flask, jsonify, request
import sqlite3 as sql

app = Flask(__name__)
DATABASE = 'db.db'



# dummy users
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