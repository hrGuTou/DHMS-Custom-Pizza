
"""
Main CRUD methods

"""

from order import OrderPizza
# import json
import pickle

class Manager:
  def __init__ (self):
    self.orders = {}
   # self.id = 0

#Implementing the CRUD Methodology
# Create Order for the custome pizza
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
    
    self.orders[phoneNumber] = OrderPizza(pizzaType, name, phoneNumber, topping, sauce)

    print("Order created! \n")

  def save(self):
    with open("tasks.json", "wb") as fp:   #Pickling
      pickle.dump(self.orders, fp)
      print("\nTasks saved! \n\n")
  def load(self):
    with open("tasks.json", "rb") as fp:   #Unpickling
      self.orders = pickle.load(fp)
      self.latest_ID = len(self.orders)
      print("Tasks loaded!")
  
  # Update order for custom pizza
  def update_order(self):
    while True:
      try:
        customer = int(input("Please enter your phone number to update your order: "))
      except:
        print("Please enter numbers!")
        continue
      else:
        break

    while customer not in self.orders:
      while True:
        try:
          customer = int(input("The option you entered does not exist, please try again, or press '0' to quit: "))
        except:
          print("Please enter numbers!")
          continue
        else:
          break
      
      if customer == 0:
        return
    
    order = self.orders[customer]

    print("""    
                     1. Update your pizza type

                     2. Update your name 

                     3. Update your topping

                     4. Update your sauce

                     0. Cancel""")

    choice = input("Enter an Option: ")
    if(choice == '1'):
      newType = input("New pizza type: ")
      order.setType(newType)
    elif(choice == '2'):
      newName = input("New name: ")
      order.setName(newName)
    elif(choice == '3'):
      newTopping = input("New topping: ")
      order.setTopping(newTopping)
    elif(choice == '4'):
      newSauce = input("New sauce: ")
      order.setSauce(newSauce)
    else:
      pass
      
    print("Done! \n")

# Deleting order for custom Pizza
  def delete_order(self):
    
    while True:
      try:
        customer = int(input("Please enter your phone number to update your order: "))
      except:
        print("Please enter numbers!")
        continue
      else:
        break

    while customer not in self.orders:
      while True:
        try:
          customer = int(input("The option you entered does not exist please try again, or press '0' to quit: "))
        except:
          print("Please enter numbers!")
          continue
        else:
          break
  
    del self.orders[customer]

    print("Thank you! Your order has been deleted! \n")
 
 # Read the custom pizza

  def see_order(self):

    if not self.orders:
      print("No orders yet. \n")
      return
    
    for order in self.orders:
      print(self.orders.get(order))


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

