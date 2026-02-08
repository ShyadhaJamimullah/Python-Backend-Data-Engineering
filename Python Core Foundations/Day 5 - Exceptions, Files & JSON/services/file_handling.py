import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
FILE_PATH = os.path.join(DATA_DIR, "students.json")


def load_students():
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_students(student_data):
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        with open(FILE_PATH, "w") as file:
            json.dump(student_data, file, indent=4)
    except Exception as e:
        print("Error saving file:", e)
