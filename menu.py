from manager import Manager

class Menu:
  def __init__ (self):
    self.manager = Manager()
    self.choices = {
            "1" : self.manager.create_order,
            "2" : self.manager.see_order, 
            "3" : self.manager.delete_order, #works
            "4" : self.manager.update_order,
            "5" : self.manager.save
            }
##main menu for the pizza store
  def display_menu (self):
    print("Welcome to DHMS Pizza!! ")
    print("................")

    print(""" What would you like today??
              1. Order Pizza
              2. See All Order
              3. Cancel My Order 
              4. Update My Order
              5. Save File""")

  def run(self):
    while True:
      self.display_menu()
      selection = input("Enter an option: " ) 
      action = self.choices.get(selection)
      if action:
        action()
      else:
        print("{0} is not a valid choice".format(selection)) 

