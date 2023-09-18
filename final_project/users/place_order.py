import os
import json
import datetime
import time

from restaurant import main as mainMenu
from users import user_menu
from models.order import Order
from models.food_item import FoodItem

#Serialize datetime and food items (removing discount and stock)
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o,FoodItem):
        item_dict = vars(o)
        del(item_dict["discount"])
        del(item_dict["stock"])
        return item_dict
    
def main(logged_user, items_for_order):
    with open(os.path.join(os.path.dirname(__file__), "./../admin/data/orders.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            print("\u26D4 - Something went wrong")
            time.sleep(2)
            user_menu.main(logged_user=logged_user)
            file.close()
            return
        
        existing_orders = data["orders"]
        #recupero tutti gli oridini dell'utente loggato
        user_orders = [x for x in existing_orders if x["userID"]==logged_user.userID]
        os.system('cls')
        print(f"=== Logged as: {logged_user.name} ===".center(36,"="))
        print("=== THIS IS YOUR ORDER ===".center(36,"="))
        print(f"-".center(36,"-"))
        for index,item in enumerate(items_for_order):
            print(f"{str(index+1)}. {repr(item)}")
        print(f"-".center(36,"-"))
        print(f"=".center(36,"="))
        while True:
            user_input = input("Do you want to PLACE this order? (Yes/No)")
            if user_input.lower()=="yes" or user_input.lower() =='y':
                break
            elif user_input.lower() == "no" or user_input.lower() == "n":
                file.close()
                user_menu.main(logged_user=logged_user)
                return
        #placing the order
        
        #CREATE THE ORDER:
        user_order = Order(
            userID=logged_user.userID,
            food_items=items_for_order
        )
        
        order_dict = vars(user_order)
        
        existing_orders.append(order_dict)
        #print(json.dumps(order_dict, default = myconverter)) 
        data["orders"]=existing_orders
        file.seek(0)
        file.truncate(0)
        try:
            json.dump(data,file,indent=4,default = myconverter)
            file.close()
        except:
            print("\u26D4 - Something went wrong")
            file.close()
            user_menu.main(logged_user=logged_user)
            return
        else:
            #loading the items for decrementing the stock
            with open(os.path.join(os.path.dirname(__file__), "./../admin/data/food_items.json"), "r+", encoding="utf-8") as foodFile:
                try:
                    foodData = json.load(foodFile)
                except:
                    print("\u26D4 - Something went wrong")
                    time.sleep(2)
                    mainMenu.main()
                    foodFile.close()
                    
                    return
                food_items = foodData["food_items"]
                #selectin only the one ordered by the user
                foodID_selected = [x.FoodID for x in items_for_order]
                for existing_item in food_items:
                    if existing_item["FoodID"] in foodID_selected:
                        existing_item["stock"] = existing_item["stock"] - 1
                    
                #TODO write on food_items.json
                foodData["food_items"]=food_items
                print("new food items: ",foodData["food_items"])
                foodFile.seek(0)
                foodFile.truncate(0)
                try:
                    json.dump(foodData,foodFile,indent=4)
                    foodFile.close()
                except:
                    print("\u26D4 - Something went wrong")
                    foodFile.close()
                else:
                    print("\U00002714 Order placed successfully")
                    time.sleep(2)
                    user_menu.main(logged_user=logged_user)
                    return
        
        

        

        