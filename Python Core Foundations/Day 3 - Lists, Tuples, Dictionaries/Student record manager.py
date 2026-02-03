students={}
while True:
    print("\n\n1. Add student")
    print("2. View all students")
    print("3. Update details")
    print("4. Delete student")
    print("5. To exit")
    manage=input("Enter the operation you need to perform (1-4):")

    if manage=="1":
        id=input("\nEnter student id:")
        if id in students:
            print("Warning...Student id already exists")
        else:
            name=input("Enter student name:")
            marks=int(input("Enter marks:"))
            students[id]={"Name":name,"Mark":marks}
            
    elif manage=="2":
        id=input("\nEnter the id to view student details or type all:")
        if id in students:
            print(id,students[id])

        elif id=="all":
            for id in students:
                print(id,students[id])
        else:
            print("No records found")
    
    elif manage=="3":
        id=input("\nEnter student id:")
        if id not in students:
            print("Student record not found")
        else:
            name_change=input("Enter the name:")
            mark_change=int(input("Enter the marks:"))
            students[id].update({"Name":name_change,"Mark":mark_change})
    elif manage=="4":
        id=input("\nEnter the id to delete the particular student record:")
        students.pop(id)
    elif manage=="5":
        print("Exited")
        break
    

    
                      