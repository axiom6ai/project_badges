from flask import Flask
import json, os, glob, csv

app = Flask(__name__)

dir_name = '/Users/brian.xu/Desktop/project_badges/badges/'
numberof_clicks = []
file_names = []
# ^ with extension
sticker_names = []
# ^ without extension
file_paths = glob.glob(os.path.join(dir_name, '*'))
for file in file_paths:
	file_names.append(os.path.basename(file))
	numberof_clicks.append(0)
for png in file_names:
        stickername = os.path.splitext(png)[0]
        sticker_names.append(stickername)

if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata'):
    os.makedirs('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata')
if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/dates.txt'):
	file = open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/dates.txt', 'w')
	file.write('{}')
	file.close()
if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.txt'):
	file = open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.txt', 'w')
	file.write('{}')
	file.close()
datestxt = '/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/dates.txt'
stickerstxt = '/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.txt'

if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.csv'):
	file = open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.csv', 'w')
	csv.writer(file).writerow([''] + sticker_names)
	file.close()
if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/summary.csv'):
	file = open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/summary.csv', 'w')
	file.close()
stickerscsv = '/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.csv'
summarycsv = '/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/summary.csv'


from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)


