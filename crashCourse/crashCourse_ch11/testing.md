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
- Testing a class is similar to testing a function—much of your work involves testing the behavior of the methods in the class.

| Method  | Use |
| ------------- | ------------- |
| assertEqual(a,b) | verify that a == b |
| assertNotEqual(a,b) | verify that a != b |
| assertTrue(x) | verify that x is True |
| assertFalse(x) | verify that x is False |
| assertIn(item, list) | verify that item is in List |
| assertNotIn(item, list) | verify that item is not in list |

## Setup Method
- setUp() method allows you to create these objects once and then use them in each of your test methods.
- Python runs the setUp() method before running each method starting with test_. Any objects created in the setUp() method are then available in each test method you write.
```
class TestAnonSurvey(unittest.TestCase):

    def setUp(self):
        question = "what language did you first learn to code in?"
        self.my_survey = anonSurvey(question)
        self.responses = ["JavaScript", "Python", "Ruby"]

    def test_store_single_res(self):
        self.my_survey.store_res(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_multi_res(self):
        for response in self.responses:
            self.my_survey.store_res(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

```
