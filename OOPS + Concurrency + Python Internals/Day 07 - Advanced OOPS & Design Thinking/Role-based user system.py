import json
import os


#employee data storage
class Storage:
    file="employee.json"

    def __init__(self):
        if not os.path.exists(self.file):
            with open(self.file,"w") as f:
                json.dump({},f,indent=4)

    def load(self):
        with open(self.file,"r") as f:
            return json.load(f)
        
    def save(self,data):
        with open(self.file,"w") as f:
            json.dump(data,f,indent=4)

class AuthStorage:
    file = "auth.json"

    def __init__(self):
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f, indent=4)

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)
        
class AuthService:
    def __init__(self, auth_store: AuthStorage):
        self.auth_store = auth_store

    def login(self, username, password):
        users = self.auth_store.load()

        if username not in users:
            raise Exception("Invalid username")

        user = users[username]

        if user["password"] != password:
            raise Exception("Invalid password")

        return user


#data model
class Employee:
    def __init__(self,Employee_ID,Name,Contact,Address,Department,Designation,Salary):
        self.Employee_ID=Employee_ID
        self.Name=Name
        self.Contact=Contact
        self.Address=Address
        self.Department=Department
        self.Designation=Designation
        self.Salary=Salary

    def to_dict(self):
        return{
            "Employee_ID":self.Employee_ID,
            "Name":self.Name,
            "Contact":self.Contact,
            "Address":self.Address,
            "Department":self.Department,
            "Designation":self.Designation,
            "Salary":self.Salary
        }
    
    @classmethod
    def from_dict(cls,Employee_ID,data):
        employee=cls(Employee_ID,
                     data["Name"],
                     data["Contact"],
                     data["Address"],
                     data["Department"],
                     data["Designation"],
                     data["Salary"]
                     )
        return employee
    
#abstract class
from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,store:Storage):
        self.store=store

    @abstractmethod
    def view_employee(self,Employee_ID):
        pass

#actual users
class Admin(User): #amdin inherits from abc-User
    def add_employee(self,employee:Employee):
        data=self.store.load() #load json to check if employee exists
        if employee.Employee_ID in data:
            raise Exception("Employee already exists")
        data[employee.Employee_ID]=employee.to_dict() #dump to json when new employee added
        self.store.save(data) #save changes to json

    def view_employee(self,Employee_ID):
        data=self.store.load()
        if Employee_ID not in data:
            raise Exception("Employee does not exists")
        return data.get(Employee_ID)
    
    def view_all_employees(self):
        data=self.store.load()
        if not data:
            print("No employees found")
            return

        for Employee_ID, info in data.items():
            print("\nEmployee ID:",Employee_ID)
            print("Name:",info["Name"])
            print("Contact:",info["Contact"])
            print("Address:",info["Address"])
            print("Department:",info["Department"])
            print("Designation:",info["Designation"])
            print("Salary:",info["Salary"])
    
    def update_employee(self,Employee_ID,updates:dict):
        data=self.store.load()
        if Employee_ID not in data:
            raise Exception("No Employee with that ID found")
        data[Employee_ID].update(updates)
        self.store.save(data)

    def delete_employee(self,Employee_ID):
        data=self.store.load()
        if Employee_ID not in data:
            raise Exception("No Employee with that ID found")
        data.pop(Employee_ID,None)
        self.store.save(data)

class Manager(User):
    def view_employee(self, Employee_ID):
        data=self.store.load()
        if Employee_ID not in data:
            raise Exception("Employee does not exists")
        return data.get(Employee_ID)
    
    def view_all_employees(self):
        data=self.store.load()
        if not data:
            print("No employees found")
            return

        for Employee_ID, info in data.items():
            print("\nEmployee ID:",Employee_ID)
            print("Name:",info["Name"])
            print("Contact:",info["Contact"])
            print("Address:",info["Address"])
            print("Department:",info["Department"])
            print("Designation:",info["Designation"])
            print("Salary:",info["Salary"])
    
    def update_employee(self,Employee_ID,updates:dict):
        data=self.store.load()

        if Employee_ID not in data:
            raise Exception("Employee not found")
        
        allowed={"Department","Designation"}

        safe_updates={
            k:v for k,v in updates.items() if k in allowed
        }
        if not safe_updates:
            raise Exception("No valid fields to update")
        
        data[Employee_ID].update(safe_updates)
        self.store.save(data)


