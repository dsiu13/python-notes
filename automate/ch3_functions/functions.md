# Functions
- def defines a Function.
- arguments can be passed to functions
```
def Hello(name)
  print("hello " + name)
```

# Return Values and return Statements
- You can specify what the return value should be with a return statement
- Expressions are composed of values and operators. A function call can be used in an expression because it evaluates to its return value.

# None Value
- **None** represents the absence of a value.
- **None** has the data type of **NoneType**. Similar to Null, Nil, or undefined
- Python adds return None to the end of any function definition with no return statement.
- A return statement with no value assigned will have **None** returned.

# Keyword Arguments
- keyword arguments are identified by the keyword put before them in the function call. Keyword arguments are often used for optional parameters.


# Scope
- Parameters and variables that are assigned in a called function exist in that function’s **local scope**. This is known as a local variable
- Variables assigned outside of all functions exist in the **global scope**. This is known as a global variable
- A variable is one or the other, it cannot be both local and global.
- Scope is a container for variables, when a scope is destroyed all values stored within it are forgotten.
- There is only one global scope and it starts when a program begins and ends when it is terminated.
- A local scope is created whenever a function is called. Info stored will not be remembered from the previous function call.
- You can reuse variable names if they exist within different scopes.
- Local variables are not accessible within the global scope. Local variables also cannot be used outside of their local scope.
- Local variables can make use of variables in the global scope.

# 'Global' Statement
- If you need to modify a global variable from within a function, use the global statement.


# Exception Handling
- Errors can be handled with try and except statements.
```
def spam(div)
  try:
    return 42/div
  except ZeroDivisionError:
    print("Invalid Argument")
```

# Summary
- Functions are a way to compartmentalize code into groups.
- Variables within function calls won't interfere with other variables.
- Easier to debug if you know a function is failing.

# Practice Questions
1. Why are functions advantageous to have in your programs?
- Organize your code, prevent variables from interfering with one another, easier to debug, cleaner code.
2. When does the code in a function execute: when the function is defined or when the function is called?
- When its called.
3. What statement creates a function?
- def function_name
4. What is the difference between a function and a function call?
- A function is a code container. The call invokes the function and tells it to run.
5. How many global scopes are there in a Python program? How many local scopes?
- One global. One local per function instance
6. What happens to variables in a local scope when the function call returns?
- They are forgotten.
7. What is a return value? Can a return value be part of an expression?
- You can specify what the return value should be with a return statement. Yes they can be.
8. If a function does not have a return statement, what is the return value of a call to that function?
- None
9. How can you force a variable in a function to refer to the global variable?
- Call the variable, and don't create an instance of the variable with the same name in the local scope
10. What is the data type of None?
- NoneType
11. What does the import areallyourpetsnamederic statement do?
- Imports a library or a file/class/function/etc...
12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
```
from spam import bacon
spam.bacon()

```
13. How can you prevent a program from crashing when it gets an error?
- Try/Except Blocks
14. What goes in the try clause? What goes in the except clause?
- Try - the code you want to run. Except - error message.
