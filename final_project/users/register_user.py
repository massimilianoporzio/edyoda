import os
import json
import time
from users import main as mainUsers
from restaurant import main as mainMenu
from models.user import User
import phonenumbers
#TODO add check if user press Q for quit and return to previous menu
def main():
     with open(os.path.join(os.path.dirname(__file__), "./../admin/data/registered_users.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            print("\u26D4 - Something went wrong")
            time.sleep(2)
            mainMenu.main()
            file.close()
            return
        existing_users = data["users"]
        
        os.system('cls')
        print("==========================================")
        print("======== REGISTER A NEW USER  ============")
        print("==========================================")
        user =User.createUser(existing_users=existing_users)
        user_dict = vars(user)
        existing_users.append(user_dict)
        data["users"]=existing_users
        file.seek(0)
        file.truncate(0)
        try:
            json.dump(data,file,indent=4)
            file.close()
        except:
            print("\u26D4 - Something went wrong")
        else:
            print("\U00002714 User registered successfully - please Login to access the application")
        time.sleep(2)
        mainUsers.main()

