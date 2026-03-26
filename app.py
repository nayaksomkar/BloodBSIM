"""
BloodSIM Web Application
Flask server for the blood inventory dashboard UI
Serves static files and handles JSON data modifications
"""

import json
import random
from flask import Flask, jsonify, send_from_directory, request

# Flask application instance
app = Flask(__name__)

# Path to the JSON data file
FILE = "blooddata.json"


def read_data():
    """Load blood inventory data from JSON file."""
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save blood inventory data to JSON file."""
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route('/')
def index():
    """Serve the main dashboard HTML page."""
    return send_from_directory('.', 'index.html')


@app.route('/style.css')
def styles():
    """Serve the CSS stylesheet."""
    return send_from_directory('.', 'style.css')


@app.route('/script.js')
def script():
    """Serve the JavaScript file."""
    return send_from_directory('.', 'script.js')


@app.route('/blooddata.json')
def get_data():
    """Serve the JSON data file."""
    return send_from_directory('.', 'blooddata.json')


@app.route('/api/modify', methods=['POST'])
def modify_data():
    """
    API endpoint to modify blood inventory.
    Expects JSON payload: {"action": "add"} or {"action": "remove"}
    """
    data = read_data()
    action = request.json.get('action', 'add')
    
    for blood in data:
        for hospital in data[blood]:
            if action == 'add':
                data[blood][hospital] += random.randint(1, 10)
            else:
                data[blood][hospital] = max(0, data[blood][hospital] - random.randint(1, 10))
    
    save_data(data)
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(port=5000, debug=True)