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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descript())
my_new_car.read_odometer()

```
