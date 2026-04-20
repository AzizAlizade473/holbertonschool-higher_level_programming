#!/usr/bin/python3
"""
Simple REST API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (do NOT put test data here for checker)
users = {}


@app.route('/')
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user by username or 404"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user via POST request"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        if 'username' not in data:
            return jsonify({"error": "Username is required"}), 400

        username = data['username']

        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        # Add user to dictionary
        users[username] = {
            "username": username,
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }

        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run(debug=True)
