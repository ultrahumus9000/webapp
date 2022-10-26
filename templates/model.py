import json


def load_db():
    with open('templates/mockdb.json') as f:
        print("i was called")
        return json.load(f)


def save_db():
    print("what is db first",db)
    with open('templates/mockdb.json', 'w') as f:
        return json.dump(db, f)

db = load_db()
