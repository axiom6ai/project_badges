from flask import abort, request, send_from_directory
from app import app
from app import variable1, dir_name, numberofclicks
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
    if  variable1 > 0:
        
        file_name = "badge_0" + str(variable1 - 1) + ".png"
        full_path = dir_name + file_name
        
        if variable1 == 2:
            variable1 = 0
        else:
            variable1 = variable1 + 1
        
        return send_from_directory(dir_name, file_name)
    else:
        variable1 = 1
        return "refresh again to see sticker."

@app.route('/qq')
def qq():
    global numberofclicks
    numberofclicks[0] = numberofclicks[0] + 1
    
    file_name = "QQ QR - Bubbles.png"
    return send_from_directory(dir_name, file_name)

@app.route('/axiom')
def axiom():
    global numberofclicks
    numberofclicks[1] = numberofclicks[1] + 1
    
    file_name = "Logo - Circle Crop.png"
    return send_from_directory(dir_name, file_name)

@app.route('/wechat')
def third():
    global numberofclicks
    numberofclicks[2] = numberofclicks[2] + 1

    file_name = "WeChat QR - Bubbles.png"
    return send_from_directory(dir_name, file_name)

@app.route('/seal')
def seal():
    global numberofclicks
    numberofclicks[3] = numberofclicks[3] + 1

    file_name = "Seal.png"
    return send_from_directory(dir_name, file_name)

@app.route('/typo')
def typo():
    global numberofclicks
    numberofclicks[4] = numberofclicks[4] + 1

    file_name = "Typography Two Tone.png"
    return send_from_directory(dir_name, file_name)

@app.route('/print')
def print():

    return str(numberofclicks)
