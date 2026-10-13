import json
import os
from Logic_main import Category, Movement

CATEGORIES_FILE = "categories.json"
MOVEMENTS_FILE = "movements.json"


def save_categories(categories):
    with open(CATEGORIES_FILE, "w") as f:
        json.dump([c.to_dict() for c in categories], f)


def charge_categories():
    if not os.path.exists(CATEGORIES_FILE) or os.path.getsize(CATEGORIES_FILE) == 0:
        return []

    with open(CATEGORIES_FILE, "r") as f:
        data = json.load(f)
        return [Category(d["name"]) for d in data]


def save_movements(movements):
    with open(MOVEMENTS_FILE, "w") as f:
        json.dump([m.to_dict() for m in movements], f)


def charge_movements():
    if not os.path.exists(MOVEMENTS_FILE) or os.path.getsize(MOVEMENTS_FILE) == 0:
        return []

    with open(MOVEMENTS_FILE, "r") as f:
        data = json.load(f)
        return [
            Movement(d["title"], d["amount"], d["category"], d["type"])
            for d in data
        ]