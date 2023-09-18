import uuid
import datetime
from builtins import staticmethod

class Order:
    def __init__(self,userID,total=0,food_items=[],created_at=datetime.datetime.now(), orderID = str(uuid.uuid4())) -> None:
        self.userID = userID
        self.created_at = created_at
        self.orderID = orderID
        self.food_items = food_items
        self.total = 0
        for item in food_items:
            self.total += item.price * (100-item.discount)/100
    
    def __str__(self) -> str:
        result =f"Order #: {self.orderID} - created at: {datetime.datetime.strftime(self.created_at,'%d/%m/%Y %H:%M')} by User: {self.userID}\nItems in order:\n"
        for item in self.food_items:
            result += repr(item)+"\n"
        return result
    def __repr__(self) -> str:
        result =f"created at: {datetime.datetime.strftime(self.created_at,'%d/%m/%Y %H:%M')}"
        result +="\nItems in order:\n"
        for item in self.food_items:
            result += repr(item)+"\n"
        result +f"\nTotal (INR): {self.total}"
        return result
    
    
