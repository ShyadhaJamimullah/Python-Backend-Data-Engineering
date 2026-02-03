total=0
while True:
    product=input("Enter the product name:")
    price=float(input("Enter the price of the product:"))
    quantity=int(input("Enter the quantity:"))
    calc=price*quantity
    total+=calc
    print(f"{product}*{quantity}={calc}")
    cont=input("Do you want to buy more products (yes/no):")
    if cont=="no":
        break
print(f"Grand total={total}")
    