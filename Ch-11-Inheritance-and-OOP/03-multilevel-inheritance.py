class Employee:
    a = 1

class Managaer(Employee):
    b = 2

class Programmer(Managaer):
    c = 3

e = Employee()
print(e.a) # Prints the a attribute
# print(e.b) Shows an error as there is no b attribute in Employee class
# print(e.c) Shows an error as there is no c attribute in Employee class

m = Managaer()
print(m.a, m.b) # Prints the a and b attribute
# print(m.c) Shows an error as there is no c attribute in Manager class

p = Programmer()
print(p.a, p.b, p.c) # Prints the a,b and c attribute