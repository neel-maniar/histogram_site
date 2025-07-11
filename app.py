import json
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
DATA_FILE = 'data.json'

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def write_data(data):
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
        name = content.get('name') or None
        data = read_data()
        data.append({'number': number, 'name': name})
        write_data(data)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 400

@app.route('/histogram')
def histogram():
    data = read_data()
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
