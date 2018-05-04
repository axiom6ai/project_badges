from flask import abort, request, send_from_directory
from app import app
from app import variable1
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
    global variable1
    
    dir_name = "/Users/brian.xu/Desktop/project_badges/badges/"
    file_name = "badge_00.png"

    full_path = dir_name + file_name

    if  (variable1 == 1):
        variable1 = 0
        return send_from_directory(dir_name, file_name)
    else:
        variable1 = 1
        return "no sticker for you."

@app.route('/laptop')
def laptop():

    return "laptop"

@app.route('/banana')
def banana():

    return "banana"

@app.route('/third')
def third():

    return "third"

@app.route('/failure')
def failure():

    return "forever"