class SingleEmployee(User):
    def __init__(self,store:Storage,Employee_ID):
        super().__init__(store)
        self.Employee_ID=Employee_ID

    def view_employee(self,Employee_ID):
        if Employee_ID!=self.Employee_ID:
            raise PermissionError("Access denied")
        data=self.store.load()
        return data.get(Employee_ID)
    
    def update_contact(self,updates:dict):
        data=self.store.load()
        if self.Employee_ID not in data:
            raise Exception("Employee not found")
        allowed={"Contact","Address"}
        safe_updates={
            k:v for k,v in updates.items() if k in allowed
        }

        if not safe_updates:
            raise Exception("No valid fields to update")
        
        data[self.Employee_ID].update(safe_updates)
        self.store.save(data)



def admin_mode(admin:Admin):
    while True:
        print("\nADMIN MODE")
        print("1. Add employee: ")
        print("2. View Employee")
        print("3. View all Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice=input("Enter choice (e.g. 1): ")
        try: 
            if choice=="1":
                Employee_ID=input("Enter ID: ")
                Name=input("Enter Name: ")
                Contact=input("Enter Contact: ")
                Address=input("Enter Address: ")
                Department=input("Enter Department: ")
                Designation=input("Enter Designation: ")
                Salary=input("Enter salary: ")

                emp=Employee(Employee_ID,Name,Contact,Address,Department,Designation,Salary)

                admin.add_employee(emp)
                print("Employee added")

            elif choice=="2":
                Employee_ID=input("Enter ID: ")
                emp=admin.view_employee(Employee_ID)
                print(emp)

            elif choice=="3":
                admin.view_all_employees()
                

            elif choice=="4":
                Employee_ID=input("Enter ID: ")
                print("Press enter if you want to skip any field")

                updates={}
                
                name=input("Update name: ")
                if name:
                    updates["Name"]=name
                contact=input("Update contact: ")
                if contact:
                    updates["Contact"]=contact
                address=input("Update address: ")
                if address:
                    updates["Address"]=address
                department=input("Update department: ")
                if department:
                    updates["Department"]=department
                designation=input("Update designation: ")
                if designation:
                    updates["Designation"]=designation
                salary=input("Update salary: ")
                if salary:
                    updates["Salary"]=salary
                if not updates:
                    print("No updates")
                else:
                    admin.update_employee(Employee_ID,updates)
                    print("Updated successfully")

            elif choice=="5":
                Employee_ID=input("Enter Employee ID: ")
                admin.delete_employee(Employee_ID)
                print("Employee removed")

            elif choice=="6":
                print("Exiting....")
                break

            else:
                print("Invalid choice")
        except Exception as e:
            print("Error: ",e)


def manager_mode(manager:Manager):
    while True:
        print("\nMANAGER MODE")
        print("1. View Employee")
        print("2. View all Employees")
        print("3. Update Employee")
        print("4. Exit")

        choice=input("Enter choice (e.g. 1): ")

        try:
            if choice=="1":
                Employee_ID=input("Enter ID: ")
                emp=manager.view_employee(Employee_ID)
                print(emp)

            elif choice=="2":
                manager.view_all_employees()


            elif choice=="3":
                Employee_ID=input("Enter ID: ")
                print("Press enter to skip fields")

                updates={}

                Department=input("Update Department: ")
                if Department:
                    updates["Department"]=Department
                Designation=input("Update Designation: ")
                if Designation:
                    updates["Designation"]=Designation
                manager.update_employee(Employee_ID,updates)
                print("Updated successfully")

            elif choice=="4":
                print("Exiting....")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error: ",e)



def employee_mode(emp:SingleEmployee):
    while True:
        print("\nEMPLOYEE MODE")
        print("1. View your info: ")
        print("2. Edit contact details: ")
        print("3. Exit")
        choice=input("Enter choice (e.g. 1): ")
        try:
            if choice=="1":
                print(emp.view_employee(emp.Employee_ID))

            elif choice=="2":
                print("Press enter if you want to skip any field")

                updates={}

                contact=input("Update contact: ").strip()
                if contact:
                    updates["Contact"]=contact
                address=input("Update address: ")
                if address:
                    updates["Address"]=address
                emp.update_contact(updates)
                print("Updated successfully")

            elif choice=="3":
                print("Exiting....")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:",e)
        

def choose_mode():
    store = Storage()
    auth_store = AuthStorage()
    auth_service = AuthService(auth_store)

    print("\nLOGIN")
    username = input("Username: ")
    password = input("Password: ")

    try:
        user = auth_service.login(username, password)
        role = user["role"]

        if role == "ADMIN":
            admin = Admin(store)
            admin_mode(admin)

        elif role == "MANAGER":
            manager = Manager(store)
            manager_mode(manager)

        elif role == "EMPLOYEE":
            emp = SingleEmployee(store, user["employee_id"])
            employee_mode(emp)

        else:
            print("Unknown role")

    except Exception as e:
        print("Login failed:", e)
choose_mode()
