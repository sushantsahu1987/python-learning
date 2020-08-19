from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    data = {'name': 'sushant', 'age': 33}
    return jsonify(data)

app.run(debug=True, port=5000)