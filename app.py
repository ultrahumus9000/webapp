from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)

counter = 0

@app.route("/")
def initialStage():
    return render_template("welcome.html")
@app.route("/hi")
def welcome():
    global counter
    counter+=1
    print("i am here "+ str(counter) + " times")
    return "you have viewed this for " + str(counter) + " times"
# welcome()
# print("1")
# welcome()
# print("2")
# welcome()
# print("3")
@app.route("/time")

def timeStamp():
    return "welcome to this time" + str(datetime.today())

#this is to listen port and call welcome
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=8080)







