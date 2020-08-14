"""
Main CRUD methods

"""
import json
import sys

from order import OrderPizza
import pickle


class Manager:
    def __init__(self):
        self.orders = {}
        self.load()

    # Implementing the CRUD Methodology
    # Create Order for the customer pizza
    def create_order(self):
        name = input("Please enter your name: ")
        while True:
            try:
                phoneNumber = int(input("Please enter your 10 digit phone number: "))
            except:
                print("Please enter numbers!")
                continue
            else:
                break

        pizzaType = input("What type of pizza would you like to order? : ")
        topping = input("What topping would you like? : ")
        sauce = input("What sauce would you like? : ")

        self.orders[str(phoneNumber)] = OrderPizza(pizzaType, name, phoneNumber, topping, sauce)

        self.save()

        print("Order created! \n")

    # Update order for custom pizza
    def update_order(self):

        customer = input("Please enter your phone number to update your order: ")

        while customer not in self.orders:
            customer = input("The order you entered does not exist, please try again or press 'q' to exit: ")
            if customer == 'q':
                return

        order = self.orders[customer]

        print("""    
                     1. Update your pizza type

                     2. Update your name 

                     3. Update your topping

                     4. Update your sauce

                     0. Cancel""")

        choice = input("Enter an Option: ")
        if (choice == '1'):
            newType = input("New pizza type: ")
            order.setType(newType)
        elif (choice == '2'):
            newName = input("New name: ")
            order.setName(newName)
        elif (choice == '3'):
            newTopping = input("New topping: ")
            order.setTopping(newTopping)
        elif (choice == '4'):
            newSauce = input("New sauce: ")
            order.setSauce(newSauce)
        else:
            pass

        print("Done! \n")

    # Deleting order for custom Pizza
    def delete_order(self):
        customer = input("Please enter your phone number to delete your order: ")

        while customer not in self.orders:
            customer = input("The order you entered does not exist, please try again or press 'q' to exit: ")
            if customer == 'q':
                return

        del self.orders[customer]

        print("Thank you! Your order has been deleted! \n")

    # Read the custom pizza

    def see_order(self):
        if not self.orders:
            print("No orders yet. \n")
            return

        for order in self.orders:
            print(self.orders.get(order))

    def quit(self):
        self.save()
        print("BYE")
        sys.exit()

    def clear(self):
        try:
            self.orders = {}
            self.save()
        except:
            pass
        else:
            print("ALL ORDERS DELETED")

    def save(self):
        try:
            with open("tasks.json", "w") as fp:
                fp.write(json.dumps(self.orders, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        except Exception as e:
            print(e)
        else:
            fp.close()
            print("\nTasks saved! \n")

    def load(self):
        try:
            with open("tasks.json", "r") as fp:
                data = json.load(fp)
                decoded = Manager.from_json(data)
                self.orders.update(decoded)

        except:
            pass
        else:
            fp.close()

    @classmethod
    def from_json(cls, data):
        decoded = {}

        for key, val in data.items():
            decoded[key] = OrderPizza.from_json(val)

        return decoded

#   ## write my data to a JSON file
#   def save(python_data):
#     with open('data.json', 'w') as output_file:
#       json.dump(python_data, output_file, indent=4) 


#   ## read data from JSON file
#   def load():
#     with open('data.json', 'r') as json_file:
#       data = json.load(json_file)
#       print(data)

# # Serializing
# data = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# print(data)


# # Deserializing
# decoded_team = self.from_json(json.loads(data))
# print(decoded_team)
# print(decoded_team.students)
