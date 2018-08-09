# Lists
- A list is a collection of items in a particular order.
- In python ([]) square brackets indicate a list, individual objects are separated by commas.

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

```
- Printing a list will return the entire list

# Accessing Elements in a List
- Lists are ordered collections, so you can access any element in a list by telling Python the index of the item you want
- bicycles[0] -> trek
- You can add string methods onto this

# Index Positions start at 0, Not 1.
- The first item in a list is at position 0.
- Python has a special syntax for accessing the last element in a list. Asking for an element at index -1 will always return the last item. index[-2], will return the 2nd to the last element, and so on.
- Useful for when you don't know how long the list will be.

# Individual Values from a List
```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

My first bicycle was a Trek.

```

# Changing, Adding, and Removing Elements

## Changing
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

['honda', 'yamaha', 'suzuki']

```
- You can change the value of any elements in a list.
```
motorcycles[0] = 'ducati'
print(motorcycles)

['ducati', 'yamaha', 'suzuki']
```

## Adding Elements to a List
- Easiest way to add elements to a list is to use "Append"
- When you append an item to a list, the new element is added to the end.
```

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

['honda', 'yamaha', 'suzuki', 'ducati']

```
- Append() makes it easy to build dynamic lists.

## Inserting Elements
- You can inset a new element at any position in your list with INSERT(). Insert takes two arguments. The 1st is the position where you want the element, the 2nd is the element.
```
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

['ducati', 'honda', 'yamaha', 'suzuki']

```

## Removing Elements
```

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)

['yamaha', 'suzuki']

```
- You can also remove elements with the Pop() method
- by default Pop() removes the last item in the list
- You can specify by passing an index value to Pop(0)

```
motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles)

['honda', 'yamaha']

print(popped_motorcycle)
suzuki

```

## Removing an Item by Value
```
['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)

```
- Python will figure out where the value is and remove it
- Remove() only deletes the first occurrence, you need to loop if you want to remove every instance of the element

# Ch3 Exercises
## 3-4 Guest List
```
guest_list = ["Bob", "Jane", "John", "Lana", "Sterling"]

for x in guest_list:
  print("Dinner invitation for " + x)

```

## 3-5 Changing Guest List
```
guest_list = ["Bob", "Jane", "John", "Lana", "Sterling"]

missing_guest = "John"
guest_list.remove(missing_guest)

print(missing_guest)

for x in guest_list:
  print("Dinner invitation for " + x)

```

## 3-6 Changing Guest List
```
import math

guest_list = ["Babou", "Mallory", "Lana", "Sterling"]
guest_list.insert(0, 'Dr.Krieger')

middleIndex = math.ceil((len(guest_list))/2)
guest_list.insert(middleIndex, 'Ray')

guest_list.append('Cheryl')

for x in guest_list:
  print("Dinner invitation for " + x)

```

## 3-7 Shrinking Guest List
```
guest_list = ["Babou", "Cheryl", "Lana", "Sterling"]

i = len(guest_list)
while i > 2:
  print("Sorry " + guest_list.pop())
  i -= 1

for x in guest_list:
  print("Still invited " + x)

del guest_list[0]
del guest_list[0]

print(guest_list)
```
