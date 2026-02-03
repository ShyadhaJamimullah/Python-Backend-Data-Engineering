l1=[int(x) for x in input("Enter the numbers with space:").split()]
even=list(filter(lambda x:x%2==0,l1))
odd=list(filter(lambda x:x%2!=0,l1))
print("Even numbers:",even)
print("Odd numbers",odd)