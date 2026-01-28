password=input("Enter a password:")
digit=False
upper=False
for i in password:
    if i.isdigit():
        digit=True
    if i.isupper():
        upper=True
if len(password)<5 and digit==False and upper==False:
    print("Weak")
elif digit==True and upper==True:
    print("Strong")
else:
    print("Medium")