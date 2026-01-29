from datetime import datetime

students={}
attendance_count={}

def student_database():
    sid=input("Enter student id:")
    if sid in students:
        print("Student id already exists")
    else:
        name=input("Enter student name:")
        
        students[sid]={"Name":name,"Attendance":{}}
        print(f"\n{name} was added to the student database")

def weekend(date_str):
    date_input=datetime.strptime(date_str,'%d-%m-%Y')
    return date_input.weekday()>=5 

def mark_attendance():
    sid=input("Enter student id:")

    if sid not in students:
        print("Student not found")
        return
    
    date=input("Enter the date (DD-MM-YYYY):")

    if weekend(date):
        print("This is weekend")
        return

    
    status=input("Enter attendance status (present/absent):").lower()
    students[sid]["Attendance"][date]=status

    if sid not in attendance_count:
        attendance_count[sid]={"Count":0}

    if status=="present":
        attendance_count[sid]["Count"]+=1

    elif status=="absent":
        print("Student marked absent")

    print(sid,students[sid])


def view_attendence():

    view=input("View (all / specific)").lower()

    if view=="all":
        for sid in students:
            print(sid,students[sid])

    
    sid=input("Enter student id to view attendence status:")
    if sid in students:
        print(sid,attendance_count[sid])

def eligibility():
    sid=input("Enter student id:")
    if sid in students and attendance_count[sid]["Count"]>20:
        print(f"{sid} is eligibile")
    else:
        print(f"{sid} not eligible")

    

while True:
    print("\n\nAttendence Tracker")
    print("1. Add Student:")
    print("2. Mark Attendence")
    print("3. View Attendence")
    print("4. Check Eligibility")
    print("5. Exit")

    choice=input("Enter action to perform (1,2,3,4,5,6):")
    if choice=="1":
        student_database()
    elif choice=="2":
        mark_attendance()
    elif choice=="3":
        view_attendence()
    elif choice=="4":
        eligibility()
    elif choice=="5":
        print("Exit")
    break

