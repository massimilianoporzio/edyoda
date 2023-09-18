from restaurant import main as mainMenu
from admin import admin_menu
import json
import os
import time
import sys

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
            admin_menu.main()
            
            