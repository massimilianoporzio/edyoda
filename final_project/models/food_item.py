import uuid
class FoodItem:
    def __init__(self,name,quantity,price,discount,stock) -> None:
        self.FoodID = str(uuid.uuid4())
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
    def __str__(self) -> str:
        return f"{self.name} ({self.quantity}) [INR {self.price}] - discount: {self.discount}% - Stock: {self.stock}"
