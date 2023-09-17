from restaurant import main as mainMenu
import sys
def main():
    print("========================")
    print("Welcome to admin section")
    print("1. Admin section")
    print("0. return to main section")
    while True:
        try:
            choice = int(input("Please make a choice\n"))
            if choice >= 0 and choice < 1:
                break
            else:
                raise Exception("error in parsing")
        except Exception as ex:
            print('Enter 1 for admin section, 0 to quit this section')
    match choice:
        case 0:
            print("back to main menu")
            mainMenu.mainMenu()
            # sys.exit()
        case _:
            print("boh")