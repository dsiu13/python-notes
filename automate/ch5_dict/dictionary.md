# The Dictionary Data Type
- A **dictionary** is a collection of many values. But unlike indexes for lists, indexes for dictionaries can use many different data types, not just integers. Indexes for dictionaries are called keys, and a key with its associated value is called a **key-value pair**.
- Dictionaries are typed {} => myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# Dictionaries vs List
- Items in dictionaries are unordered unlike lists.
- There is no first item in a dictionary, while order matters for determining whether two lists are similar.
- Order does not matter for key-value pairs.
- Dictionaries cannot be sliced like lists.
- You can have arbitrary values for the keys so you can organize your data

# keys(), values(), and items()
- These three dictionary methods will return list-like values of the dictionary's keys, values, or the key and values.
- The values returned by these methods are not true lists: They cannot be modified and do not have an append() method.
- You can use these in **for loops**. Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary
- If you want a true list from one of these methods, pass its list-like return value to the list() function.
- You can also use the multiple assignment trick in a for loop to assign the key and value to separate variables.

### Values()
```
spam = {'color': 'red', 'age': 42}

for v in spam.values():
  print(v)

red
42
```

### Keys()
```
spam = {'color': 'red', 'age': 42}

for k in spam.keys():
  print(k)

color
age

```

### Items()
```
spam = {'color': 'red', 'age': 42}

for i in spam.items():
  print(i)

('color', 'red')
('age', 42)

```

### True List
```
spam = {'color': 'red', 'age': 42}

spam.keys()
dict_keys(['color', 'age'])

list(spam.keys())
['color', 'age']

```

### Multiple assignment
```
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
  print('Key ' + k + 'Value ' + v)

Key: age Value: 42
Key: color Value: red

```

# Checking Whether a Key or Value Exists in a Dictionary
- the **in** and **not in** operators can check whether a value exists in a list
- 'color' in spam is essentially a shorter version of writing 'color' in spam.keys(). This is always the case: If you ever want to check whether a value is (or isn’t) a key in the dictionary, you can simply use the **in** or **not in** keyword with the dictionary value itself.
```
spam = {'name': 'Bob', 'Age': 42}

'name' in spam.keys()
>>> true

'Jeff' not in spam.values()
>>> true

'color' in spam.values()
>>> false

'color' in spam
False

```

## get() method
- The **get() method** takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.
- Since eggs doesn't exist as a key, we get the default value of 0 returned.
```
picnic_basket = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnic_basket.get('cups, 0')) + ' cups'
>> 'I am bringing 2 cups.'

'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
>> 'I am bringing 0 eggs.'
```

## setdefault() Method
- You’ll often have to set a value in a dictionary for a certain key only if that key does not already have a value.
- setdefault() takes two arguments.
- The first argument passed is the key to check for, and the second is the value to set at that key if the key doesn't exist.
- If the key does exist it returns the key's value.
```
picnic_basket = {'apples': 5, 'cups': 2}
if 'water' not in picnic_basket:
  picnic_basket['water'] = 3
```

## Pretty printing
- you can import the **pprint module** which gives you the **pprint()** and the **pformat()** methods.
- this will give you a cleaner display.
- The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

# Data Structures to Model Real-World Things
- You can data to model real-world things. and you can write code to work with this model. This is where lists and dictionaries can come in.

# Nested Dictionaries and Lists
-  Lists are useful to contain an ordered series of values, and dictionaries are useful for associating keys with values.


# Summary
Lists and dictionariesare values that can contain multiple values, including other lists and dictionaries. 
- Dictionaries are useful because you can map one item (the key) to another (the value), as opposed to lists, which simply contain a series
of values in order.
- Values inside a dictionary are accessed using square brackets just as with lists. Instead of an integer index, dictionaries can have keys of a variety of data types: integers, floats, strings, or tuples.
- By organizing a program’s values into data structures, you can create representations of real-world objects
