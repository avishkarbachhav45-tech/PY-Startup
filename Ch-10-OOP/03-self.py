class Employee:
    language = "Python"
    salary = 4500000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    def greet(self):
        print(f"Good Morning {self.name}")


rohit = Employee()
rohit.language = "JavaScript"
rohit.name = "Rohit"

rohit.greet()
rohit.getInfo()

