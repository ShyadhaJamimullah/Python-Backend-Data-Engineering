num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
operator=input("Specify the operation you wish to perform: (+, -, *, /, **, √)")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/" and num2!=0:
    print(num1/num2)
elif operator=="**":
    print(num1**num2)
elif operator=="√":
    print(num1**0.5)
    print(num2**0.5)
else:
    print("Error! Division by zero \ No operation specified")

