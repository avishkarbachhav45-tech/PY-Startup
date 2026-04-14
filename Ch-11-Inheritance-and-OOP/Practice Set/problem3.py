class Employee():
    salary = 2500
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1 )* 100

        
e = Employee()
e.salaryAfterIncrement = 3505

print(e.increment)