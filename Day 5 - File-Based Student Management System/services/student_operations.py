from services.file_handling import*

from exceptions.custom_exceptions import*

def add_student(sid,name,age,department,gpa):
    students=load_students()

    if sid in students:
        raise StudentAlreadyExists(f"\nStudent with ID {sid} already exist")
    
    students[sid]={"Name":name,"Age":age,"Dept":department,"GPA":gpa}

    save_students(students)

def view_student(sid):
    students=load_students()

    if sid not in students:
        raise StudentNotFound("\nStudent not found")

    return students[sid]

def view_all():
    return load_students()

def view_students_by_department(dept):
    students=load_students()
    filtered={}
    for sid in students:
        if students[sid]["Dept"]==dept:
            filtered[sid]=students[sid]
    return filtered

def update_details(sid):
    students=load_students()
    if sid not in students:
        raise StudentNotFound("\nStudent not found")
    print("Press Enter to skip updating a field")

    new_name = input("Update name: ").upper()
    new_age = input("Update age: ")
    new_dept = input("Update department: ").upper()
    new_gpa = input("Update GPA: ")

    if new_name:
        students[sid]["Name"] = new_name

    if new_age:
        students[sid]["Age"] = int(new_age)

    if new_dept:
        students[sid]["Dept"] = new_dept

    if new_gpa:
        students[sid]["GPA"] = float(new_gpa)

    save_students(students)
    
def delete_student(sid):
    students=load_students()
    if sid not in students:
        raise StudentNotFound("\nStudent not found")
    del students[sid]
    save_students(students)

def sholarship_eligibilty(sid):
    students=load_students()
    if sid not in students:
        raise StudentNotFound("\nStudent not found")

    age=students[sid]["Age"]
    gpa=students[sid]["GPA"]
    if age<17 or age>23 or gpa<7.0:
        raise NotEligibleForScholarship("Student not eligible for scholarship")
    return "\nEligible for Scholarship"
    













        