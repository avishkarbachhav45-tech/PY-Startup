class Employee:
    language = "Python"
    salary = 4500000

    def __init__(self, name, salary, language):
        self.name= name
        self.salary = salary
        self.language = language
        print("I am creating an object")
        

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    def greet(self):
        print(f"Good Morning {self.name}")


rohit = Employee("Rohit", 5000000, "JavaScript")

# rohit.greet()

print(rohit.name, rohit.salary, rohit.language)