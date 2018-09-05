import unittest
from employee import Employee

class TestAnonSurvey(unittest.TestCase):

    def setUp(self):
        self.new_employee = Employee("Bob", "Smith", 100000)

    def test_give_raise(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        self.new_employee.give_raise(20000)
        self.assertEqual(self.new_employee.annual_salary, 120000)

unittest.main()
