import os
import json
import time
from users import user_menu,place_order
from models.user import User

def main(logged_user):
     with open(os.path.join(os.path.dirname(__file__), "./../admin/data/registered_users.json"), "r+", encoding="utf-8") as file:
        file.seek(0)
        try:
            data = json.load(file)
        except Exception as ex:
            print("\u26D4 - Something went wrong")
            time.sleep(2)
            user_menu.main(logged_user=logged_user)
            file.close()
            return
        existing_users = data["users"]
        user_to_update = next((x for x in existing_users if x['userID'] == logged_user.userID), None)
        index_of_user_to_update = existing_users.index(user_to_update)
        os.system('cls')
        print(f"=== Logged as: {logged_user.name} ===".center(36,"="))
        print(" UPDATE PROFILE ".center(36," "))
        print("====================================")
        updated_user = User.updateUser(existing_users=existing_users,user_to_update=logged_user)
        user_dict = vars(updated_user)
        existing_users[index_of_user_to_update]=user_dict
        data["users"]=existing_users
        file.seek(0)
        file.truncate(0)
        try:
            json.dump(data,file,indent=4)
            file.close()
        except:
            print("\u26D4 - Something went wrong")
            file.close()
        else:
            print("\U00002714 user profile updated successfully")
        
        time.sleep(1.5)
        user_menu.main(logged_user=updated_user)
        
        