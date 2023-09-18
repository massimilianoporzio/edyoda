from restaurant import main as mainMenu
import json
import os
import time
import sys
from models.food_item import FoodItem
def main():
    os.system('cls')
    print("\n========================")
    print("Welcome to admin section")
    print("1. Login")
    print("0. Return to main Menu")
    print("========================")
    while True:
        try:
            choice = int(input("Please make a choice\n"))
            if choice >= 0 and choice < 2:
                break
            else:
                raise Exception("error in parsing")
        except Exception as ex:
            print('Enter 1 for admin section, 0 to return to main Menu')
    match choice:
        case 0:
            mainMenu.mainMenu()
        case 1:
            #reading from file admin users
            try:
                f =  open(os.path.join(os.path.dirname(__file__), 'admin_users.json'),encoding="utf-8")
                admin_users = json.load(f)['admin_users']
                f.close()
               
            except Exception as ex:
                os.system('cls')
                print("\n\u26D4 Something went wrong.\n")
                time.sleep(1)
                mainMenu.mainMenu()

            while True:
                os.system('cls')
                print("\n========================")
                print("\n======= LOGIN ==========")
                print("\n========================")
                username = input("username: ")
                if username == "0":
                    mainMenu.mainMenu()
                admin_user =  next((x for x in admin_users if x['username'] == username), None)
                if not admin_user:
                    print("\n========================")
                    print("\u26D4 Username not found - please try again or press 0 for Main Menu")
                    time.sleep(1)
                else:
                    break
            while True:
                os.system('cls')
                print("\n========================")
                print("\n======= LOGIN ==========")
                print("\n========================")
                password = input(f"password for user '{admin_user['username']}': ")
                if password == "0":
                    mainMenu.mainMenu()
                admin_password =  next((x for x in admin_users if x['password'] == password), None)
                if not admin_password:
                    print("\n========================")
                    print("\u26D4 Wrong password - please try again or press 0 for Main Menu")
                    time.sleep(1)
                else:
                    break
            os.system('cls')
            
            while True:
                print("====================================")
                print("1. Add new food items")
                print("2. Edit food items")
                print("3. View the list of food items")
                print("4. Remove a food item from the menu")
                print("0. Logout")
                print("====================================")
                try:
                    choice = int(input("Please make a choice\n"))
                    if choice >= 0 and choice < 5:
                        break
                    else:
                        raise Exception("error in parsing")
                except Exception as ex:
                    os.system('cls')
                    print('Make a selection, or press 0 to logout')
            match choice:
                    case 0:
                        mainMenu.mainMenu()
                    case 1:
                        #read from existing file of food items (if exists, or open it for writing)
                        with open(os.path.join(os.path.dirname(__file__), "food_items.json"), "a+", encoding="utf-8") as file:
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
                            json.dump(data,file)
                            
                