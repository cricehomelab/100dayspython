class Person:
    def __init__(self, sal):
          self.salary = sal
    def inc_salary(self):
          self.salary += 100
    def print_sal(self):
          print(f"The salary of the person is {self.salary}")


my_person = Person(2000)
my_person.inc_salary()
my_person.print_sal()