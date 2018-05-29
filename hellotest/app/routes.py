from flask import abort, request, send_from_directory
from app import app
from app import dir_name, file_names, file_paths
from app import numberof_clicks, stickerstxt, datestxt
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
    global numberof_clicks
    numberof_clicks[file_names.index(file_name)] += 1

    stickername = os.path.splitext(file_name)[0]
    updatedatestxt(stickername, file_names.index(file_name))
    updatestickerstxt(stickername)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker01')
def sticker01():
    
    file_name = file_names[1]
    global numberof_clicks
    numberof_clicks[file_names.index(file_name)] += 1

    stickername = os.path.splitext(file_name)[0]
    updatedatestxt(stickername, file_names.index(file_name))
    updatestickerstxt(stickername)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker02')
def sticker02():
   
    file_name = file_names[2]
    global numberof_clicks
    numberof_clicks[file_names.index(file_name)] += 1

    stickername = os.path.splitext(file_name)[0]
    updatedatestxt(stickername, file_names.index(file_name))
    updatestickerstxt(stickername)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker03')
def sticker03():
   
    file_name = file_names[3]
    global numberof_clicks
    numberof_clicks[file_names.index(file_name)] += 1

    stickername = os.path.splitext(file_name)[0]
    updatedatestxt(stickername, file_names.index(file_name))
    updatestickerstxt(stickername)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker04')
def sticker04():
   
    file_name = file_names[4]
    global numberof_clicks
    numberof_clicks[file_names.index(file_name)] += 1

    stickername = os.path.splitext(file_name)[0]
    updatedatestxt(stickername, file_names.index(file_name))
    updatestickerstxt(stickername)

    return send_from_directory(dir_name, file_name)

@app.route('/sticker05')
def sleepy():

    global numberof_clicks
    if numberof_clicks[0] > 0:
        
        file_name = file_names[5]
        numberof_clicks[file_names.index(file_name)] += 1

        stickername = os.path.splitext(file_name)[0]
        updatedatestxt(stickername, file_names.index(file_name))
        updatestickerstxt(stickername)

        return send_from_directory(dir_name, file_name)
    else:
        return "not available"

@app.route('/dates')
def dates():
    return json_sticker_dates

@app.route('/print')
def print():
	
    return str(file_paths)


@app.route('/printing')
def printing():
    for n in range(len(numberofclicks)):
        if numberofclicks[n] > 0:
            return send_from_directory(dir_name, file_names[n])

    return "list"

def updatestickerstxt(stickername):
    #stickers.txt
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)

    today = str(datetime.datetime.now().strftime('%m%d%y'))
    currenttime = str(datetime.datetime.now().strftime('%H:%M:%S'))

    if stickername in stickers:
        None
    else:
        stickers[stickername] = []
        stickers[stickername].append({})
        stickers[stickername][-1][today] = []

    if today in stickers[stickername][-1]:
        None
    else:
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

    if today in dates:
        None
    else:
        dates[today] = []
        for file in file_names:
            dates[today].append({})
            dates[today][-1][os.path.splitext(file)[0]] = 0
    dates[today][index][stickername] += 1                        

    with open(datestxt, 'w') as file:
        file.write(json.dumps(dates))
        file.close()


