import uuid
from builtins import staticmethod




class FoodItem:
    def __init__(self,name,quantity,price,discount,stock,fooodID = str(uuid.uuid4())) -> None:
        self.FoodID = fooodID
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self) -> str:
        return f"{self.name} ({self.quantity}) [INR {self.price}] - discount: {self.discount}% - Stock: {self.stock}"
   
    @staticmethod
    def createFood():
        food_name = input("Name: ")
        food_quantity = input("Quantity: ")
        while True:
            try:
                food_price = int(input("Price (INR): "))
                if food_price>0:
                    break
                else:
                    raise Exception("incorrect price")
            except:
                print("Enter a valid price in INR")
        
        while True:
            try:
                food_discount = float(input("Discout (%): "))
                if food_discount>=0 and food_discount<=100:
                    break
                else:
                    raise Exception("incorrect discount")
            except:
                print("Enter a number between 0 and 100")
        while True:
            try:
                food_stock = int(input("Stock amount: "))
                if food_stock>=0:
                    break
                else:
                    raise Exception("incorrect stock")
            except:
                print("Enter a number greater than 0")
        
        
        item=FoodItem(name=food_name,
                    quantity=food_quantity,
                    price=food_price,
                    discount=food_discount,
                    stock=food_stock)
        return item

    @staticmethod
    def editFood(itemToEdit):
        new_name = input(f"New Name (actual: {itemToEdit.name}): ")
        if new_name == "":
            new_name = itemToEdit.name
        new_quantity = input(f"New Quantity  (actual: {itemToEdit.quantity}): ")
        if new_quantity == "":
            new_quantity = itemToEdit.quantity
        while True:
            try:
                user_input = input(f"New Price  (actual: INR {itemToEdit.price}): ")
                if user_input == "":
                    new_price = itemToEdit.price
                    break
                new_price = int(user_input)

                if new_price>0:
                    break
                else:
                    raise Exception("incorrect price")
            except:
                print("Enter a valid price in INR")
        
        while True:
            try:
                user_input = input(f"New Discout (actual: {itemToEdit.discount}%): ")
                if user_input == "":
                    new_discount = itemToEdit.discount
                    break
                new_discount = float(user_input)
                if new_discount>=0 and new_discount<=100:
                    break
                else:
                    raise Exception("incorrect discount")
            except:
                print("Enter a number between 0 and 100")
        while True:
            try:
                user_input = input(f"Stock amount (actual: {itemToEdit.stock}): ")
                if user_input == "":
                    new_stock = itemToEdit.stock
                    break
                new_stock = int(user_input)
                if new_stock>=0:
                    break
                else:
                    raise Exception("incorrect stock")
            except:
                print("Enter a number greater than 0")
        item=FoodItem(
            fooodID=itemToEdit.FoodID,
                    name=new_name,
                    quantity=new_quantity,
                    price=new_price,
                    discount=new_discount,
                    stock=new_stock)
        return item
