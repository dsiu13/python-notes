# Chapter 11 Testing

## Testing a Function / Unit Test and Test Cases
- the module **unittest** provides tools for Testing
- **unit test** verifies that **one specific** aspect of a function’s behavior is correct.
- a **test case** is a collection of unit tests that together prove that a function works as intended within a range of situations you expect
-  A test case with **full coverage** includes a full range of unit tests covering all the possible ways you can use a function.


## A Passing Test
- Import **unittest** and the function you want to test
```
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

```

## Testing a Class
- Python provides a number of assert methods in the unittest.TestCase class.

| Method  | Use |
| ------------- | ------------- |
| assertEqual(a,b) | verify that a == b |
| assertNotEqual(a,b) | verify that a != b |
| assertTrue(x) | verify that x is True |
| assertFalse(x) | verify that x is False |
| assertIn(item, list) | verify that item is in List |
| assertNotIn(item, list) | verify that item is not in list |



| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
