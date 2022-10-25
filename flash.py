from flask import Flask
from datetime import datetime

app = Flask(__name__)

counter = 0

@app.route("/")
def initialStage():
    return"welcome to my first flask app"
@app.route("/")
def welcome():
    global counter
    counter+=1
    return "you have viewed this for " + str(counter) + " times"

welcome()
print("haha"
      "")
@app.route("/time")

def timeStamp():
    return "welcome to this time" + str(datetime.today())

#this is to listen port and call welcome
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)







