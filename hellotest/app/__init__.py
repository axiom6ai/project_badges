from flask import Flask
import json, os, glob

app = Flask(__name__)

variable1 = 0
dir_name = '/Users/brian.xu/Desktop/project_badges/badges/'
file_names = []
glob = glob.glob(os.path.join(dir_name, '*'))
for file in glob:
	file_names.append(os.path.basename(file))

numberofclicks = [0,0,0,0,0,0]

sticker_dates = {}
json_sticker_dates = json.dumps(sticker_dates)
sticker_counts_total = [0,0,0,0,0,0]
sticker_counts_daily = [0,0,0,0,0,0]

if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata'):
    os.makedirs('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata')
if not os.path.exists('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.txt'):
	file = open('/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.txt', 'w')
	file.write('{}')
	file.close()
stickerstxt = '/Users/brian.xu/desktop/project_badges/hellotest/stickerdata/stickers.txt'


from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)


