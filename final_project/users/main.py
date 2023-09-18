from restaurant import main as mainMenu
from users import register_user
import json
import os
import time
import sys

def main():
    os.system('cls')
    print("\n========================")
    print("Welcome to Users section")
    print("1. Register")
    print("2. Login")
    print("0. Return to main Menu")
    print("========================")
    while True:
        try:
            choice = int(input("Please make a choice\n"))
            if choice >= 0 and choice < 3:
                break
            else:
                raise Exception("error in parsing")
        except Exception as ex:
            print('Enter 1 to register a new user, 2 to login,or  0 to return to main Menu')
    match choice:
        case 0:
            mainMenu.mainMenu()
            return
        case 1:
            register_user.main()
            return