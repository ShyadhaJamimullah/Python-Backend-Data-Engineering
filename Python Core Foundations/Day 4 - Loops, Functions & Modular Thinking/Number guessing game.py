import random
n=None
actual_num=None
attempt=None

def admin():
    global n,actual_num,attempt
    n=int(input("Enter the limit (any number):"))
    actual_num=random.randint(1,n)
    attempt=int(input("Enter number of attempts:"))
    

def user():
    if n is None or actual_num is None or attempt is None:
        print("No input from admin")
        return

    print("\nNumber guessing game.")
    user_name=input("Enter user name:")
    print(f"\nHii {user_name}. Let's get started!")
    print(f"\nChoose a number between 1 to {n}")

    for attempts_used in range(1,attempt+1):
        guessed_num=int(input("Guess a number:"))
        if guessed_num<actual_num:
            print("Guess is low")
        elif guessed_num>actual_num:
            print("Guess is high")
        else:
            print("Congrats! You Won")
            break
    else:
        print(f"\nReached max attempts. The actualnumber is {actual_num}")


while True:
    print("\n1. Admin mode")
    print("2. User mode")
    print("3. Exit")
    choice=input("Choose (1/2):")
    if choice=="1":
        admin()
    elif choice=="2":
        user()
    elif choice=="3":
        print("Bye")
    else:
        print("Invalid option")
    


        

