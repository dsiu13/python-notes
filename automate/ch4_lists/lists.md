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

## List-like types: Strings and Tuples
- Lists aren’t the only data types that represent ordered sequences of values.
- Lists and strings are different in an important way.
- A list value is a mutable data type: It can have values added, removed, or changed. However, a string is immutable: It cannot be changed.
- Tuples use () instead of [], it is immutable and cannot have its value changed, appended, or removed.
- f you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses. ('hello',))
- A benefit of using tuples instead of lists is that, because they are immutable and their contents don’t change, Python can implement some optimizations that make code using tuples slightly faster than code using lists. Also its indicates this value is meant to never change to other looking at your code

## Converting Types with the list() and tuple() Functions
- the functions list() and tuple() will return list and tuple versions
of the values passed to them. tuple(['cat', 'dog', 5]) => ('cat', 'dog', 5)

## References
- When you assign a list to a variable, you are actually assigning a list reference to the variable. A reference is a value that points to some bit of data, and a list reference is a value that points to a list.

## Passing References
- When a function is called, the values of the arguments are copied to the parameter variables.
```
def eggs(someParameter):
    someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)

```

## copy() and deepcopy()
- You can use copy() to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.
- If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy(). The deepcopy() function will copy these inner lists as well.


# Summary
- Lists are useful data types since they allow you to write code that works on a modifiable number of values in a single variable.
- Lists are mutable, meaning that their contents can change. Tuples and strings, although list-like in some respects, are immutable and cannot be changed.
- A variable that contains a tuple or string value can be overwritten with a new tuple or string value, but this is not the same thing as modifying the existing value
- Variables do not store list values directly; they store references to lists. This is an important distinction when copying variables or passing lists as arguments in function calls.


# Practice Questions
1. What is []?
- A list
2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].) For the following three questions, let’s say spam contains the list ['a','b', 'c', 'd'].
3. What does spam[int(int('3' * 2) / 11)] evaluate to?
- 8
4. What does spam[-1] evaluate to?
- 'd'
5. What does spam[:2] evaluate to?
- 2,4,6

### For the following three questions, let’s say bacon contains the list
[3.14, 'cat', 11, 'cat', True].
6. What does bacon.index('cat') evaluate to?
- 1
7. What does bacon.append(99) make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True, 99]
8. What does bacon.remove('cat') make the list value in bacon look like?
[3.14, 'cat', 11, True, 99]
9. What are the operators for list concatenation and list replication?
10. What is the difference between the append() and insert() list methods?
11. What are two ways to remove values from a list?
12. Name a few ways that list values are similar to string values.
13. What is the difference between lists and tuples?
14. How do you type the tuple value that has just the integer value 42 in it?
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
17. What is the difference between copy.copy() and copy.deepcopy()?
