# Classes and Objects
- A class is a logical collection of attributes and methods.
- An object is an instance of a Class

# Attributes and Methods

## Class vs instance attribute
- This is a class attribute.
```
class Employee:
  working_day = 40

employee_one = Employee()
employee_one.working_day => 40

Employee.working_day = 50
employee_one.working_day => 50
```

- An instance attribute is specific to the Object itself.
- If you call employee_two.name it won't exist because the name attribute is specific only to employee_one.
- If we change the working_day for employee_one, the change will not show on employee_two. We did not change the value of our Class attribute, but we created a new instance attribute of working_day for employee_one.
```
employee_one.name = "Bob"
employee_one.name => Bob

```

- Python will check for an instance attribute, and then check for a class attribute, it will then throw an error if it doesn't exist

# Self Parameters
- If we don't pass **self** we're going to get a argument passed error
- This occurs because it uses the name of the class and then the name of the method, and passes the Object as the argument.
- For example. bob.employee_details => Employee.employee_details(bob)
- bob.employee_details is shorted syntax for the 2nd. Python passes Bob to the function call as an argument.
```
class Employee:
  def employee_details(self, name):
    self.name = name

bob = Employee()
bob.employee_details

Employee.employee_details(bob)
```

# Static Methods and Instance Methods
- Instance methods make use of the self parameter to modify and access the instance attribute of your class.
- Static methods do not take the default self parameter
```
class Employee:
  def employee_info(self):
    self.name = "Ben"

  @staticmethod
  def welcome():
    print("Welcome!")

```
