from flask import abort, request
from app import app
import json

@app.route('/')
def index():
	return "hello (?)"

@app.route('/shanghai')
def shanghai():
	return "the weather sucks"

@app.route('/post', methods=['POST'])
def post():
    if not request.json:
        abort(400)
    print (request.json)
    return json.dumps(request.json)


