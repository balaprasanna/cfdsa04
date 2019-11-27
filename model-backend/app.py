from flask import Flask, render_template, jsonify
from flask_cors import CORS
from datetime import datetime
import os, json

## Configs
PORT = os.getenv("PORT", 5002)

## App object
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello(): return "Hello, world!"

@app.route("/train")
def train():  return "Not implemented yet"

@app.route("/model")
def getmodel():
    try:
        with open("static/model.json") as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({ "error": e })

@app.route("/time")
def time():  return str(datetime.now())


## Start the app
app.run(port=PORT, host="0.0.0.0")