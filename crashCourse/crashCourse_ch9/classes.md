# Classes

## Object-oriented programming
- Object oriented programming is an effective approach to writing software.
- in OOP you write classes that represent real-world things or situations and create objects based on those classes.
- When you create individual objects from the class, each object is automatically equipped with the general behavior
- Making an object from a class is called **instantiation**, and you work with an instance of a class


## Creating and Using a Class
- init() is a special python method.
- 'self' parameter is required, and it must come before any other parameter. Required because when python calls init(), it will automatically pass self as an argument
- Every method call associated with a class automatically passes self, it is a reference to the instance itself
- it gives the individual instance access to the attributes and methods in the class.
- **self prefix**  Variables with the self prefix is available to every method in the class. the variable takes the value of the parameter
- Variables that are accessible through instances like this are called attributes.
```
class Dog():
  def __init__(self, name, age):
  self.name = name
  self.age = age

  def set(self):
    print(self.name.title() + " is now sitting")

  def roll_over(self):
    print(self.name.title() + " rolled over")    
```

## Making an Instance from a Class
- A **class** is a set of instructions for how to make an instance
- there is no explicit return statement in init(), but Python automatically returns an instance representing the class
- In the example below, **my_dog** refers to a single instance created from a Class
```
class Dog():
  def __init__(self, name, age):
  self.name = name
  self.age = age

  def set(self):
    print(self.name.title() + " is now sitting")

  def roll_over(self):
    print(self.name.title() + " rolled over")  

my_dog = Dog('kaylee', 4)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

```

### Accessing attributes
- To access Attributes of an instance, you use dot notation.
- my_dog.name

### Calling Methods
- After we create an instance from a class, we can also use dot notation to call any Method defined within the Class
- my_dog.sit() or my_dog.roll_over()

### Creating Multiple Instances
- You can create as many instances from a Class as you need.

## 9-1 Restaurant
```
class Restaurant():

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print("we are " + self.restaurant_name + " specializing in " + self.cuisine_type + " food")

  def open_restaurant(self):
    print(self.restaurant_name + " is now open")

my_restaurant = Restaurant('Taco Town', 'Mexican')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

```
## 9-2 Three Restaurant
```
class Restaurant():

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print("we are " + self.restaurant_name + " specializing in " + self.cuisine_type + " food")

  def open_restaurant(self):
    print(self.restaurant_name + " is now open")

taco_town = Restaurant('Taco Town', 'Mexican')
dumpling_house = Restaurant('Dumpling House', 'Chinese')
garden_fresh = Restaurant('Garden Fresh', 'Vegan')

taco_town.describe_restaurant()
dumpling_house.describe_restaurant()
garden_fresh.describe_restaurant()

```

## 9-3 Users
```
class Users():
  def __init__(self, first_name, last_name, username):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username

  def user_summary(self):
    print(self.first_name + " " + self.last_name + " , username:" + self.username)

  def greet_user(self):
    print('Hello ' + self.first_name + "!")

jeff = Users('Jeff', 'Winger', "wingman")
jeff.user_summary()
jeff.greet_user()

annie = Users('Annie', 'Eddison', 'aeddison')
annie.user_summary()
annie.greet_user()
```

## Working with Classes and Instances
```
class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descript(self):
    return str(self.year) + ' ' + self.make + ' ' + self.model

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descript())
my_new_car.read_odometer()

```
- You can modify the attributes of an instance directly or write methods that update attributes in specific ways.
- You can modify an attribute's value in three ways.
1. you can change the value directly through the instance
2. set the value through the method
3. Increment the value through a method

### modifying an attribute directly
- my_new_car.odometer_reading = 23
- my_new_car.read_odometer()
- This line tells Python to take the instance, find the attribute and set the value of the attribute to the new value.

### modifying an attribute through a method
```
class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descript(self):
    return str(self.year) + ' ' + self.make + ' ' + self.model

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descript())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

```

### Incrementing an attribute value through a Method
```
class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descript(self):
    return str(self.year) + ' ' + self.make + ' ' + self.model

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    self.odometer_reading = mileage

  def increment_odometer(self, miles):
    self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013 print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

```

