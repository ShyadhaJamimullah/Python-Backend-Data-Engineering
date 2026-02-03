items={}
Grand_total=0
while True:
    print("\n\n1. Add a new product:")
    print("2. View available products:")
    print("3. Add to cart:")
    print("4. Remove expired products:")
    print("5. Exit")

    choice=input("\nEnter your choice:")
    
    if choice=="1":
        product=input("Enter the product:").lower()
        if product in items:
            print("Product already available")
        else:
            quantity=int(input("Enter the available quantity:"))
            
            price=int(input("Enter the product price:"))
            items[product]={"Quantity":quantity,"Price":price}
    
    elif choice=="2":
        for product in items:   
            print(product,items[product])
    
    elif choice=="3":
        product=input("Enter the product to add to cart:")
        if product not in items or items[product]["Quantity"]==0:
            print("Product is out of stock")
        else:
            print(f"{product} added to cart")
            
            buy=input("Do you want to buy (yes/no):").lower()
            if buy=="yes":
                aval_quantity=items[product]["Quantity"]
                quant_wanna_buy=int(input(f"Enter the quantity: (Quantity available ={aval_quantity})"))
                total=items[product]["Price"]*quant_wanna_buy
                Grand_total+=total
                items[product]["Quantity"]-=quant_wanna_buy

    elif choice=="4":
        product=input("Enter the product you wnat to remove from the list:")
        if product not in items or items[product]["Quantity"]==0:
            print("Product is already unavailable:")
        else:
            items.pop(product)

    elif choice=="5":
        print("GRAND TOTAL=",Grand_total)

        print("Thanks for visiting us. See you again!")
        
           


        
