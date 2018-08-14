# IF Statements

## Simple Example
```
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == "bmw":
    print(car.upper())
  else:
    print(car.title())

```

## Conditional Tests
- Every 'if' statement is an expression that can be evaluated as either 'True' or 'False'
- Python uses these values to decide whether the code in the 'if' statement should be run

## Equality Operators
- the simplest Conditional test checks whether the value of a variable is equal to the value of interest
- Equality testing is **case sensitive** in Python
- You can check the value of both strings and integers
```
car = 'bmw'
car == 'bmw'

```

## Checking for Inequality
```
req_toppings = 'mushrooms'

if req_toppings != 'anchovies':
  print('hold the anchovies')
```

# Checking Multiple Conditions

### And
```
age_0 = 22
age_1 = 20

age_0 >= 21 and age_1 >= 21

```

### Or
```
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

```

# Checking whether a Value is in a List
- Checking for a value in a list we use the keyword 'in'
```
banned = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned:
  print("Weclome, " + user.title())
```

## Boolean Expressions
- a Boolean value is either True or False

## 5-1 Conditional Tests
```
dog = "shiba"

if dog == "shiba":
  print('Yes that is a Doge')

```

## 5-2
```
pet = 'dog'

if pet != 'dog'
  print('thats not your pet')

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == "bmw":
    print(car.lower())
  else:
    print(car.title())

```

## If Else Statements
```
age = 17

if age > 18:
  print('You're old enough to vote)
else:
  print('You can vote when you turn 18')
```

## If Else Chain
- You can use as many elif blocks are you'd like
- Python does not require an else block at the end of an if-elif chain.
```
age = 12

if age < 4:
  print('Free Admission')
elif age < 18:
  print('$5 Admission')
else:
  print('$10 Admission')
```

## 5-3 Alien Colors
```
alien_color = 'red'

if alien_color == 'green':
  print('Earned 5 Pts')
else:
  print('Wrong')

```

## 5-4 Alien Colors
```
alien_color = 'red'

if alien_color == 'green':
  print('Earned 5 Pts')
else:
  print('Earned 10 Pts')

```

## 5-5 Alien Colors
```
if alien_color == 'green':
  print('5 pts')
elif alien_color == 'yellow':
  print('10 pts')
elif alien_color == 'red':
  print('15 pts')
```

## 5-6 Stages of Life
```
age = 24

if age < 2:
  print('Baby')
elif age <= 2 or age < 4:
  print('Toddler')
elif age <= 4 or age < 13:
  print('Kid')
elif age <= 13 or age < 20:
  print('Teen')
elif age <= 20 or age < 65:
  print('Adult')
elif age <= 65:
  print('Elder')

```

## 5-8 Fruit
```
fav_fruits = ['apple', 'strawberry', 'banana']

if 'apple' in fav_fruits:
  print('You like apples')
if 'peach' in fav_fruits:
  print('you like peaches')
if 'banana' in fav_fruits:
  print('You like bananas')
if 'kiwi' in fav_fruits:
  print('you like kiwis')
if 'strawberry' in fav_fruits:
  print('you like strawberries')

```

# If Statements with Lists
- You can check for special values that need to be treated differently
- Manage changing conditions

## Checking for Special Items
```
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
      print("sorry we're out of green peppers")
    else:
      print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

```

## Checking that a List is not Empty
```
requested_toppings = []

if requested_toppings:
  for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '.')
else:
  print('Are you sure you want a plain pizza?')
```

## Multiple Lists
```
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:

if requested_topping in available_toppings:
  print("adding " + requested_topping + ".")
else:
  print("Sorry, we don't have any, " + requested_topping + ".")

print("\nFinished making your pizza!")

```

## 5-8 Hello Admin
```
users = ['Dean Pelton', 'jeff', 'annie', 'troy', 'abed', 'shirley', 'britta']

for user in users:
  if user == 'Dean Pelton':
    print('Hello Dean, would you like to see the Student Records?')
  else:
    print('Welcome to the Study Group Chat Room, ' + user.title())

```

## 5-9 No Users
```
users = []

if users:
  for user in users:
    print('Hello, ' + user.title())
else:
  print('You have no members in your study group :(')

```

## 5-10 Checking Usernames
```
current_users = ['jeff', 'annie', 'abed', 'britta']
new_users = ['hinkie', 'leeroy', 'frankie', 'jeff']

for new_user in new_users:
  if new_user.lower() in current_users:
    print('User name ' + new_user + ' is taken')
  else:
    print('welcome ' + new_user)

```

## 5-11 Ordinal Numbers
```
nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
  if num == 1:

```
