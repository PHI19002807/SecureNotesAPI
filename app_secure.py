from flask import Flask, request, jsonify
import re

app = Flask(__name__)

USERS = {"admin": "secure123"}
TOKENS = {"admin": "secure-token"}
NOTES = {}

def is_valid_input(text):
    return isinstance(text, str) and 1 <= len(text) <= 200 and re.match(r'^[a-zA-Z0-9 .,!?-]+$', text)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if USERS.get(username) == password:
        return jsonify({"token": TOKENS[username]})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/add_note', methods=['POST'])
def add_note():
    token = request.headers.get('Authorization')
    data = request.get_json()
    note = data.get('note')

    user = next((u for u, t in TOKENS.items() if t == token), None)
    if not user or not is_valid_input(note):
        return jsonify({"error": "Unauthorized or invalid input"}), 403

    NOTES.setdefault(user, []).append(note)
    return jsonify({"message": "Note added."})

@app.route('/get_notes', methods=['GET'])
def get_notes():
    token = request.headers.get('Authorization')
    user = next((u for u, t in TOKENS.items() if t == token), None)
    if not user:
        return jsonify({"error": "Unauthorized"}), 403

    return jsonify({"notes": NOTES.get(user, [])})

if __name__ == '__main__':
    app.run(debug=False)

