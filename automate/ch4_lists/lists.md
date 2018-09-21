# Lists
- A **list** is a value that contains multiple values in an ordered sequence.
- The term **list value** refers to the list itself (which is a value that can be stored in a variable or passed to a function like any other value), not the values inside the list. list value: ['cat', 'bat', 'rat', 'elephant'].
- You can grab individual list values via bracket notation and the index position. list_name[0]
- Lists can also accept negative values. list_name[-2] would grab the second to last index item. while [-1] refers to the last item in the list

## Sublists with Slices
- A **slice** is typed between between square brackets and can grab multiple values. list_name[1:4]
- the 1st value is the start and the 2nd value is the end. The slice will not include the 2nd value.
- the slice will evaluate to a new list value.
- You can leave the 1st or 2nd value blank in a slice. If the 1st position is empty **0** will be used. If the 2nd position is empty, it will use the length of the list

## Getting List Length
- list_name = ["Hello", "Howdy", "Hi", "Hey", "Sup"]
- len(list_name) = 5

## Changing Values via index
- You can also use an index of a list to change the value at that index.
- list_name = ["Hello", "Howdy", "Hi", "Hey", "Sup"]
- list_name[0] = "Hello World"

## List concatenation and List replication
- the **+** operator can join two lists to create a new list value.
- the multiply operator can replicate the list.
- [1, 2, 3] + ['A', 'B', 'C'] => [1, 2, 3, 'A', 'B', 'C']
- ['X', 'Y', 'Z'] * 3 => ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

## Removing Values via Del
- The del statement will delete values at an index in a list. All of the values
in the list after the deleted value will be moved up one index.
- spam = ['cat', 'bat', 'rat', 'elephant']
- del spam[2] => spam = ['cat', 'bat', 'elephant']

## Loops with Lists
```
for i in range(4):
    print(i)
```

# "in" and "not in" operator
- You can determine whether a value is or isn’t in a list with the in and not in operators.
- **in** and **not in** are used in expressions and connect two values: a value to look for in a list and the list where it may be found.
- 'howdy' in ['hello', 'hi', 'howdy', 'heyas'] => true

## Multiple assignment trick
- The number of variables and the length of the list must be exactly equal
```
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

cat = ['fat', 'black', 'loud']
size, color, disposition = cat
```

## Methods
- A method is the same thing as a function, except it is “called on” a value.
- The method part comes after the value, separated by a period.
- spam = ['hello', 'hi', 'howdy', 'heyas'] => spam.index('hello') => 0
- You can add values with append() and insert(), and you can remove with remove()
- sort() method, to sort a list
