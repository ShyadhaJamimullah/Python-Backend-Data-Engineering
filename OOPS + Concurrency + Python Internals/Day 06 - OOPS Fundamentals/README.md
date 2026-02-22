## Day 6 — Object-Oriented Programming (OOPS) Fundamentals

On Day 6, I focused on understanding Object-Oriented Programming in Python and how to design real-world systems using classes and objects.

### Concepts Covered

The following core Python concepts were learned and practiced through these programs:

- Classes and Objects

- ```__init__``` constructor

- Instance variables vs Class variables

- Encapsulation

- Getters and setters (through controlled methods)

- Code organization using multiple classes

- File handling using JSON for data persistence

- Exception handling for safe operations


### Hands-On Projects

**1. Bank Account Management System**

A console-based banking system built using OOPS principles.

**Features:**

- Create and store bank accounts persistently using JSON

- User authentication with account number and PIN

- Deposit and withdraw money

- Balance checking and transaction history

- Bank-level controls:

  - Open account
  
  - Close account (only if balance is zero)
  
  - Freeze and unfreeze accounts

- Account state management (active, frozen)

- Separation of responsibilities using multiple classes

**OOPS Concepts Applied:**

- **Encapsulation:** Account data is modified only through methods

- **Single Responsibility Principle:**

  - BankAccount → account data and transactions
  
  - AccountStorage → file handling
  
  - UserAuthentication → login validation
  
  - User → user operations
  
  - Bank → administrative actions

- Class methods for object reconstruction from stored data

- Exception handling for invalid operations
  


**2. Product Inventory Management System**

A simple inventory management system with persistent storage.

**Features:**

- Add, view, update, and deactivate products

- Increase and decrease stock safely

- Check product availability

- Inventory analytics:

  - Total number of products
  
  - Total stock quantity
  
  - Total inventory value

- JSON-based storage for inventory data

**OOPS Concepts Applied:**

- ProductInventory class to model real-world products

- Encapsulation to control stock updates

- Static methods to recreate objects from stored data

- Separation of business logic and file operations

- Input validation and exception handling
    

**What I Learned**

- How OOPS helps structure large programs cleanly

- How real-world systems can be modeled using classes

- Importance of separating data, logic, and storage

- Using JSON files to persist object data
