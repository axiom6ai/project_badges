from flask import Flask

app = Flask(__name__)

variable1 = 0
dir_name = "/Users/brian.xu/Desktop/project_badges/badges/"
file_names = ["QQ QR - Bubbles.png","Logo - Circle Crop.png","WeChat QR - Bubbles.png","Seal.png","Typography Two Tone.png","sleepy.jpg"]
numberofclicks = [0,0,0,0,0,0]
dateofclicks = ["","","","","",""]

from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)


