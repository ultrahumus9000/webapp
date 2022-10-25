from flask import Flask

app = Flask(__name__)

@app.route("/hello")

def welcome():
    return "welcome to my first flask app haha"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)