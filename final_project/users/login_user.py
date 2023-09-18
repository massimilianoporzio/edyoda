import os
import json
import time
from restaurant import main as mainMenu
from users import user_menu
from models.user import User
import maskpass
def main():
    with open(os.path.join(os.path.dirname(__file__), "registered_users.json"), "r+", encoding="utf-8") as file:
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
        
        while True:
                
            os.system('cls')
            print("==========================================")
            print("============== LOGIN USER  ===============")
            print("==========================================")
            username = input("username (email address): ")
            if username == "0":
                mainMenu.mainMenu()
            existing_user =  next((x for x in existing_users if x['email'] == username), None)
            if not existing_user:
                print("\n========================")
                print("\u26D4 Username (email) not found - please try again or press 0 for Main Menu")
                time.sleep(1.5)
            else:
                break
        while True:
                
            os.system('cls')
            print("==========================================")
            print("============== LOGIN USER  ===============")
            print("==========================================")
            password = maskpass.askpass(prompt=f"password for user '{existing_user['name']}': ")
            if password == "0":
                mainMenu.mainMenu()
            matching_password =  next((x for x in existing_users if x['password'] == password), None)
            if not matching_password:
                print("==========================================")
                print("\u26D4 Wrong password - please try again or press 0 for Main Menu")
                time.sleep(1)
            else:
                break
        loggedUser = User(
            userID=existing_user["userID"],
            address=existing_user["address"],
            email=existing_user["email"],
            password=existing_user["password"],
            name=existing_user["name"],
            phone=existing_user["phone"]

        )

        user_menu.main(loggedUser)
        return
    
