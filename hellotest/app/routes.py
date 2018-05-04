from flask import abort, request, send_from_directory
from app import app
from app import variable1
from app import dir_name
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
    
    file_name = "badge_00.png"

    full_path = dir_name + file_name

    if  (variable1 == 1):
        variable1 = 0
        return send_from_directory(dir_name, file_name)
    else:
        variable1 = 1
        return "refresh again to see sticker."

@app.route('/qq')
def qq():

    file_name = "QQ QR - Bubbles.png"
    
    return send_from_directory(dir_name, file_name)

@app.route('/banana')
def banana():

    return "banana"

@app.route('/third')
def third():

    return "third"

@app.route('/failure')
def failure():

    return "forever"
