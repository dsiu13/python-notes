class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)
        self.attributes = []

    def give_raise(self):
        self.annual_salary += 5000
