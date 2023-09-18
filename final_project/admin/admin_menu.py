import os
from restaurant import main as mainMenu
from admin import add_item, edit_item

def main():
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
            add_item.main()
        case 2:
            edit_item.main()
    