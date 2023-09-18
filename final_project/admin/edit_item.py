import json
import os
import time

from admin import admin_menu as mainAdmin
from models.food_item import FoodItem
from restaurant import main as mainMenu


def main():
    with open(os.path.join(os.path.dirname(__file__), "food_items.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            print("\u26D4 - Something went wrong")
            time.sleep(1.5)
            mainAdmin.main()
        food_items = data["food_items"]
        
        os.system('cls')
        print("====================================")
        print("===== SELECT ITEM TO EDIT ==========")
        print("====================================")
        print("\n")
        
        for item in food_items:
            print(f"{item['FoodID']} - {item['name']}")
        print("\n")
        while True:
            foodID = input("Please type the FoodID of the item you want to edit\n(you can copy and paste it from the above list): ")
            if foodID == "0":
                    mainMenu.mainMenu()
            item_to_edit = next((x for x in food_items if x['FoodID'] == foodID), None)
            if(item_to_edit):
                
                break
            else:
                print("\u26D4 Item not found - Please try again OR type 0 for the Admin Menu")
        #visualize the item to edit
        item_to_edit_index = food_items.index(item_to_edit)
        foodItem = FoodItem(fooodID=item_to_edit["FoodID"],
                            name=item_to_edit["name"],
                            quantity=item_to_edit["quantity"],
                            discount=item_to_edit["discount"],
                            price=item_to_edit["price"],
                            stock=item_to_edit["stock"])
        print("===================================")
        print(f"Name: {foodItem.name}")
        print(f"Quantity: {foodItem.quantity}")
        print(f"Price (INR): {foodItem.price}")
        print(f"Discount (%): {foodItem.discount}")
        print(f"Stock: {foodItem.stock}")
        print("===================================")
        foodItem = FoodItem.editFood(foodItem)
        item_dict = vars(foodItem)
        food_items[item_to_edit_index]=item_dict
        data["food_items"]=food_items
        
        file.seek(0)
        try:
            json.dump(data,file,indent=4)
            file.close()
        except:
            print("\u26D4 - Something went wrong")
        else:
            print("\U00002714 Item edited successfully")
        
        time.sleep(1.5)
        mainAdmin.main()
        
