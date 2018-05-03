from flask import Flask

app = Flask(__name__)

from app import routes

app.run(host='127.0.0.1', port=3000, debug=True)
