import json
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
DATA_FILE = 'data.json'

# Load existing data or initialize empty list
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
else:
    data = []

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    content = request.json
    try:
        number = float(content.get('number'))
        name = content.get('name') or None  # Optional
        data.append({'number': number, 'name': name})
        save_data()
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 400

@app.route('/histogram')
def histogram():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
