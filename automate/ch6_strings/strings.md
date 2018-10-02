# Working with Strings
- Strings can begin and end with double quotes, just as they do with single quotes. One benefit of using double quotes is that the string can have a single quote character in it.
- An escape character lets you use characters that are otherwise impossible to put into a string. An escape character consists of a backslash (\) followed by the character you want to add to the string.
- You can place an **r** before the beginning quotation mark of a string to make it a raw string. **raw strings** completely ignore all escape characters and prints any backslash that appears in the string.
- A **multiline string** in Python begins and ends with either **three single quotes** or **three double quotes**. Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string.
- While the hash character (#) marks the beginning of a comment for the rest of the line, a multiline string is often used for comments that span multiple lines.
```
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')


Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob

```

## Indexing and Slicing Strings
- Strings use indexes and slices the same way lists do
- If you specify an index, you’ll get the character at that position in the string. If you specify a range from one index to another, the starting index is included and the ending index is not.
- Note that slicing a string does not modify the original string. You can capture a slice from one variable in a separate variable.

## The 'in' and 'not in' Operators with Strings
- The in and not in operators can be used with strings just like with list values.
- An expression with two strings joined using in or not in will evaluate to a Boolean True or False
- These expressions test whether the first string (the exact string, case sensitive) can be found within the second string.
```
'Hello' in 'Hello World' => True

```

## Useful String Methods - upper(), lower(), isupper(), and islower()
- upper() and lower() methods return a new string where all the letters in the original string have been converted. non-letter chars remain unchanged.
- These methods do not change the string itself but return new string values.
- You can call string methods on those returned string values as well. 'Hello'.upper().lower()

## isX String Method
- there are several string methods that have names beginning with the word **is**
- isalpha() returns True if the string consists only of letters and is not blank.
- isalnum() returns True if the string consists only of letters and numbers
and is not blank.
- isdecimal() returns True if the string consists only of numeric characters and is not blank.
- isspace() returns True if the string consists only of spaces, tabs, and new- lines and is not blank.
- istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
- Useful for things like input validation

## The startswith() and endswith() String Methods
- These two methods return 'True' if the string value key they are called on matches the string passed to the method.

## join() and split()
- The join() method is called on a string, gets passed a list of strings, and returns a string.
- **join()** is called on a string value and is passed a list value.
- **split()** is called on a string value and returns a list of strings.

## Justifying Text with rjust(), ljust(), and center()