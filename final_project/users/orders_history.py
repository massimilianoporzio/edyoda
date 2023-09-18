import os
import json
import time
import datetime

from users import user_menu
from models.order import Order
from models.food_item import FoodItem
def main(logged_user):
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
        my_orders = []
        for order_json in user_orders:
            order = Order(
                created_at=datetime.datetime.strptime(order_json["created_at"],'%Y-%m-%d %H:%M:%S.%f') ,
                total=order_json["total"],
                orderID=order_json["orderID"],
                userID=order_json["userID"]

            )
            order_items= []
            for item in order_json["food_items"]:
                food_item = FoodItem(
                    
                    fooodID=item["FoodID"],
                    name=item["name"],
                    price=item["price"],
                    quantity=item["quantity"],
                   
                )
                order_items.append(food_item)
            order.food_items=order_items
            my_orders.append(order)

        os.system('cls')
        print(f"=== Logged as: {logged_user.name} ===".center(36,"="))
        print("=== ORDERs HISTORY ===".center(36,"="))
        print(f"-".center(36,"-"))
        for index,order in enumerate(my_orders):
            print(f"{str(index+1)}. {repr(order)}\n")
            print(f"-".center(36,"-"))
        print(f"=".center(36,"="))
        print("\nPress ENTER to return to User Menu")
        input()
        file.close()
        user_menu.main(logged_user=logged_user)