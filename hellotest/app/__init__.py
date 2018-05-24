from flask import Flask
import json, os

app = Flask(__name__)

variable1 = 0
dir_name = '/Users/brian.xu/Desktop/project_badges/badges/'
file_names = ["sticker_00.png","sticker_01.png","sticker_02.png","sticker_03.png","sticker_04.png","sticker_05.png"]
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
latest = ""
from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)


