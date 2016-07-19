#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
ml = Flask(__name__)

points = [
    {
        'time': 1,
        'temp': 60,
        'done': False
    },
    {
        'id': 2,
        'temp': 50,
        'done': False
    }
]

@ml.route('/hello')
def hello():
    return "Hello, World!"


@ml.route('/todo/api/ml', methods=['POST'])
def doML():
    if not request.json or not 'temp' in request.json:
        abort(400)
    temp = {
        'id': points[-1]['id'] + 1,
        'temp': request.json['temp'],
        'done': True
    }
    points.append(temp)
    return jsonify({'temp': temp}), 201
	
if __name__ == '__main__':
    ml.run(debug=True)
