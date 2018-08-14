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

## Looping through all Key-Value Pairs
