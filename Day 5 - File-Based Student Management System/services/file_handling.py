import json

def load_students():
    try:
        with open("Day 5 - File-Based Student Management System/students.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}   

    except json.JSONDecodeError:
        return {}  

def save_students(student_data):
    try:
        with open("Day 5 - File-Based Student Management System/students.json","w") as file:
            json.dump(student_data,file)
    except Exception as e:
        print("Error saving file",e)