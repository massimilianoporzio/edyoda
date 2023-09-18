import re
import uuid
from builtins import staticmethod


import phonenumbers
from phonenumbers import geocoder

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

class User:
    def __init__(self,name,phone,email,address,password,userID = str(uuid.uuid4())) -> None:
        self.userID = userID
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.password = password

    def isValid(email):
        if re.fullmatch(regex, email):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.name} - Email: {self.email} - Password: {self.password} - Phone: {phonenumbers.format_number(self.phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)} - Address: {self.address} - userID: {str(self.userID)}"
    
    @staticmethod
    def createUser(existing_users):
        while True:
            user_name = input("Full Name: ")
            if user_name != "":
               existing_name = next((x for x in existing_users if x['name'] == user_name), None)
               if existing_name:
                   print("A User with the same name already exists.")
               else:
                   break
            else:
                print("Enter a non-empty string") 

        while True:
            try:
                user_input = input("Phone number: (International mobiles - +XX xxx xxxxxxx)")
                user_phone =phonenumbers.parse(user_input) 
                
                if phonenumbers.is_valid_number(user_phone):
                    break
                else:
                    raise Exception("Incorrect phone number")
            except Exception as ex:
                print("Enter a valid phone number (International Mobile: +XX xxx xxxxxxx)")
        while True:
            try:
                user_email = input("Email: ")
                if User.isValid(user_email):
                    existing_email = next((x for x in existing_users if x['email'] == user_email), None)
                    if existing_email:
                        print("A User with the same email address already exsists.")
                    else:
                        break
                else:
                    raise Exception("Invalid email")
            except:
                print("Enter a valid email address")
        
        user_address = input("Address: ")
        while True:
            try:
                print("Enter password matching alle the below criteria:\n")
                print("1. Atleast one uppercase character")
                print("2. Atleast one lowercase character")
                print("3. Minimum 8 characters long")
                print("4. Atleast one special symbol")
                print("5. Atleast one digit.")
                user_password = input("password: ")
                find = re.match(pattern,user_password)
                if find:
                    break
                else:
                    raise Exception("Not valid password")
            except:
                print("Enter a password matching the stated criteria")
        new_user = User(
            name=user_name,
            email=user_email,
            password=user_password,
            address=user_address,
            phone=phonenumbers.format_number(user_phone,phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        )
        return new_user

