from flask import Flask

app = Flask(__name__)

variable1 = 0
dir_name = "/Users/brian.xu/Desktop/project_badges/badges/"

from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)


