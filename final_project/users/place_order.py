import os
import json
import time
from restaurant import main as mainMenu
import datetime

#Serialize datetime
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def main(logged_user):
     with open(os.path.join(os.path.dirname(__file__), "./../admin/orders.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            print("\u26D4 - Something went wrong")
            time.sleep(2)
            mainMenu.main()
            file.close()
            return
        print(data)
        existing_orders = data["orders"]
        #recupero tutti gli oridini dell'utente loggato
        user_orders = [x for x in existing_orders if x["userID"]==logged_user.userID]
        print(user_orders)