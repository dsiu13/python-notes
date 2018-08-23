class Restaurant():

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.customers_served = 0

  def describe_restaurant(self):
    print("we are " + self.restaurant_name + " specializing in " + self.cuisine_type + " food")

  def open_restaurant(self):
    print(self.restaurant_name + " is now open")

  def update_served(self, served):
    self.customers_served = served

  def restaurant_stats(self):
    print(str(self.customers_served))

  def increment_served(self, customers):
    self.customers_served += customers
