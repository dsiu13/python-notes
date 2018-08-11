# Working with Lists

# Looping through an entire list
- helpful to choose meaningful temp var names
```
magicians = ['Alice', 'Quinton', 'Margo', 'Elliot', 'Julia']

for magician in magicians:
  print(magician)
```
- you can use ".\n" for a newline

# Doing something after a For Loop
- anything not indented underneath the for loop is not looped
```
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")
```

# Avoiding indentation errors
- Python uses indentation to determine when one line of code is connected to the line above.
- Most common mistakes are forgetting to indent or indenting when its not needed

## 4-1 Pizzas
```
pizzas = ['Cheese', 'Veggie', 'Pepperoni']

for pizza in pizzas:
  print('i like ' + pizza + ' pizza')

print('Meh, pizza is okay')

```

## 4-2 Animals
```
animals = ['Dog', 'Cat', 'Ferret']

for animal in animals:
  print(animal + ' would make a great pet')

print('All these animals have fur')
```

## Numerical Lists
- Lists are ideal for storing sets of numbers, python provides a number of tools to help you work efficiently.

## range() function
- Range makes it easy to generate a series of numbers
- Range will only print 1 to 4, it starts counting at the 1st arg and stops at the 2nd arg provided. Since it stops, the output never contains that value
- You can generate a list from a range
```
for value in range(1,5)
  print(value)

numbers = list(range(1,6))
print(numbers)
```
- you can tell python to skip numbers
- the 1st and 2nd argument are the range. The 3rd tells python to add 2 until the range is met.
```
even = list(range(2,11,2))

squares = []
for val in range(1,11):
  squares.append(val**2)

print(squares)

```

# Simple Stats
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min(nums) -> 0
max(nums) -> 9
sum(nums) -> 45

```

# List Comprehensions
- List Comprehension allows you to generate this same list in just one line of code. list comprehension combines the 'for' loop and creation of new elements in just one line of code
```
squares = [value**2 for value in range(1,11)]
print(squares)

```

## 4-3 Counting to 20
```
twenty = [val for val in range(1,21)]
print(twenty)

```

## 4-4 One Million & 4-5 Sum a Million
```
aMilly = [val for val in range(1,1,000,000)]
print(aMilly)
print(sum(aMilly))

```

## 4-6 odds
```
odds = [odd for odd in range(1,21,2)]
print(odds)

```

## 4-7 Threes
```
threes = [three for three in range(3,31,3)]
print(threes)
```

## 4-8/9 Cubes
```
cubes = [value**3 for value in range(1,11)]
print(cubes)

```

# Working with Parts of a List

## Slicing a List
- to make a slice, you specify the index of the first and last elements you want to work with. Python stops one item before the 2nd index argument
- if you omit the first index in a slice, python starts at the beginning of the list
- you can also omit the 2nd index, and python will go through the entire list
```
players = ['charles', 'martina', 'michael', 'florence', 'eli']  

print(players[0:3]) -> ['charles', 'martina', 'michael']

print(players[:4]) -> ['charles', 'martina', 'michael', 'florence']

print(players[-3:])

```

## Looping through a Slice
- you can use slice in a for loop to work with a subset of elements in a list

```

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

```

## Copying a List
- To copy a list, you can make a slice that includes the entire original list, by omitting both the 1st and 2nd index
```
my_foods = ['yoghurt', 'chicken', 'veggies']
friends_foods = my_foods[:]

```

## 4-10 Slices
```
my_foods = ['yoghurt', 'chicken', 'veggies', 'fish', 'milk']
print("Here are the first three items in my fridge:")
for food in my_foods[:3]:
    print(food.title())

my_foods = ['yoghurt', 'chicken', 'veggies', 'fish', 'milk']
print("Here are the middle items in my fridge:")
for food in my_foods[1:4]:
    print(food.title())

my_foods = ['yoghurt', 'chicken', 'veggies', 'fish', 'milk']
print("Here are the last three items in my fridge:")
for food in my_foods[2:]:
    print(food.title())

```

## 4-11 Your Pizza, Nacho Pizza
```
pizzas = ['Cheese', 'Veggie', 'Pepperoni']
nacho_pizzas = pizzas[:]

pizzas.append('bbq chicken')
nacho_pizzas.append('anchovies')

for pizza in pizzas:
  print('i like these ' + pizza + ' pizza')

for nacho_pizza in nacho_pizzas:
  print('my friends like these ' + nacho_pizza + ' pizza')

print(pizzas)
print(nacho_pizzas)

```

## Tuples
- Tuples are immutable lists.
- A tuple looks like a list except you use paratheses instead of square brackets
- Once you define a tuple you can access items via the index
- You can't modify a Tuple but you can assign a new value to a variable thats holds a Tuple

```

dimensions = (200, 50) print("Original dimensions:")
for dimension in dimensions:
  print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
  for dimension in dimensions:
    print(dimension)

```

## 4-13
```
menu = ('steak', 'lobster', 'steamed veggies', 'mac n cheese', 'ice cream')

menu = ('steak','fish tacos','sushi','fries','burritos')

for items in menu:
  print(items)
```

# Styling Code
- four spaces per indentation
- line length less than 80 chars
- 72 chars per comment
