# Files and Exceptions

## Reading from a File
- Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle.

### Reading an Entire File
- the open() functions needs one argument, the file name you want to open
- read() method, reads the entire content of the file, and stores it as one long string
- use rstrip() to remove the empty string returned from read()
- Python’s rstrip() method removes, or strips, any whitespace characters from the right side of a string.
```
with open('pi.txt') as file_object:
  contents = file.object.read()
  print(contents.rstrip())
```

## File paths
- Need the file path, if you want a file that is not in the current root.
```
with open('text_files/filename.txt') as file_object:

```

## Reading Line by Line
- You can use a for loop on the file object to examine each line from a file one at a time
```
filename = 'pi.txt'
with open('pi.txt') as file_object:
  for line in file_object:
    print(line.rstrip())

```

## Making a List of Lines from a File
- using **with**, the file object returned by open() is only available inside the **with** that contains it.
- If you want to retain access to a file's contents outside the **with** block, you can store it in a list inside the block.
```
filename = 'pi.txt'
with open(filename) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line.rstrip())
```

## Working with a File's Content
- After you've read a files into memory, you can do whatever you want with it
- When Python reads from a text file, it is viewed as a string. For numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function.
```
filename = 'pi.txt'
with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

```

## Writing to an Empty File
- To write to a file call open() with a second argument telling Python that you want to write to a file.
- Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.
```
filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("i love programming")
  file_object.write("I love programming.\n")
```

## Writing Multiple Lines
- write() function doesn’t add any newlines to the text you write.
- use **/n** -> file_object.write("I love programming.\n")


## Exceptions
- Python uses special objects called **Exceptions** to manage errors
- Exceptions are handled with **try-except blocks**
- When you use try-except blocks, your programs will continue running even if things start to go wrong

## Using Exceptions to prevent crashes
```
print('enter a number for divions')
print("use 'q' to quit")

while True:
  first_num = input("\nFirst Number: ")
  if first_num == 'q'
    break
  second_num = input("\Second Number: ")
  if first_num == 'q'
    break
  ans = int(first_num) / int(second_num)
  print(ans)
```
- To hide our traceback err from user we should use a try-block
```
print('enter a number for divions')
print("use 'q' to quit")

while True:
  first_num = input("\nFirst Number: ")
  if first_num == 'q'
    break
  second_num = input("\Second Number: ")
  try:
    ans = int(first_num) / int(second_num)
  except ZeroDivisionError:
    print("can't divide by 0")
  else:
    print(ans)
```
