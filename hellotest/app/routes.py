from flask import abort, request, send_from_directory
from app import app
from app import dir_name, file_names, sticker_names, file_paths
from app import numberof_clicks, stickerstxt, datestxt, stickerscsv
import json, datetime, os, csv

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
    if numberof_clicks[0] > 0:
        file_name = file_names[5]
        updatetxts(file_name)

        return send_from_directory(dir_name, file_name)
    else:
        return "not available"

####TESTING_SECTION####
@app.route('/test')
def test():
	
    return str(file_paths)

@app.route('/testing')
def testing():
    updatecsv()

    return 'list'


####/TESTING_SECTION####
def updatestickerstxt(stickername):
    #stickers.txt
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)

    today = str(datetime.datetime.now().strftime('%m%d%y'))
    currenttime = str(datetime.datetime.now().strftime('%H:%M:%S'))

    if not stickername in stickers:
        stickers[stickername] = {}
        stickers[stickername][today] = []

    if not today in stickers[stickername]:
        stickers[stickername][today] = []
    stickers[stickername][today].append(currenttime)

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
    stickername = sticker_names[index]
    updatedatestxt(stickername, index)
    updatestickerstxt(stickername)

def updatecsv():
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)
    with open(datestxt, 'r') as file:
        dates = json.load(file)

    for date in dates.keys():
        datekeys = list(dates[date])
        firstrow = 1
        n = 1
        rownumber = 0

        while (n > 0):
            row = []
            n = len(sticker_names)

            for sticker in dates[date]:
                index = datekeys.index(sticker)
                stickername = sticker_names[index]

                if (dates[date][index][stickername] > rownumber):
                    row.append(stickers[stickername][date][rownumber])
                else:
                    row.append('')    
                    n -= 1
            rownumber += 1

            if (n == 0):
                finalrow = []
                
                for sticker in dates[date]:
                    index = datekeys.index(sticker)
                    stickername = sticker_names[index]
                    finalrow.append(dates[date][index][stickername])

                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([''] + finalrow) 
            elif (firstrow == 1):
                firstrow = 0
                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([date] + row) 
            else:
                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([''] + row) 
            print(n)



