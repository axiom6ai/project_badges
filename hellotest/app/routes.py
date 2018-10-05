from flask import abort, request, send_from_directory, render_template
from app import app
from app import dir_name, file_names, sticker_names, file_paths
from app import numberof_clicks, stickerstxt, datestxt, stickerscsv, summarycsv
import json, datetime, os, csv
import calendar

@app.route('/sticker00')
def sticker00():
    if datetime.datetime.today().weekday() > 4:
        file_name = file_names[0]
        updatetxts(file_name)

        return send_from_directory(dir_name, file_name)
    return "not available"

@app.route('/sticker01')
def sticker01():
    if datetime.datetime.today().weekday() < 5:
        file_name = file_names[1]
        updatetxts(file_name)

        return send_from_directory(dir_name, file_name)
    return "not available"

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
    return "not available"

@app.route('/allstickers')
def allstickers():
    with open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/summary.csv', 'r') as file:
        summary = list(csv.reader(file))

    githubstickers = [
                    "https://user-images.githubusercontent.com/35032810/46395675-c0f51180-c71f-11e8-9950-0f99fed91e1c.png",
                    "https://user-images.githubusercontent.com/35032810/46395685-c6525c00-c71f-11e8-842e-b2625876dbcb.png",
                    "https://user-images.githubusercontent.com/35032810/46395686-c6525c00-c71f-11e8-86c4-ed9d8ac11217.png",
                    "https://user-images.githubusercontent.com/35032810/46395687-c7838900-c71f-11e8-9365-ff58ee1f4890.png",
                    "https://user-images.githubusercontent.com/35032810/46395690-c81c1f80-c71f-11e8-8d70-5d58203e00c2.png",
                    "https://user-images.githubusercontent.com/35032810/46395692-c8b4b600-c71f-11e8-8a9b-29703484c928.png"
                    ]
    unlocked = []

    for i in range(1, len(summary[1])):
        if int(summary[1][i]) > 0:
            unlocked.append((githubstickers[i-1], summary[1][i]))
                
    return render_template('test.html', unlocked=unlocked)

@app.route('/calendar')
def calendartest():
    with open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.csv', 'r') as file:
        stickers = list(csv.reader(file))
    test = []

    for row in stickers:
        if len(row[0]) > 1:
            test.append(int(row[0][3:4]))
    print(test)

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    date = datetime.date(2018, 6, 10)

    c =  calendar.Calendar(firstweekday=6)
    month = c.monthdays2calendar(date.year, date.month)
    
    #return str(month)
    return render_template('calendar.html', month=month, weekdays=weekdays, months=months, date=date, test=test)

####TESTING_SECTION####
@app.route('/test')
def test():
    updatecsvdaily()
	
    return 'ok'

@app.route('/testing')
def testing():
    updatecsv()

    return 'ok'

@app.route('/total')
def summary():
    updatesummarycsv()

    return 'ok'

@app.route('/day')
def count():
    date = request.args.get('date')
    return daycount(date)

@app.route('/dates')
def dates():
    with open(datestxt, 'r') as file:
        dates = json.dumps(json.load(file))

    return dates

@app.route('/stickers')
def stickers():
    with open(stickerstxt, 'r') as file:
        stickers = json.dumps(json.load(file))

    return stickers

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
    #initial update ? all current days
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)
    with open(datestxt, 'r') as file:
        dates = json.load(file)

    for date in dates:
        datekeys = list(dates[date])
        firstrow = 1
        n = 1
        rownumber = 0
        daycount = 0

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
                if (firstrow == 1):
                    daycount += dates[date][index][stickername]

            rownumber += 1

            if (n == 0):
                finalrow = []
                
                for sticker in dates[date]:
                    index = datekeys.index(sticker)
                    stickername = sticker_names[index]
                    finalrow.append(dates[date][index][stickername])

                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([daycount] + finalrow) 
            elif (firstrow == 1):
                firstrow = 0
                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([date] + row) 
            else:
                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([''] + row) 

def updatecsvdaily():
    #daily update
    with open(stickerstxt, 'r') as file:
        stickers = json.load(file)
    with open(datestxt, 'r') as file:
        dates = json.load(file)

    today = str(datetime.datetime.now().strftime('%m%d%y'))
    
    if today in dates:
        datekeys = list(dates[today])
        firstrow = 1
        n = 1
        rownumber = 0
        daycount = 0

        while (n > 0):
            row = []
            n = len(sticker_names)

            for sticker in dates[today]:
                index = datekeys.index(sticker)
                stickername = sticker_names[index]

                if (dates[today][index][stickername] > rownumber):
                    row.append(stickers[stickername][today][rownumber])
                else:
                    row.append('')    
                    n -= 1
                if (firstrow == 1):
                    daycount += dates[today][index][stickername]

            rownumber += 1

            if (n == 0):
                finalrow = []
                
                for sticker in dates[today]:
                    index = datekeys.index(sticker)
                    stickername = sticker_names[index]
                    finalrow.append(dates[today][index][stickername])

                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([daycount] + finalrow) 
            elif (firstrow == 1):
                firstrow = 0
                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([today] + row) 
            else:
                with open(stickerscsv, 'a') as file:
                    csv.writer(file).writerow([''] + row) 

## for updating daily -> updatecsv() queues updatecsvdaily(), which will then queue itself for sorrowful eternity

def updatesummarycsv():
    with open(datestxt, 'r') as file:
        dates = json.load(file)

    totalcount = 0
    row = []

    today = str(datetime.datetime.now().strftime('%m%d%y'))
    if today in dates:
        datekeys = list(dates[today])
        for sticker in dates[today]:
            index = datekeys.index(sticker)
            stickername = sticker_names[index]

            stickercount = 0
            for date in dates:
                stickercount += dates[date][index][stickername]
            row.append(stickercount)
            totalcount += stickercount
     
        with open(summarycsv, 'w') as file:
            csv.writer(file).writerow([''] + sticker_names)
            csv.writer(file).writerow([totalcount] + row) 

def daycount(date):
    with open(datestxt, 'r') as file:
        dates = json.load(file)

    if date in dates:
        count = 0
        datekeys = list(dates[date])
        for sticker in dates[date]:
            index = datekeys.index(sticker)
            stickername = sticker_names[index]
            count += dates[date][index][stickername]
        return str(count)
    else:
        return 'sorry'
