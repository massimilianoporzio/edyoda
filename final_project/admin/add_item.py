import os
import json
import time
from restaurant import main as mainMenu
from admin import admin_menu as mainAdmin
from models.food_item import FoodItem

def main():
    #read from existing file of food items (if exists, or open it for writing)
    with open(os.path.join(os.path.dirname(__file__), "food_items.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            data = {
                "food_items":[]
            }
        food_items = data["food_items"]
        print(food_items)
        os.system('cls')
        print("====================================")
        print("=========== ADD ITEM ===============")
        print("====================================")
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
        item_dict = vars(item)
        food_items.append(item_dict)
        data["food_items"]=food_items
        file.seek(0)
        json.dump(data,file,indent=4)
        file.close()
        print("\U000F2714 Item saved successfully")
        time.sleep(1.5)
        mainAdmin.main()


        
