from flask import Flask
import json

app = Flask(__name__)

variable1 = 0
dir_name = "/Users/brian.xu/Desktop/project_badges/badges/"
file_names = ["QQ QR - Bubbles.png","Logo - Circle Crop.png","WeChat QR - Bubbles.png","Seal.png","Typography Two Tone.png","sleepy.jpg"]
numberofclicks = [0,0,0,0,0,0]

axiom = {}
axiom['axiom_date'] = {}
json_axiom = json.dumps(axiom)
axiom_key = 0

dates = {}
json_dates = json.dumps(dates)
sticker_counts = [0,0,0,0,0,0]
sticker_counts_daily = [0,0,0,0,0,0]

from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)


