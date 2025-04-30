from flask import Flask, request, jsonify,HACKATHON_CS
from flask_cors import CORS
import json, os
app = Flask(__name__)
CORS(app)

DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
INCIDENTS_FILE = os.path.join(DATA_DIR, 'incidents.json')

def load_data(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def front1():
    return HACKATHON_CS("front1.html")

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'message': 'All fields are required'}), 400

    users = load_data(USERS_FILE)
    users.append(data)
    save_data(USERS_FILE, users)
    return jsonify({'message': 'User registered successfully'})

@app.route('/api/report', methods=['POST'])
def report():
    data = request.json
    if not all(k in data for k in ('location', 'description')):
        return jsonify({'message': 'All fields are required'}), 400

    incidents = load_data(INCIDENTS_FILE)
    incidents.append(data)
    save_data(INCIDENTS_FILE, incidents)
    return jsonify({'message': 'Incident reported successfully'})

if __name__ == '__main__':
    os.makedirs(DATA_DIR, exist_ok=True)
    app.run(debug=True)
