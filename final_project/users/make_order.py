import os
import json
import time
from restaurant import main as mainMenu
from users import user_menu,place_order
from models.food_item import FoodItem


def main(logged_user):
    #mostro la lista di food
    with open(os.path.join(os.path.dirname(__file__), "./../admin/data/food_items.json"), "r", encoding="utf-8") as foodFile:
        try:
            foodData = json.load(foodFile)
        except:
            print("\u26D4 - Something went wrong")
            time.sleep(2)
            mainMenu.main()
            foodFile.close()
            
            return
    food_items = foodData["food_items"]
    food_items = [x for x in food_items if x["stock"]>0]
    os.system('cls')
    print(f"=== Logged as: {logged_user.name} ===".center(36,"="))
    print("=== SELECT FOODS FOR YOUR ORDER ===".center(36,"="))
    print(f"-".center(36,"-"))
    if len(food_items)==0:
        print("Sorry! No items left")
        print(f"-".center(36,"-"))
        foodFile.close()
        user_menu.main()
        return
    else:
        while True:
            os.system('cls')
            print(f"=== Logged as: {logged_user.name} ===".center(36,"="))
            print("=== SELECT FOODS FOR YOUR ORDER ===".center(36,"="))
            print(f"-".center(36,"-"))
            for index,item in enumerate(food_items):
                print(f"{str(index+1)}. {item['name']} ({item['quantity']}) [INR {item['price']}]")
            print(f"-".center(36,"-"))
            input_items = input("Please enter the item(s) for your order, separated by a comma: ")
            input_items = [x for x in input_items.split(",")]
            selected_items = []
            
            try:
                for item in input_items:
                    if item.isdigit():
                        if int(item)<1 or int(item) > len(food_items):
                            raise Exception("Wrong index for food item")
                        selected_items.append(int(item))
                    else:
                        break
            except:
                print("\u26D4 Please, enter the correct indices for the selected item(s)")
                time.sleep(2)
            else:
                if len(input_items) != len(selected_items):
                    print("\u26D4 Please, enter the correct list of selected item(s)")
                else:
                    break
        selected_items.sort()
        items_for_order = []
        for index in selected_items:
            selected = food_items[index-1]
            item = FoodItem(
                fooodID=selected["FoodID"],
                discount=selected["discount"],
                name=selected["name"],
                price=selected["price"],
                quantity=selected["quantity"],
                stock=selected["stock"]
            )
            items_for_order.append(item)
        
        foodFile.close()
        place_order.main(logged_user=logged_user, items_for_order=items_for_order)
        return


                    
                