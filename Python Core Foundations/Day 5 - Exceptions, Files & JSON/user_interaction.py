from services.student_operations import*
from exceptions.custom_exceptions import*

while True:
    print("\nFile-Based Student Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. View all Students")
    print("4. View Students by Department")
    print("5. Update Student Details")
    print("6. Remove a Student")
    print("7. Check Scholarship Eligibility")
    print("8. Exit")
    

    choice=input("\nEnter choice (e.g. 1): ")

    try:
        if choice=="1":
            sid=input("Enter Student ID: ")
            name=input("Enter Student Name: ").upper()
            age=int(input("Enter student Age: "))
            department=input("Enter Department: ").upper()
            gpa=float(input("Enter GPA of the recent semester results: "))
            add_student(sid,name,age,department,gpa)
            print("\n Student Added Successfully!")

        elif choice=="2":
            sid=input("Enter Student ID: ")
            print(view_student(sid))

        elif choice=="3":
            students=view_all()
            for sid,data in students.items():
                print(f"\nID: {sid}")
                print(f"Name: {data['Name']}")
                print(f"Age: {data['Age']}")
                print(f"Department: {data['Dept']}")
                print(f"GPA: {data['GPA']}")

        elif choice=="4":
            dept=input("Enter Department to view filtered students: ").upper()
            students_in_dept=view_students_by_department(dept)
            if not students_in_dept:
                print(f"\nNo students in {dept} department")
            else:
                print(f"\nStudents in {dept} department")
                for sid,data in students_in_dept.items():
                    print(f"\nID: {sid}")
                    print(f"Name: {data['Name']}")
                    print(f"Age: {data['Age']}")
                    print(f"GPA: {data['GPA']}")

        elif choice=="5":
            sid=input("Enter Student ID to update details: ")
            update_details(sid)
            print("\nStudent details updated successfully!")
            

        elif choice=="6":
            sid=input("Enter ID to remove student: ")
            delete_student(sid)
            print(f"\nStudent with ID {sid} is successfully removed")

        elif choice=="7":
            sid=input("Enter Student ID: ")
            print(sholarship_eligibilty(sid))


        elif choice=="8":
            print("\nExiting....")
            break

        else:
            print("\nInvalid choice")


    except StudentAlreadyExists as e:
        print(e)
        continue

    except StudentNotFound as e:
        print(e)
        continue      

    except NotEligibleForScholarship as e:
        print(e)
        continue

    except ValueError:
        print("\nAge must be a number")




    
