"""

Individual order
class order
- pizza type
- topping
- sauce
- customer name 
- customer phone number

"""
import json


class OrderPizza():

    def __init__(self, pizza_type, cust_name, cust_phonenum, toppings, sauce):
        self.type = pizza_type
        self.name = cust_name
        self.phonenumber = cust_phonenum
        self.toppings = toppings
        self.sauce = sauce
        # list_pizza=[] # emty list to store the selected pizza

    def setType(self, newType):
        self.type = newType

    def setName(self, newName):
        self.name = newName

    def setNumber(self, newPhone):
        self.phonenumber = newPhone

    def setTopping(self, newTopping):
        self.toppings = newTopping

    def setSauce(self, newSauce):
        self.sauce = newSauce

    def __str__(self):
        return f"\n Customer Name: {self.name},\n Customer Phone Number: {self.phonenumber},\n Type of Pizza: {self.type},\n Toppings: {self.toppings},\n Sauce: {self.sauce}\n"


    @classmethod
    def from_json(cls, data):
        type,name,phonenumber,toppings,sauce = data["type"],data["name"],data["phonenumber"],data["toppings"],data["sauce"]

        return cls(pizza_type=type, cust_name=name, cust_phonenum=phonenumber, toppings=toppings, sauce=sauce)