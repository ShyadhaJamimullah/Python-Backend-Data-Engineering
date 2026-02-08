import json
import os

file="inventory.json"

def load_inventory():
    if not os.path.exists(file):
        return {}
    with open(file,"r") as f:
        return json.load(f)
    
def dump_inventory(inventory):
    with open(file,"w") as f:
        json.dump(inventory,f)

#analytical functions
    
def total_products(inventory):
    return len(inventory)

def total_stock_quantity(inventory):
    total = 0
    for product in inventory.values():
        if product["is_active"]:
            total += product["quantity"]
    return total

def total_inventory_value(inventory):
    total = 0
    for product in inventory.values():
        if product["is_active"]:
            total += product["price"] * product["quantity"]
    return total

class ProductInventory:

    def __init__(self,product_id,product_name,price,quantity,is_active=True):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
        self.is_active=is_active


    def in_stock(self):
        return self.quantity>0
    
    def increase_stock(self,amount):
        if amount<=0:
            raise Exception("Must be positive")
        self.quantity+=amount

    def decrease_stock(self,amount):
        if amount<=0:
            raise Exception("Must be positive")
        if amount>self.quantity:
            raise Exception("Amount should be less than or equal to quantity")
        self.quantity-=amount

    def deactivate(self):
        self.is_active=False      

    def to_dict(self):
        return{
            "product_id":self.product_id,
            "product_name":self.product_name,
            "price":self.price,
            "quantity":self.quantity,
            "is_active":self.is_active
        }
    
    @staticmethod
    def from_dict(data):
        return ProductInventory(
            data["product_id"],
            data["product_name"],
            data["price"],
            data["quantity"],
            data["is_active"]
        )





def inventorySystem():
    while True: 
        print("INVENTORY MANAGER")
        print("1. Add Product")
        print("2. View Product Details")
        print("3. Check Stock")
        print("4. Increase Stock")
        print("5. Decrease Stock")
        print("6. Delete Product")
        print("7. View Stock Analytics")
        print("8. Exit")

        choice=input("Enter choice (e.g. 1): ")

        inventory=load_inventory()

        try:
            if choice=="1":
                product_id=input("Enter Product ID: ")
                if product_id in inventory:
                    print("Product already exists")
                    continue

                product_name=input("Enter Product Name: ")
                price=float(input("Enter Price: "))
                quantity=int(input("Enter Quantity: "))
                product=ProductInventory(product_id,product_name,price,quantity)

                inventory[product_id]=product.to_dict()
                dump_inventory(inventory)
                print("Product added")

            elif choice=="2":
                product_id=input("Enter product ID: ")
                if product_id not in inventory:
                    print("Product not found")
                    continue
                product=ProductInventory.from_dict(inventory[product_id])

                if not product.is_active:
                    print("Product is deactivated")
                    continue
                print(product.to_dict())

            elif choice=="3":
                product_id=input("Enter product id: ")
                if product_id not in inventory:
                    print("Product not found")
                    continue
                product=ProductInventory.from_dict(inventory[product_id])
                print(f"Product name: {product.product_name}")
                print(f"Price: {product.price}")
                print(f"Quantity: {product.quantity}")

            elif choice=="4":
                product_id=input("Enter product id: ")
                if product_id not in inventory:
                    print("Product not found")
                    continue

                amount=int(input("Enter amount: "))
                
                product=ProductInventory.from_dict(inventory[product_id])
                product.increase_stock(amount)
                inventory[product_id]=product.to_dict()
                dump_inventory(inventory)
                print("Stock increased")

            elif choice=="5":
                product_id=input("Enter product id: ")
                if product_id not in inventory:
                    print("Product not found")
                    continue

                amount=int(input("Enter amount: "))

                product=ProductInventory.from_dict(inventory[product_id])
                product.decrease_stock(amount)
                inventory[product_id]=product.to_dict()
                dump_inventory(inventory)
                print("Stock decreased")

            elif choice=="6":
                product_id=input("Enter product id: ")
                if product_id not in inventory:
                    print("Product not found")
                    continue

                product=ProductInventory.from_dict(inventory[product_id])
                product.deactivate()
                inventory[product_id]=product.to_dict()
                dump_inventory(inventory)

            elif choice == "7":
                print("Total products:", total_products(inventory))
                print("Total stock:", total_stock_quantity(inventory))
                print("Total inventory value:", total_inventory_value(inventory))


            elif choice=="8":
                print("Exiting....")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error: ",e)

inventorySystem()





                




            
        






