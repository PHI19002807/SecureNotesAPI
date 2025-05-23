from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {"admin": "1234"}
NOTES = []

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if USERS.get(username) == password:
        return jsonify({"token": "not-so-secure-token"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.get_json()
    note = data['note']
    NOTES.append(note)
    return jsonify({"message": "Note added."})

@app.route('/get_notes', methods=['GET'])
def get_notes():
    return jsonify({"notes": NOTES})

if __name__ == '__main__':
    app.run(debug=False)

