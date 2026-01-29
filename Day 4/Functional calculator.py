import math

def addition():
    sum=0
    for num_str in numbers_split:
        try:
            num=float(num_str)
            sum+=num
        except:
            print("Invalid input")
    print("Sum=",sum)

def subtraction():
    try:
        diff=float(numbers_split[0])
        for num_str in numbers_split[1:]:
            num=float(num_str)
            diff-=num
    except:
        print("Invalid input")
    print("Difference:",diff)

def multiplication():
    product=1
    for num_str in numbers_split:
        try:
            num=float(num_str)
            product*=num
        except:
            print("Invalid input")
    print("Product:",product)

def division():
    try:
        result=float(numbers_split[0])
        for num_str in numbers_split[1:]:
            num=float(num_str)
            result/=num
    except:
        print("Invalid input")
    print("Final Quotient:",result)

def modulus():
    try:
        modulus=float(numbers_split[0])
        for num_str in numbers_split[1:]:
            num=float(num_str)
            modulus%=num
    except:
        print("Invalid input")
    print("Modulus:",modulus)

def powers():
    try:
        power=float(numbers_split[0])
        for num_str in numbers_split[1:]:
            num=float(num_str)
            power**=num
    except:
        print("Invalid input")
    print("Power:",power)

def square():
    try:
        number=float(input("Enter a single number:"))
        output=number**2
    except:
        print("Invalid input")
    print(f"Square of {number} is:",output)
        
def square_root():
    try:
        number=float(input("Enter a single number:"))
        output=math.sqrt(number)
    except:
        print("Invalid input")
    print(f"Square root of {number} is:",output)

def expressions():
    expression=input("Enter the expression ((1+3)*6):")
    try:
        result=eval(expression)
        print(f"Result of expression {expression} is:",result)
    except:
        print("Invalid input")

def percentage():
    base_value=float(input("Enter base value:"))
    percent=float(input("Enter percent"))
    try:
        percentage=(percent/100)*base_value
    except:
        print("Invalid input")
    print(f"{percent}% of {base_value} is:",percentage)


while True:
    print("\n Functional Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square root")
    print("9. Expressions")
    print("10. Percentage")
    print("11. Exit")

    choice=input("Enter the operation you wish to perform (Eg:1 for addition):")
    if choice=="1" or choice=="2" or choice=="3" or choice=="4" or choice=="5" or choice=="6":
        numbers=input("Enter the numbers seperated by commas (1,2,3):")
        numbers_split=numbers.split(",")


    if choice=="1":
        addition()

    elif choice=="2":
        subtraction()

    elif choice=="3":
        multiplication()

    elif choice=="4":
        division()

    elif choice=="5":
        modulus()

    elif choice=="6":
        powers()

    elif choice=="7":
        square()
    
    elif choice=="8":
        square_root()

    elif choice=="9":
        expressions()

    elif choice=="10":
        percentage()

    elif choice=="11":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice")






