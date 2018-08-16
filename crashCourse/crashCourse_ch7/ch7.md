# User Input and While Loops
- input() waits for a user to input some text
- once received Python stores the input into a variable
- input() takes one arg: the prompt
- input() stores info as a string. You can convert to an integer using int()

## Modulo
- divides a number by another and returns the remainder
- modulo doesn't tell you how many times one number fits into another

## Even or Odd
```
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

```

## 7-1 Rental Car
```
prompt = "what kind of car would you like?"
car = input(prompt)

```
## 7-2 Restaurant Seating
```
prompt = "how many?"
seats = input(prompt)
seats = int(seats)

if seats > 8:
  print('Nope')
else:
  print('Your table is ready')
```

## 7-3 Multiple of Tens
```
prompt = "enter a number?"
x = input(prompt)
x = int(x)

def ten(x):
  if x % 10 == 0:
    print('Multiple of ten')
  else:
    print('nope')
```

## While Loop
- a 'for' loop takes a collection of items and executes a block of code once for each item.
- a 'while' loop runs as along as a certain condition is True
```
num = 1
while num <= 5:
  print(num)
  num += 1

```

## Letting the User choose when to Quit
- we can define a 'quit' value and then keep the program running as long as
the user has not entered the quit value
```
prompt = "type something"
prompt += "type 'quit' to exit anytime "

msg = ""

while msg != 'quit'
  msg = input(prompt)
  print(msg)
```

## Using a Flag
- For a program that should only run as long as many conditions are true you can define a 'flag'
- the 'flag' variable  is a signal to the program, you can set the 'flag' value to true or false to stop or start code.
```
active = True
prompt = "type something"
prompt += "type 'quit' to exit anytime "

while active:
  msg = input(prompt)

  if msg == 'quit':
    active = False
  else:
    print(msg)
```

## Break to exit a loop
- to exit a while loop without running any more code in the loop, you can use a 'break' statement.
- you can use 'break' in 'for' loops as well

```
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
city = input(prompt)
if city == 'quit':
  break
else:
  print("I'd love to go to " + city.title() + "!")

```

## Using continue in a Loop
- You can use 'continue' to return to the beginning of the loop based on a conditional test
```
num = 0
while num < 10:
  num += 1
  if num % 2 == 0:
    continue

print(num)

```
## Avoiding infinite loops
- test your loop, to make sure it stops when you expect it to.
- Important if your stop condition is subtle

## 7-4 Pizza Toppings
