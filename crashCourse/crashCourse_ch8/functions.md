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

you_are_a_wizard_harry(wizards)

```
