## Day 5 — Exceptions, Files, and JSON

This folder contains programs written as part of Day 5 learning: Exceptions, Files, and JSON.
The focus of this day was on handling errors properly, working with files, storing data using JSON, and organizing code into modules.
All these concepts were applied in a File-Based Student Management System mini project.

### Concepts Covered

- Exception handling using try / except / finally

- Creating and using custom exceptions

- File handling in Python

- Reading and writing JSON data (json.load(), json.dump())

- Folder and project structure

- Modular programming


### Mini Project — File-Based Student Management System

A role-based student management system that stores data in a JSON file and uses proper exception handling and modular design.


**Project Structure**

- *user_interaction.py*: 
    Handles all menus and user interaction based on roles (Admin, Staff, Principal, Student).

- *services/student_operations.py*: 
    Contains core logic for student operations such as add, view, update, delete, filtering, and eligibility checks.

- *services/file_handling.py*: 
    Manages reading from and writing to the JSON file safely.

- *exceptions/custom_exceptions.py*: 
    Defines custom exceptions for clear and meaningful error handling.

- *data/students.json*: 
    Stores student records persistently.

**Roles and Features**

**Admin / Office**

- Add student records

- View a student or all students

- Update student details

- Delete student records

**Staff**

- View student details

- View all students

- Filter students by department

- Check scholarship eligibility

**Principal**

- View all students

- View students department-wise

**Student**

- View own details only

- Check scholarship eligibility

**Concepts and Methods Used**

- try / except blocks for safe execution

- Custom exceptions like:

  - StudentAlreadyExists
  
  - StudentNotFound
  
  - NotEligibleForScholarship

- File operations with open()

- JSON operations using json.load() and json.dump()

- Dictionary-based data storage

- Role-based access control

- Modular function design
  

**What I Learned**

- How to handle errors gracefully using exceptions

- How to create meaningful custom exceptions

- How to store and retrieve data using JSON files

- How to organize a Python project into modules and folders
