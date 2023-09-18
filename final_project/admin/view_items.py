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
        print("===== LIST OF FOOD ITEMS ===========")
        print("====================================")
        print("\n")
        if len(food_items)==0:
            print("There are no items in the list")
        else:
            for item in food_items:
                print(f"{item['name']} ({item['quantity']}) [INR {item['price']}] - Discount (%): {item['discount']} - Stock: {item['stock']}")
        print("\nPress ENTER to return to Admin Menu")
        input()
        file.close()
        mainAdmin.main()