## Day 2 — Operators, Numbers, and Strings

This folder contains Python programs written as part of Day 2 learning: Operators, Numbers, and Strings.
These tasks helped me understand how operators work in Python, how strings can be processed, and how user input can be validated logically.


### Concepts Covered

The following core Python concepts were learned and practiced through these programs:

- Arithmetic, comparison, and logical operators

- Operator precedence

- Mathematical operations

- String slicing

- String methods

- f-strings

- Input validation


### Programs Included

**1. Calculator Application**

This program performs basic mathematical operations based on user input.

**Supported Operations:**

- Addition (+)

- Subtraction (-)

- Multiplication (*)

- Division (/) with zero-division check

- Power (**)

- Square root (√)

**Concepts and Functions Used:**

- input() – to take user input

- int() – to convert input into integers

- Arithmetic operators (+, -, *, /, **)

- Comparison operator (!=)

- Conditional statements (if / elif / else)

- print() – to display results
  

**2. Email Validator**

This program checks whether an entered email address is valid based on simple validation rules.

**Validation Rules:**

- Must contain exactly one @ symbol

- Should not contain consecutive dots (..)

- Username should not be empty or contain spaces

- Domain must contain a dot (.)

- Domain should not start or end with a dot

**Concepts and Functions Used:**

- input() – to read email input

- str.count() – to count occurrences of @

- str.split() – to separate username and domain

- in keyword – to check substrings

- str.startswith() and str.endswith()

- Conditional statements

- print() – to display validation result
  

**3. Simple Billing System**

This program simulates a basic billing system that allows users to enter multiple products and calculates the final bill.

**Features:**

- Accepts product name, price, and quantity

- Calculates total cost per product

- Displays running bill

- Shows grand total at the end

**Concepts and Functions Used:**

- while True loop

- input() – to collect user data

- float() and int() – type conversion

- Arithmetic operations

- f-strings for formatted output

- Conditional statements (break)
  

**What I Learned**

- Applying operator precedence in calculations

- Using string methods for validation

- Formatting output using f-strings

- Writing loops for repeated user input
