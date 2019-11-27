from flask import Flask
from flask_cors import CORS
from datetime import datetime

import os

## Configs
PORT = os.getenv("PORT", 5000)

## App object
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello(): return "Hello, world!"

@app.route("/time")
def time():  return str(datetime)


## Start the app
app.run(port=PORT, host="0.0.0.0")