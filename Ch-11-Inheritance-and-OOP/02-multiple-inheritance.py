class Employee:
    company = "Google"
    name = "Default"
    salary = 25000
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Coder():
    language = "Python"
    def printLanguages(self):
        print(f"Out of all languages your language is: {self.language}")



class Programmer(Employee,Coder):
    company = "Google Cloud"

    def showLang(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLang()