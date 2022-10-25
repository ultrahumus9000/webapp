from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def welcome():
    return "welcome to my first flask app"

@app.route("/hello")

def welcome():
    return "welcome to my first flask app"

#this is to listen port and call welcome
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
