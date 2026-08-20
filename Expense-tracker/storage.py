import json

DATA_FILE = "data/transactions.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)
