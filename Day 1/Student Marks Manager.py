name=input("Enter your name:")
dbms_mark=int(input("Enter your DBMS mark:"))
dsa_mark=int(input("Enter your DSA mark:"))
os_mark=int(input("Enter your OS mark:"))
avg=(dbms_mark+dsa_mark+os_mark)/3
if avg>=85:
    print("A")
elif avg>=70:
    print("B")
elif avg>=50:
    print("C")
else:
    print("Fail")
