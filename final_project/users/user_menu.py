import os
from restaurant import main as mainMenu
from users import place_order, orders_history
def main(logged_user):
    os.system('cls')
    while True:
        print(f"=== Logged as: {logged_user.name} ===".center(36,"="))
        print("1. Place New Order")
        print("2. Orders History")
        print("3. Update Profile")
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
            place_order.main(logged_user=logged_user)