# Python Basics

## Operators
- Python takes order of operations into consideration
- Table below shows **precedence** from high to low.

| Operator  | Operation | Ex | Output
| :---------: | :-------------: | :---: | :---: |
| ** | Exponent | 2 ** 3 | 8 |
| % | Modulus/remainder | 22 % 8 | 6 |
| // | integer div/floored quotient | 22 // 8 | 2 |
| / | Division | 22 / 8 | 2.75 |
| * | multiplication | 3 * 5 | 15 |
| - | subtraction | 5 - 2 | 3 |
| + | addition | 2 + 2 | 4 |

## Data Types
- Integers are numbers. 1, 2, 3
- Floating-Points Numbers carry decimals referred to as "Floats"
- Strings, "Hello World", "Hello"
- Strings can be concatenated(joined together). "Alice" + "Bob" will output "AliceBob"
- Type conversion does not occur in Python for concatenation. 42 + "42" will throw an error. You must convert either the string or number to be the same data types.
- When the multiplication operator is used on a string, we get **String replication** "Alice" * 5 will output "AliceAliceAliceAliceAlice". The multiplication operator either takes one string and integers or two integers. It does not take float-point numbers

## Variables
- Store values in variables via an **assignment statement**. eggs = 2
- Variables are initialized the first time a value is stored in it.
- Variables can be overwritten
- Variables have naming restrictions, one word, letters/numbers/underscores only. It can't start with a number. No spaces.

## Boolean values
- True or False

## Comparison Operators
- These operators evaluate to True or False

| Operators | Meaning |
| :--------: | :--------: |
| == | Equal To |
| != | Not Equal to |
| less than | < |
| less than or equal to | <= |
| greater than | > |
| greater than or equal to | >= |

## Boolean Operators
- The **and** and **or** operators always take two Boolean values (or expressions), so they’re considered binary operators
- The **and** operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.

### The "AND" Operator's Truth Table

| Expression | Evaluates |
| :--------: | :--------: |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |


### The "OR" Operator's Truth Table

| Expression | Evaluates |
| :--------: | :--------: |
| True or True | True |
| True or False | True |
| False or True | True |
| False or False | False |

## The "NOT" Operator
- the **not** operator operates on only one Boolean value (or expression). The **not** operator simply evaluates to the opposite Boolean value.

### The "NOT" Operator's Truth Table

| Expression | Evaluates |
| :--------: | :--------: |
| Not True | False |
| Not False | True |

## Mixing Boolean and Comparison Operators
- Since the comparison operators evaluate to Boolean values, you can use them in expressions with the Boolean operators.
- The Boolean operators have an order of operations. After any math and comparison operators evaluate, Python evaluates the **not** operators first, then the **and** operators, and last the **or** operators.


# Flow Control

## "If" Statements
- The **if** statement is the most common flow control statement. An **if** statement’s clause will execute if the statement’s condition is True. The clause is skipped if the condition is False.
```
def nameCheck(name):
  if(name == "alice"):
    print("Hi, Alice")
```

## "Else" Statements
- An **if** clause can optionally be followed by an else statement.
- The else clause is executed only when the if statement’s condition is False.
```
def nameCheck(name):
  if(name == "alice"):
    print("Hi, Alice")
  else:
    print("Hello")
```

## "Elif" Statements
- While only one of the **if** or **else** cl auses will execute, you may have a case where you want one of many possible clauses to execute.
- The **elif** statement is an “else if” statement that always follows an if or another **elif** statement. It provides another condition that is checked only if any of the previous conditions were False.
```
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
```

### Rules for using "If", "Else", and "Elif"
- First, there is always exactly one if statement. Any elif statements you need should follow the if statement.
- Second, if you want to be sure that at least one clause is executed, close the structure with an else statement.


## While Loop Statements
- The code in a **while** clause will be executed as long as the while statement’s condition is True
- Unlike an **if statement** that ends once it finishes running, a while clause jumps back to the start of the while statement.
- While Loops, can create infinite loops if a condition to stop the loop isn't set.
```
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
```

## "break" Statements
- You can use a **Break** statement to end code early.

## "continue" Statements
- When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.

## for Loops and the Range() function
- Some functions can be called with multiple arguments separated by a comma
- The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument
- You can use negative numbers in steps
```
print('My name is ')
for i in range(5):
  print('Jimmy Five Times (' + str(i) + ')')

for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

```

# Importing Modules
- import module_name
- from file_name import A



# Ch1 Questions
1. What are the two values of the Boolean data type? How do you write them?
- True or False
2. What are the three Boolean operators?
- and, or, and not

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to)

### The "AND" Operator's Truth Table

| Expression | Evaluates |
| :--------: | :--------: |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |


### The "OR" Operator's Truth Table

| Expression | Evaluates |
| :--------: | :--------: |
| True or True | True |
| True or False | True |
| False or True | True |
| False or False | False |

## The "NOT" Operator

| Expression | Evaluates |
| :--------: | :--------: |
| Not True | False |
| Not False | True |


4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5) - False
not (5 > 4) - False
(5 > 4) or (3 == 5) - True
not ((5 > 4) or (3 == 5)) - False
(True and True) and (True == False) - False
(not False) or (not True) - True


5. What are the six comparison operators?
- less than, less than or equal, greater than, greater than or equal to, equal to, not equal to

6. What is the difference between the equal to operator and the
assignment operator?
- single equal sign for assignment, double equal sign for equal to operator

7. Explain what a condition is and where you would use one.
- Tell your code to run when a specific condition is met. You only want certain code to run when a user inputs a condition
- A condition is an expression used in a flow control statement that evalu- ates to a Boolean value.

8. Identify the three blocks in this code:
```
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
print('spam')

```

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
```
if spam == 1:
  print("Hello")
elif spam == 2:
  print("Howdy")
else:
  print("Greetings")
```

10. What can you press if your program is stuck in an infinite loop?
- ctrl + c

11. What is the difference between break and continue?
- Break stops your code.
- Continue restarts your code at the start.
- The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
- 1st example, gives you the end Range
- 2nd example, gives you the start and end range
- 3rd example, gives you start, end, and an increment value/step value.

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
```
for i in range(1,11):
    print(i)

i = 1
while i <= 10:
  print(i)
  i += 1

```

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
- spam.bacon()
