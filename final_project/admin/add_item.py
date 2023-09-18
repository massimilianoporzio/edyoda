import os
import json
import time
from restaurant import main as mainMenu
from admin import admin_menu as mainAdmin
from models.food_item import FoodItem

def main():
    #read from existing file of food items (if exists, or open it for writing)
    with open(os.path.join(os.path.dirname(__file__), "./data/food_items.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            data = {
                "food_items":[]
            }
        food_items = data["food_items"]
        
        os.system('cls')
        print("====================================")
        print("=========== ADD ITEM ===============")
        print("====================================")
        item = FoodItem.createFood()
        item_dict = vars(item)
        food_items.append(item_dict)
        data["food_items"]=food_items
        file.seek(0)
        file.truncate(0)
        try:
            json.dump(data,file,indent=4)
            file.close()
        except:
            print("\u26D4 - Something went wrong")
        else:
            print("\U00002714 Item added successfully")
        time.sleep(1.5)
        mainAdmin.main()


        
