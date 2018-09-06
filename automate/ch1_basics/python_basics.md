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
