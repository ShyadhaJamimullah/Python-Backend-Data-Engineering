from services.student_operations import*
from exceptions.custom_exceptions import*


def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice=input("Enter choice: ")

        try:
            if choice=="1":
                sid=input("ID: ")
                name=input("Name: ").upper()
                age=int(input("Age: "))
                dept=input("Department: ").upper()
                gpa=float(input("GPA: "))
                add_student(sid, name, age, dept, gpa)
                print("Student added")

            elif choice=="2":
                sid=input("ID: ")
                print(view_student(sid))

            elif choice=="3":
                students=view_all()
                for sid, data in students.items():
                    print(sid, data)

            elif choice=="4":
                sid=input("ID: ")
                update_details(sid)

            elif choice=="5":
                sid=input("ID: ")
                delete_student(sid)

            elif choice=="6":
                break
            else:
                print("Invalid choice")

        except Exception as e:
            print(e)

def staff_menu():
    while True:
        print("\nStaff Menu")
        print("1. View Student")
        print("2. View All Students")
        print("3. View Students by Department")
        print("4. Check Scholarship Eligibility")
        print("5. Exit")

        choice=input("Enter choice: ")

        try:
            if choice=="1":
                sid=input("Student ID: ")
                print(view_student(sid))

            elif choice=="2":
                students=view_all()
                for sid, data in students.items():
                    print(sid, data)

            elif choice=="3":
                dept=input("Department: ").upper()
                students=view_students_by_department(dept)
                print(students)

            elif choice=="4":
                sid=input("Student ID: ")
                print(sholarship_eligibilty(sid))

            elif choice=="5":
                break
            else:
                print("Invalid choice")

        except Exception as e:
            print(e)

def principal_menu():
    while True:
        print("\nPrincipal Menu")
        print("1. View All Students")
        print("2. View Students by Department")
        print("3. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            print(view_all())

        elif choice=="2":
            dept=input("Department: ").upper()
            print(view_students_by_department(dept))

        elif choice=="3":
            break
        else:
            print("Invalid choice")

def student_menu():
    logged_in_sid = input("Enter your Student ID: ")

    while True:
        print("\nStudent Menu")
        print("1. View My Details")
        print("2. Check Scholarship Eligibility")
        print("3. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                print(get_my_details(logged_in_sid, logged_in_sid))

            elif choice == "2":
                print(sholarship_eligibilty(logged_in_sid))

            elif choice == "3":
                break
            else:
                print("Invalid choice")

        except PermissionError as e:
            print(e)
        except Exception as e:
            print(e)



def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Admin / Office")
        print("2. Staff")
        print("3. Principal")
        print("4. Student")
        print("5. Exit")

        choice = input("Select role: ")

        if choice=="1":
            admin_menu()
        elif choice=="2":
            staff_menu()
        elif choice=="3":
            principal_menu()
        elif choice=="4":
            student_menu()
        elif choice=="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main_menu()





    
