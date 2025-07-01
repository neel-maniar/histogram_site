from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
data = []  # In-memory storage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    number = request.json.get('number')
    try:
        number = float(number)
        data.append(number)
        return jsonify(success=True)
    except:
        return jsonify(success=False), 400

@app.route('/histogram')
def histogram():
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)