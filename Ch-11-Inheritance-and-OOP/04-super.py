class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

    def greet(self):
        print("Hello There!")

class Managaer(Employee):
    def __init__(self):
        print("Constructor of Manager")
    b = 2

class Programmer(Managaer):
    def __init__(self):
        super().greet()
        super().__init__()
        print("Constructor of Programmer")
    c = 3


p = Programmer()
print(p.a, p.b, p.c) # Prints the a,b and c attribute