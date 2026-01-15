from flask import Flask, jsonify, request, g
from flask_cors import CORS
import bcrypt
import sqlite3

app = Flask(__name__)
CORS(app)

# Set bcrypt salt to 10
salt = bcrypt.gensalt(rounds=10)

# Connect to database
DATABASE = 'db.db'

# Reference for query_db and get_db: https://flask.palletsprojects.com/en/stable/patterns/sqlite3/
def get_db():
    # Checks for active database
    db = getattr(g, '_database', None)
    # If there is no active database, connect to the define database above
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    # Define cursor, use query and args
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    # Commit any changes necessary to the database
    get_db().commit()
    cur.close()
    # If one is true, commit only the first item recieved
    return (rv[0] if rv else None) if one else rv

# Placeholder index
@app.route("/")
def home():
    return '<h1>Project Tracker API</h1>'

# Endpoint to all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    for user in query_db('select * from users'):
        # print(user)
        users.append({"id": user[0], "username": user[1], "password_hash": user[2]})
    return jsonify(users)
    

# Get specific user via username
@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    user = query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user)

# Create user
@app.route('/api/users', methods=['POST'])
def create_user():
    # Grab data from post body
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Required fields
    required = ['username', 'password']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
        
    # Hash the password with bcrypt
    password = data['password'].encode("utf-8")
    password_hash = bcrypt.hashpw(password, salt)

    # Attempt to add the user 
    try:
        query_db("INSERT INTO users (username, password_hash) values (?, ?)", (data['username'], str(password_hash)))
        return jsonify({'message': 'User created'}), 201
    except sqlite3.IntegrityError:
            return jsonify({'error': 'Email or username already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500
            

