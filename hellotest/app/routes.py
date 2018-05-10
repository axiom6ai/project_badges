from flask import abort, request, send_from_directory
from app import app
from app import variable1, dir_name, file_names, numberofclicks
from app import json_axiom, axiom_key
from app import json_dates, sticker_counts, sticker_counts_daily
import json, datetime

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

    file_name = file_names[0]

    global json_dates
    global sticker_counts
    global sticker_counts_daily

    dates = json.loads(json_dates)
	
    if str(datetime.date.today()) in dates:
        None
    else:
        sticker_counts_daily = [0,0,0,0,0,0]
        dates[str(datetime.date.today())] = {
                                                'sticker_00':0,
                                                'sticker_01':0,
                                                'sticker_02':0,
                                                'sticker_03':0,
                                                'sticker_04':0,
                                                'sticker_05':0
                                            }
    sticker_counts[0] = sticker_counts[0] + 1
    sticker_counts_daily[0] = sticker_counts_daily[0] + 1

    dates[str(datetime.date.today())]['sticker_00'] = sticker_counts_daily[0]
    json_dates = json.dumps(dates)

    return send_from_directory(dir_name, file_name)

@app.route('/axiom')
def axiom():
    global json_dates
    global sticker_counts
    global sticker_counts_daily

    dates = json.loads(json_dates)
	
    if str(datetime.date.today()) in dates:
        None
    else:
        sticker_counts_daily = [0,0,0,0,0,0]
        dates[str(datetime.date.today())] = {
                                                'sticker_00':0,
                                                'sticker_01':0,
                                                'sticker_02':0,
                                                'sticker_03':0,
                                                'sticker_04':0,
                                                'sticker_05':0
                                            }
    sticker_counts[1] = sticker_counts[1] + 1
    sticker_counts_daily[1] = sticker_counts_daily[1] + 1

    dates[str(datetime.date.today())]['sticker_01'] = sticker_counts_daily[1]
    json_dates = json.dumps(dates)

    return send_from_directory(dir_name, file_name)

@app.route('/wechat')
def third():
    global numberofclicks
    numberofclicks[2] = numberofclicks[2] + 1

    file_name = file_names[2]

    global json_dates
    global sticker_counts
    global sticker_counts_daily

    dates = json.loads(json_dates)
	
    if str(datetime.date.today()) in dates:
        None
    else:
        sticker_counts_daily = [0,0,0,0,0,0]
        dates[str(datetime.date.today())] = {
                                                'sticker_00':0,
                                                'sticker_01':0,
                                                'sticker_02':0,
                                                'sticker_03':0,
                                                'sticker_04':0,
                                                'sticker_05':0
                                            }
    sticker_counts[2] = sticker_counts[2] + 1
    sticker_counts_daily[2] = sticker_counts_daily[2] + 1

    dates[str(datetime.date.today())]['sticker_02'] = sticker_counts_daily[2]
    json_dates = json.dumps(dates)

    return send_from_directory(dir_name, file_name)

@app.route('/seal')
def seal():
    global numberofclicks
    numberofclicks[3] = numberofclicks[3] + 1

    file_name = file_names[3]

    global json_dates
    global sticker_counts
    global sticker_counts_daily

    dates = json.loads(json_dates)
	
    if str(datetime.date.today()) in dates:
        None
    else:
        sticker_counts_daily = [0,0,0,0,0,0]
        dates[str(datetime.date.today())] = {
                                                'sticker_00':0,
                                                'sticker_01':0,
                                                'sticker_02':0,
                                                'sticker_03':0,
                                                'sticker_04':0,
                                                'sticker_05':0
                                            }   
    sticker_counts[3] = sticker_counts[3] + 1
    sticker_counts_daily[3] = sticker_counts_daily[3] + 1

    dates[str(datetime.date.today())]['sticker_03'] = sticker_counts_daily[3]
    json_dates = json.dumps(dates)

    return send_from_directory(dir_name, file_name)

@app.route('/typo')
def typo():
    global numberofclicks
    numberofclicks[4] = numberofclicks[4] + 1

    file_name = file_names[4]

    global json_dates
    global sticker_counts
    global sticker_counts_daily

    dates = json.loads(json_dates)
	
    if str(datetime.date.today()) in dates:
        None
    else:
        sticker_counts_daily = [0,0,0,0,0,0]
        dates[str(datetime.date.today())] = {
                                                'sticker_00':0,
                                                'sticker_01':0,
                                                'sticker_02':0,
                                                'sticker_03':0,
                                                'sticker_04':0,
                                                'sticker_05':0
                                            }
    sticker_counts[4] = sticker_counts[4] + 1
    sticker_counts_daily[4] = sticker_counts_daily[4] + 1

    dates[str(datetime.date.today())]['sticker_04'] = sticker_counts_daily[4]
    json_dates = json.dumps(dates)

    return send_from_directory(dir_name, file_name)

@app.route('/sleepy')
def sleepy():
    global numberofclicks
    file_name = file_names[5]

    global json_dates
    global sticker_counts
    global sticker_counts_daily

    dates = json.loads(json_dates)
	
    if str(datetime.date.today()) in dates:
        None
    else:
        sticker_counts_daily = [0,0,0,0,0,0]
        dates[str(datetime.date.today())] = {
                                                'sticker_00':0,
                                                'sticker_01':0,
                                                'sticker_02':0,
                                                'sticker_03':0,
                                                'sticker_04':0,
                                                'sticker_05':0
                                            }
    sticker_counts[5] = sticker_counts[5] + 1
    sticker_counts_daily[5] = sticker_counts_daily[5] + 1

    dates[str(datetime.date.today())]['sticker_05'] = sticker_counts_daily[5]
    json_dates = json.dumps(dates)

    if numberofclicks[0] > 0:
        numberofclicks[5] = numberofclicks[5] + 1
        return send_from_directory(dir_name, file_name)
    else:
        return "not available"

@app.route('/test')
def test():
    file_name = file_names[1]

    global json_axiom
    global axiom_key

    axiom_key = axiom_key + 1
    axiom = json.loads(json_axiom)
    axiom['axiom_date'][str(axiom_key)] = str(datetime.date.today())
    json_axiom = json.dumps(axiom)

    return send_from_directory(dir_name, file_name)

@app.route('/datetest')
def date():
    return json_axiom

@app.route('/dates')
def dates():

	return json_dates


@app.route('/print')
def print():
	
    return str(numberofclicks)


@app.route('/printing')
def printing():
    for n in range(len(numberofclicks)):
        if numberofclicks[n] > 0:
            return send_from_directory(dir_name, file_names[n])

    return "list"

