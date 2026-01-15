from flask import Flask, jsonify, request, g
import sqlite3

app = Flask(__name__)

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
    get_db().commit()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def home():
    return '<h1>Project Tracker API</h1>'

# Endpoint to all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    for user in query_db('select * from users'):
        print(user)
        users.append(user)
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
    required = ['username', 'password_hash']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Attempt to add the user 
    try:
        result = query_db("INSERT INTO users (username, password_hash) values (?, ?)", (data['username'], data['password_hash']))
        return jsonify({'message': 'User created', 'result': result}), 201
    except sqlite3.IntegrityError:
            return jsonify({'error': 'Email or username already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500
            