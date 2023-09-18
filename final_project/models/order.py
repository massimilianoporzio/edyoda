import uuid
from builtins import staticmethod

class Order:
    def __init__(self,userID,total=0,food_items=[],orderID = str(uuid.uuid4())) -> None:
        self.userID = userID
        for item in food_items:
            total += item.price * (100-item.discount)/100