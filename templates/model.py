import json

def load_db():
    with open('templates/mockdb.json') as f:
        return json.load(f)

db = load_db()
