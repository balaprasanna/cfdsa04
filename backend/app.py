from flask import Flask, render_template
from flask_cors import CORS
from datetime import datetime

import os

## Configs
PORT = os.getenv("PORT", 5000)

## App object
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    resp = """
    <h1> Demo links...</h1>
    <ol>
    <li> <a href="/demo"> demo </a> </li>
    <li> <a href="/mobilenet"> Image Classfication </a> </li>
    <ol>
    """
    return resp

@app.route("/demo")
def demo():  
    return render_template("demo/index.html")


@app.route("/mobilenet")
def mobilenet(): 
    return render_template("mobilenet/index.html")


@app.route("/time")
def time():  return str(datetime.now())


## Start the app
app.run(port=PORT, host="0.0.0.0")