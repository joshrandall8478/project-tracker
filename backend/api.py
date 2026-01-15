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
    
    data = {"id": user[0], "username": user[1], "password_hash": user[2]}
    return jsonify(data)

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
        query_db("INSERT INTO users (username, password_hash) values (?, ?)", (data['username'], str(password_hash.decode('utf-8'))))
        return jsonify({'message': 'User created'}), 201
    except sqlite3.IntegrityError:
            return jsonify({'error': 'Email or username already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500
            

# Authenticate user
@app.route('/api/login', methods=['GET'])
def authenticate():
    # Grab data from post body
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Required fields
    required = ['username', 'password']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
        
    # Encode the password in utf-8
    password = data['password'].encode("utf-8")
    

    username = data['username']


    # Get user
    user = query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    queryResult = {"id": user[0], "username": user[1], "password_hash": user[2]}
    password_hash = queryResult['password_hash']

    # print(queryResult["password_hash"])
    # print(password_hash)
    print(password)
    print(password_hash)
    if bcrypt.checkpw(password, password_hash.encode('utf-8')):
        return jsonify({'message': 'Successfully Authenticated'}), 202
    else:
        return jsonify({'message': 'Authorization Failed'}), 401

# Create project
@app.route('/api/projects', methods=['POST'])
def create_project():
    # Grab data from post body
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Required fields
    required = ['user_id', 'name']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
        
    description = ""
    if data['description']:
        description = data['description']

    # Attempt to add the user 
    try:
        query_db("INSERT INTO projects (user_id, name, description) values (?, ?, ?)", (data['user_id'], data['name'], description))
        return jsonify({'message': 'Project Created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create tasks
@app.route('/api/tasks', methods=['POST'])
def create_task():
    # Grab data from post body
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Required fields
    required = ['project_id', 'title']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Attempt to add the user 
    try:
        query_db("INSERT INTO tasks (project_id, title) values (?, ?)", (data['project_id'], data['title']))
        return jsonify({'message': 'Task Created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update task status
@app.route('/api/tasks', methods=['PUT'])
def update_task():
    # Grab data from post body
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Required fields
    required = ['id', 'status']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Attempt to add the user 
    try:
        query_db("UPDATE tasks SET status = ? WHERE id = ?", (data['status'], data['id']))
        return jsonify({'message': 'Task Updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all projects based on username
@app.route('/api/projects/<username>', methods=['GET'])
def get_user(username):
    user = query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    data = {"id": user[0], "username": user[1], "password_hash": user[2]}

    user_id = data[id]

    projects = []
    for project in query_db('select * from projects where user_id = ?', user_id):
        # print(user)
        projects.append({"id": project[0], "user_id": project[1], "name": project[2], "description": project[3]})
    return jsonify(projects)

# Get all tasks based on project ID
@app.route('/api/tasks/<project_id>', methods=['GET'])
def get_user(project_id):
    tasks = query_db('SELECT * FROM tasks WHERE project_id = ?', [project_id], one=True)
    
    if tasks is None:
        return jsonify({'error': 'Tasks not found'}), 404
    
    result = []
    for task in tasks:
        # print(user)
        result.append({"id": task[0], "project_id": task[1], "title": task[2], "status": task[3], "created_at": task[4]})
    return jsonify(result)
