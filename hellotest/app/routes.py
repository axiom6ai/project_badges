from flask import abort, request, send_from_directory
from app import app
from app import dir_name, file_names, file_paths
from app import numberof_clicks, stickerstxt, datestxt, stickerscsv
import json, datetime, os

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

@app.route('/sticker00')
def sticker00():
    file_name = file_names[0]
    updatetxts(file_name)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker01')
def sticker01():
    file_name = file_names[1]
    updatetxts(file_name)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker02')
def sticker02():
    file_name = file_names[2]
    updatetxts(file_name)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker03')
def sticker03():
    file_name = file_names[3]
    updatetxts(file_name)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker04')
def sticker04():
    file_name = file_names[4]
    updatetxts(file_name)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker05')
def sleepy():
    file_name = file_names[5]
    if numberof_clicks[0] > 0:
        updatetxts(file_name)

        return send_from_directory(dir_name, file_name)
    else:
        return "not available"

@app.route('/print')
def print():
	
    return str(file_paths)

@app.route('/printing')
def printing():
    updatecsv()

    return 'list'

def updatestickerstxt(stickername):
    #stickers.txt
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)

    today = str(datetime.datetime.now().strftime('%m%d%y'))
    currenttime = str(datetime.datetime.now().strftime('%H:%M:%S'))

    if not stickername in stickers:
        stickers[stickername] = []
        stickers[stickername].append({})
        stickers[stickername][-1][today] = []

    if not today in stickers[stickername][-1]:
        stickers[stickername].append({})
        stickers[stickername][-1][today] = []
    stickers[stickername][-1][today].append(currenttime)

    with open(stickerstxt, 'w') as file:
        file.write(json.dumps(stickers))
        file.close()

def updatedatestxt(stickername, index):
    #dates.txt
    with open(datestxt, 'r') as file:
        dates = json.load(file)

    today = str(datetime.datetime.now().strftime('%m%d%y'))

    if not today in dates:
        dates[today] = []
        for file in file_names:
            dates[today].append({})
            dates[today][-1][os.path.splitext(file)[0]] = 0
    dates[today][index][stickername] += 1                        

    with open(datestxt, 'w') as file:
        file.write(json.dumps(dates))
        file.close()

def updatetxts(file_name):
    global numberof_clicks
    index = file_names.index(file_name)

    numberof_clicks[index] += 1
    stickername = os.path.splitext(file_name)[0]
    updatedatestxt(stickername, index)
    updatestickerstxt(stickername)

def updatecsv():
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)
    with open(datestxt, 'r') as file:
        dates = json.load(file)




