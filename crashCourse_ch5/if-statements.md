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
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == "bmw":
    print(car.upper())
  else:
    print(car.title())

```
