import json
import os
import time

from admin import admin_menu as mainAdmin
from models.food_item import FoodItem
from restaurant import main as mainMenu
def main():
    with open(os.path.join(os.path.dirname(__file__), "./data/food_items.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            print("\u26D4 - Something went wrong")
            time.sleep(1.5)
            mainAdmin.main()
        food_items = data["food_items"]
        if len(food_items)==0:
            print("\n")
            print("There are no items in the list")
            time.sleep(1.5)
            file.close()
            mainAdmin.main()
            return
        os.system('cls')
        
        
        
        while True:
            print("====================================")
            print("===== SELECT ITEM TO REMOVE ========")
            print("====================================")
            print("\n")
            for item in food_items:
                print(f"{item['FoodID']} - {item['name']}")
            print("\n")
            foodID = input("Please type the FoodID of the item you want to remove\n - you can copy and paste it from the above list - \n(type 0 for the Admin Menu)\n FoodID: ")
            if foodID == "0":
                    mainAdmin.main()
                    return
            item_to_edit = next((x for x in food_items if x['FoodID'] == foodID), None)
            if(item_to_edit):
                
                break
            else:
                print("\u26D4 Item not found - Please try again OR type 0 for the Admin Menu")
                time.sleep(2)
                os.system('cls')
        item_to_edit_index = food_items.index(item_to_edit)
        while True:
            user_input = input(f"are you sure you want to remove '{item_to_edit['name']}'?(Yes/No)")
            if user_input.lower()=="yes" or user_input.lower() =='y':
                break
            elif user_input.lower() == "no" or user_input.lower() == "n":
                mainAdmin.main()
                file.close()
                return
        food_items.pop(item_to_edit_index)
        if(len(food_items)==0):
            data["food_items"]= []
        else:
            data["food_items"]=food_items
        file.seek(0)
        file.truncate(0)
        try:
            json.dump(data,file,indent=4)
            file.close()
        except:
            print("\u26D4 - Something went wrong")
        else:
            print("\U00002714 Item removed successfully")
        
        time.sleep(1.5)
        mainAdmin.main()


