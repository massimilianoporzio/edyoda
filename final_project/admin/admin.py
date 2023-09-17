from restaurant import main as mainMenu
import json
import os
import sys
def main():
    print("========================")
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
               
            except Exception as ex:
                print("\nSomething went wrong.\n")
                mainMenu.mainMenu()

            #TODO fare loop chiedendo se vuole uscire
            username = input("username:")
          
            admin_user =  next((x for x in admin_users if x['username'] == username), None)
            if not admin_user:
                print("Username not found")
            else:
                password = input("password:")
                admin_password =  next((x for x in admin_users if x['password'] == username), None)
        case _:
            print("boh")