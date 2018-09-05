# Functions

## Defining a Function
```
def hello():
  print('hello!')

hello()
```

## passing an arg to a function
```
def hello(name):
  print('hello! ' + name.title())

hello('james')
```

## Args and Parameters
- the var name is an example of a parameter. It is a piece of information the function needs to run.
- Args and Parameter are sometimes used interchangeably. Function defined variables are called args, while variables in the function call are parameters.

## 8-1 Messages
```
def display_msg():
  print("hello")

display_msg()
```

## 8-2 Favorite Book
```
def books(book):
  print('my favorite book is ' + book)

books()

```

## Passing Arguments
- A function definition can have multiple parameters, a function call may need multiple args
- you can pass args to your functions in a number of ways. The easiest way is **positional arguments**.
- When you call a function, python matches each argument with a parameter
- **Order matters** in positional arguments
- you can call a function as many times as you'd like
```
def pets(animal_name, animal_type):
  print(animal_name + " is a " + animal_type)

pets('kaylee', 'doge')

```

## Keyword Arguments
- a **keyword argument** is a name-value pair you pass to a function.
- you directly associate the name and the value within the arguments
- In keyword we tell python which values go with each other
```
def pets(animal_name, animal_type):
  print(animal_name + " is a " + animal_type)

pet(animal_name="kaylee", animal_type="doge")

```

## Default Values
- you can define a default value for each parameter. If no argument is passed, the function will use the default value provided.
- when you use default values, any parameter with a default value needs to be listed **after** all parameters that don't have default values.
```
def pets(animal_name="penny", animal_type):
  print(animal_name + " is a " + animal_type)

pet(animal_name="kaylee", animal_type="doge")

```

## Equivalent function calls
- Positional arguments, keyword arguments and default values can all be used together.
- Style doesn't matter, its personal pref
```
# A dog named Willie.

describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

```

## Avoiding Argument Errors
- Errors can occur if you provide too many or too few arguments for a function.

## 8-3 T-Shirt
```
def shirt(size, caption):
  print('shirt size of ' + size + ", caption of " + caption)

shirt('med', 'hello')

```
## 8-4 Large T-Shirt
```
def shirt(size='large', caption='i love python'):
  print('shirt size of ' + size + ", caption of " + caption)

shirt()
shirt('med')
```

## 8-5 Cities
```
def cities(city, country='usa'):
  print(city + ' is in ' + country)

cities('san francisco')
cities('san diego')
cities('kyoto', 'japan')  
```

## Return Values
- A function can return a value or set of values
- 'return' takes a value from inside a function and sends it back to the line that called in within the function

## Return a Simple Value
```
def name(first, last):
  full = first + " " + last
  return full.title()
```

## Optional Arguments
- You can use default values to make an argument optional so that people using the function can chose to provide extra info

## Returning a Dictionary
- A function can return any kind of value you need it to, including data structures
```
def build_person(first, last):
  person = {'first': first, 'last': last}
  return person
```

## Functions in a 'While' Loop
- We can pass a break condition to stop the loop
```
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

```

## 8-6 City Names
```
def city_country(city, country):
  location = city + ", " + country
  return location

```

## 8-7 Album
```
def album(artist, cd, yr, tracks=''):
  cd = {
    'artist_name': artist,
    'cd_name': cd,
    'year': yr,
    'track_count': tracks
  }
  return cd
```

## 8-8 User Album
```
def album(artist, cd, yr, tracks=''):
  cd = {
    'artist_name': artist,
    'cd_name': cd,
    'year': yr,
    'track_count': tracks
  }
  return cd

while True:
  print("(quit by entering 'q')")
if
```

## Passing a List
- When you pass a list to a function, the function gets direct access to the contents of the list.
```
def hello(names):
  for name in names:
    msg = "Hello " + name.title()
    print(msg)

usernames = ['jeff', 'annie', 'abed']
hello(usernames)

```

## Modifying a List in a Function
- When you pass a list to a function, the function can modify the list.
- Any changes made to the list within the function body are **permanent**
```
unprinted = ['d20', 'tiny robot', '3DS']
completed = []

while unprinted:
  current_designs = unprinted.pop()
  print(current_designs + " printed")
  completed.append(current_designs)

for complete in completed:
  print(completed)

```

