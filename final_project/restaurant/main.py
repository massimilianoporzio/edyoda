import os
import sys
def mainMenu():
    os.system('cls')
    print("\n======================")
    print("Welcome to my restaurant")
    print("1. Admin section")
    print("2. User section")
    print("0. QUIT")
    print("======================")
    while True:
        try:
            choice = int(input("Please make a choice\n"))
            if choice >= 0 and choice < 3:
                if choice == 0:
                    sys.exit()
                break
            else:
                raise Exception("error in parsing")
        except Exception as ex:
            print('Enter 1 for admin section, 2 for users section')
    match choice:
        case 1:
            from admin import main as mainAdmin
            mainAdmin.main()
            #sys.exit()
        case 2:
            from users import main as mainUsers
            mainUsers.main()
if __name__ == '__main__':
    mainMenu()
    