## 9-4 Restaurant
```
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


<!-- #1 -->
my_restaurant = Restaurant('Garden Fresh', 'Vegan')
my_restaurant.update_served(6)
my_restaurant.restaurant_stats()

<!-- #2 -->
my_restaurant = Restaurant('Garden Fresh', 'Vegan')
my_restaurant.customers_served = 5
my_restaurant.restaurant_stats()

<!-- #3 -->
my_restaurant = Restaurant('Garden Fresh', 'Vegan')
my_restaurant.customers_served = 5
my_restaurant.increment_served(23)
my_restaurant.restaurant_stats()

```

## 9-5 Login Attempts
```
class Users():
  def __init__(self, first_name, last_name, username):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.logins = 0

  def user_summary(self):
    print(self.first_name + " " + self.last_name + " , username:" + self.username)

  def greet_user(self):
    print('Hello ' + self.first_name + "!")

  def login_attempts(self):
    self.logins += 1

```

## Inheritance
- If the Class you are writing is a specialized version of another class you wrote, you can use Inheritance.
- When a class inherits from another, it automatically takes on all attributes and methods of the first class
- The original is the **parent class**. While the new class is the **child class**
- The child class inherits methods and attributes of its parent. It can also define new methods and attributes as well

## init Method for a Child Class
- The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class
```
class Car():

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    print(str(self.year) + ' ' + self.make + ' ' + self.model)

  def read_odometer(self):
    print(str(self.odometer_reading))

  def update_odometer(self, mileage):
    if milage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print('nope')

  def increment_odometer(self, miles):
      self.odometer_reading += miles

class ElectricCar(Car):

  def __init__(self, make, model, year):
    super().__init__(make, model, year)

my_telsa = ElectricCar('Tesla', 'model s', 2016)
my_telsa.get_descriptive_name()

```

## Defining Attributes and Methods for the Child Class
- you can add any new attributes and methods necessary to differentiate the child class from the parent class.
- There’s no limit to how much you can specialize a child class
```
class ElectricCar(Car):

  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = 70

  def describe_battery(self):
    print('Battery size: ' + str(self.battery_size))

my_telsa = ElectricCar('Tesla', 'model s', 2016)
my_telsa.get_descriptive_name()
my_tesla.describe_battery()

```

## Overriding Methods from the Parent Class
- You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class
- Define a method in the child class with the same name as the method you want to override.
- Python will now ignore the parent class method, and use the child class method instead

## Instances as Attributes
- You can break your large class into smaller classes that work together.

## 9-6 Ice Cream Stand
```
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

class iceCreamStand(Restaurant):
  def __init__(self, restaurant_name, cuisine_type):
    super().__init__(self, restaurant_name, cuisine_type)

  def flavors():
    print('vanilla', 'chocolate', 'strawberry')

iceCreamStand.flavors()
```

## 9-7 + 9-8 Admin
```
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

```

## 9-9 Battery Upgrade
```
class Car():

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    print(str(self.year) + ' ' + self.make + ' ' + self.model)

  def read_odometer(self):
    print(str(self.odometer_reading))

  def update_odometer(self, mileage):
    if milage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print('nope')

  def increment_odometer(self, miles):
      self.odometer_reading += miles

class Battery():

  def __init__(self, battery_size=60):
      """Initialize the batteery's attributes."""
      self.battery_size = battery_size

  def describe_battery(self):
      print("This car has a " + str(self.battery_size"-kWh battery.")


  def get_range(self):
      if self.battery_size == 60:
          range = 140
      elif self.battery_size == 85:
          range = 185

      message = "This car can go approximately " + str(range)
      message += " miles on a full charge."
      print(message)

  def upgrade_battery(self):
       if self.battery_size == 60:
          self.battery_size = 85
          print("Upgraded the battery to 85 kWh.")
      else:
          print("The battery is already upgraded.")

class ElectricCar(Car):

  def __init__(self, make, model, year):
    super().__init__(make, model, year)

my_telsa = ElectricCar('Tesla', 'model s', 2016)
my_telsa.get_descriptive_name()

```

# Importing Classes
- You can store as many classes as you need in a single module.
- Importing an Entire Module -> import module_name
- All Class -> from module_name import *
- You can import Modules into other Modules

## Importing a Single Class
- from file import Class Name -> from car import Car

## Importing Multiple Classes from a Module
- You can import as many classes as you need into a program file.
- If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar
- from car import Car, ElectricCar

## Standard Python Library
- A set of modules included with every Python install
- OrderedDict is an example of a standard Library
- normally dictionaries don't keep track of order
```
from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages['jen'] = python
fav_languages['sarah'] = 'c'

```
