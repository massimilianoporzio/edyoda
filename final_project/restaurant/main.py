def mainMenu():
    print("Welcome to my restaurant")
    print("1. Admin section")
    print("2. User section")
    print("======================")
    while True:
        try:
            choice = int(input("Please make a choice\n"))
            if choice > 0 and choice < 3:
                break
            else:
                raise Exception("error in parsing")
        except Exception as ex:
            print('Enter 1 for admin section, 2 for users section')
    match choice:
        case 1:
            from admin import admin
            admin.main()
            #sys.exit()
        case 2:
            from users import users
            users.main()
if __name__ == '__main__':
    mainMenu()
    