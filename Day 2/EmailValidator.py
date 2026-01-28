email=input("Enter your email:")
if email.count("@")!=1:
    print("Invalid email")
if ".." in email:
    print("Invalid email")
else:
    username,domain=email.split("@")
    if username=="":
        print("Invalid email")
    elif " " in username:
        print("Invalid email")
    elif "." not in domain:
        print("Invalid email")
    elif domain.startswith(".") or domain.endswith("."):
        print("Invalid email")
    else:
        print("Valid email")