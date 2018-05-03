from flask import abort, request, send_from_directory
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

@app.route('/badges')
def axiom_badge():
    dir_name = "/Users/brian.xu/Desktop/project_badges/badges/"
    file_name = "badge_00.png"

    full_path = dir_name + file_name
    return send_from_directory(dir_name, file_name)



