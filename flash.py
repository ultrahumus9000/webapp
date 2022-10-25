from flask import Flask
from datetime import datetime

app = Flask(__name__)

counter = 0

@app.route("/")
def welcome():
    global counter
    counter+=1
    return "welcome to my first flask app " + str(counter) + " times"
@app.route("/time")

def timeStamp():
    return "welcome to this time" + str(datetime.today())

#this is to listen port and call welcome
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)







