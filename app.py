from flask import Flask, render_template, abort, request, redirect, url_for
from datetime import datetime
from templates.model import db, save_db

app = Flask(__name__)

counter = 0


@app.route("/")
def initialStage():
    return render_template("welcome.html", message="LINLIN")


@app.route("/hi")
def welcome():
    global counter
    counter += 1
    print("i am here " + str(counter) + " times")
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


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index)
    except IndexError:
        abort(404)


@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == 'POST':
        card = {"question": request.form['question'], "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('card_view', index=len(db) - 1))
    else:
        return render_template('form.html')


# this is to listen port and call welcome
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