## Prevent List modification within a Function
- You can send a copy of a list instead to prevent any changes to a list.
```
function_name(list_name[:])

```

## 8-9 Mages
```
wizards = ['harry', 'hermione', 'ron']

def you_are_a_wizard_harry(names):
  for name in names:
    print(name)

you_are_a_wizard_harry(wizards)
```

## 8-10 Great Mages
```
wizards = ['harry', 'hermione', 'ron']

def you_are_a_wizard_harry(names):
  for name in names:
    print('auror ' + name)

you_are_a_wizard_harry(wizards[:])

```

## Passing an Arbitrary Number of Arguments
- Python allows you to pass an arbitrary number of Args
- the asterisk creates an empty tuple called 'arguement', and puts whatever values it receives into the tuple
```
def make_pizza(*toppings):
  print(toppings)

make_pizza('extra cheese', 'mushrooms', 'pepperoni')
```

## Mixing Positional and Arbitrary
- Any arbitrary arguements must be placed last, as python matches positional and keyword arguments first
```
def make_pizza(size, *toppings):
  print(size + toppings)

make_pizza(16, 'extra cheese', 'mushrooms', 'pepperoni')

```

## Arbitrary Keywords
- You can write functions that accept as many key-value pairs as the calling statement provides
- You can mix positional, keyword, and arbitrary values in different ways when writing your own functions.
```
def build_profile(first_name, last_name, **user_info):
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last

  for key, value in user_info.items():
    profile[key] = value
  return profile

user_profile = build_profile('bob', 'smith',
location='princeton', field='econ')

print(user_profile)
```
## 8-12 Sandwiches
```
def build_sandwich(*ingredients):
  print(ingredients)

build_sandwich('cheese','ham','lettuce')
build_sandwich('cheese','ham','lettuce', 'tomato')
build_sandwich('cheese','tuna','lettuce', 'tomato', 'jalpenos')   
```

## 8-13 User Profile
```
def build_profile(first_name, last_name, **user_info):
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last

  for key, value in user_info.items():
    profile[key] = value
  return profile

user_profile = build_profile('jeff', 'winger',
location='greendale', field='law')

print(user_profile)

```

## 8-14 Cars
```
def build_car(manufacturer, model, **kwargs):
  car = {}
  car['maker'] = manufacturer
  car['car_name'] = model

  for key, value in kwargs.items():
    car[key] = value

  return car

built_car = build_car('bmw', 'i3', color='grey')
print(built_car)

```

## Storing Functions in Modules
- You can store a function in a separate file called a **module** and then **import** that module into your main program
- An **import** statement tells Python to make the code in the module available in the current file.
- Using modules allows you to hide, reuse, or share parts of your code easier
- Multiple ways to import a module

## Importing an Entire Module
- Importing the entire module gives you access to every function in the module

### pizza.py
```
def make_pizza(size, *toppings):
  print("\nMaking a " + str(size) +
      "-inch pizza with the following toppings:")
  for topping in toppings:
      print("- " + topping)
```

### making_pizza.py
```
import pizza

pizza.make_pizza(16, 'pepperoni')

pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

```

## Importing Specific functions
- from module_name import function_name
- you can import as many functions via a comma separated list -> **from module_name import function_1, function_2, function_3**

### making_pizza.py
```
import pizza import make_pizza

pizza.make_pizza(16, 'pepperoni')

```

## Using 'as' to give a Function an Alias
- If the name of a function might conflict with an existing name or if the function name is long, you can use an **Alias**
- The import statement renames the function to the alias
- from module_name import function_name as fn
```
from pizza import make_pizza as mp
mp(16, 'pepperoni')

```

## Using 'as' to give a Module an Alias
- All functions retain their original name
- import module_name as mn
```
import pizza as p

p.make_pizza(16, 'pepperoni')

```

## Importing all functions in a Module
- Python can import every function using the asterisks operator
- the asterisks tells python to copy every function
- Better practice to import the desired function or functions. Or to import the entire module instead to reduce name conflicts
```
from pizza import *

make_pizza(16, 'pepperoni')

```

## Styling Functions
- Use descriptive names for functions. lower case and underscores
- Comment your functions to explain what they do
- no spaces after or before value assignment
```
def function_name(parameter_0, parameter_1='default value')

function_name(value_0, parameter_1='value')

```  
- No more than 79 chars in a line
- import statements at the beginning of the file
