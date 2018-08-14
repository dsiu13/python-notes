# Dictionaries
- Dictionaries can store an unlimited amount of information
- Dictionaries are a collection of key-value pairs. Each key is connected to a value. You use the key to access the value associated.
- A key's value can be a number, string, list, or another dictionary
- To grab the value associated with a key, give the name of the dictionary and then place the key inside a set of [] - alien_0['color'] -> Green
- you can have unlimited key value pairs in a dictionary

## A simple dictionary
```
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

## Adding New Key-Value pairs
- Dictionaries are dynamic structures, you can add new key-value pairs at any time.
- Python does not care about the order in which key-value pairs are stored. It only cares avout the connection between keys and values
```
alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

```

## Starting with an Empty dictionary
- to create an empty dictionary, we define a dictionary using {}, and then
add each key-value pair on its own line.
```
alien_0 = {}

alien_0['color'] = 'green'

alien_0['points'] = 5

print(alien_0)

```

## Modifying Values within a Dictionary
- Modifying a value is done by giving the name of the dictionary with the key in [] and then the new value assigned to that key

```
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'

alien_0 = {'color': 'yellow'}
```

## Removing Key-Value Pairs
- you can use the 'del' statement to remove a key-value pair
- the deleted key-value pair is removed **permanently**
```
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
```

## A Dictionary of similar objects
- you can also use a dictionary to store one kind of info about many objects

```
fav_language = {
  'jen': 'java',
  'sarah': 'c',
  'ed': 'javascript',
  'phil': 'python'
}

```

## 6-1 Person & 6-2 Favorite Numbers
```
person = {
  'first': 'jeff',
  'last': 'winger',
  'age': '35',
  'city': 'greendale'
}

fav_nums = {
  'freddy': 13,
  'james': 7,
  'emily': 5,
  'bob': 8,
  'linda': 11
}

for key, value in fav_nums.items():
  print(key + ' favorite number is ' + str(value))
```

## 6-3 Glossary
```
glossary = {
  'one': 'monday',
  'two': 'tuesday',
  'three': 'wednesday',
  'four': 'thursday',
  'five': 'friday'
}

for key, value in glossary.items():
  print(key + ': ' + value)
```


## Looping through all Key-Value Pairs
- looping through keys is the default behavior when going through a dictionary
- you can use keys() method if it makes your code easier to read
- you can access value associated with any key you care about inside the loop by using the current key
- The key() method returns a list of all keys
```
for name in favorite_languages.keys():
  print(name.title())

for name in favorite_languages:
```

## Grabbing values by key
```
fav_language = {
  'jen': 'java',
  'sarah': 'c',
  'ed': 'javascript',
  'phil': 'python'
}


friends = ['phil', 'sarah']

for name in favorite_languages.keys():
  print(name.title())

  if name in friends:
    print(" Hi " + name.title() + ' you like ' + favorite_languages[name].title())

```
## Looping through a dictionary's keys in order
- There is no predictable order from the items in a dictionary.
- There is only a clear connection between each key and its assigned value
- One way to get order is to use sorted()

```
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

for name in sorted(favorite_languages.keys()):
   print(name.title() + ", thank you for taking the poll.")

```

## Looping through all Values in a Dictionary
- If you interested in the values that a dictionary contains, you can use values()
- Values() returns a list of values without their keys
- when you use the set() method, you pull all unique values
```
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

```

## 6-4 Glossary 2
```
glossary = {
  'one': 'monday',
  'two': 'tuesday',
  'three': 'wednesday',
  'four': 'thursday',
  'five': 'friday'
}

for key, value in glossary.items():
  print(key + ': ' + value)

```

## 6-5 Rivers
```
rivers = {
  'mississippi': 'mississippi river',
  'amazon': 'amazon river',
  'germany': 'rhine river',
  'china': 'yangtze river',
  'mexico': 'rio grande river'  
}

for key, value in rivers.items():
  print(key + ' has the ' + value)

```

## 6-6 Polling
```
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah', 'ted']
for name in favorite_languages.keys():

  if name in friends:
    print('hi ' + name.title() + ' you like ' + favorite_languages[name].title())
  else:
    print('hi ' + name.title() +' Please vote in our poll')

```

## Nesting
- Storing a set of Dictionaries in a list or a list of items as value in a dictionary is called **Nesting**.
- You can nest a set of Dictionaries inside a list, list of items, or another dictionary in a dictionary.

## A list of Dictionaries
- Its common to store a number of dictionaries in a list.
```
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
  print(alien)

aliens = []

for alien_number in range(30):
  new_alien = {'color': 'red', 'pts': 15, 'speed': 'fast'}
  aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
        alien['points'] = 10

```

## A list in a dictionary
- you can nest a list inside a dictionary anytime you want more than one value associated with a single key in a dictionary
```
pizza = {
  'crust': 'thin',
  'toppings': ['mushrooms', 'extra cheese']
}

```

## A dictionary in a dictionary
- you can nest a dictionary in a dictionary, but it can cause your code to become complicated
```
users = {
  'aeinstein':{
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton'
  },
  'mcurie':{
    'first': 'marie',
    'last': 'curie',
    'location': 'paris'
  }
}

```

## 6-7 People
```
greendale_students = {
  'jwinger': {
    'first': 'jeff',
    'last': 'winger',
    'job': 'law prof'
  },
  'aedison': {
    'first': 'annie',
    'last': 'edison',
    'job': 'fbi agent'
  },
  'tbarnes': {
    'first': 'troy',
    'last': 'barnes',
    'job': 'captain'
  }
}

for student, student_info in greendale_students.items():
  full_name = student_info['first'] + " " + student_info['last']
  job = student_info['job']
  print('id ' + student + " " + full_name + " " + job)

```

## 6-8 Pets
