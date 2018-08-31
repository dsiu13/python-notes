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

## Failing Tests
