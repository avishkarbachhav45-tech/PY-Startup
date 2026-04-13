class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Rohit", 450000, 423303)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 120000, 423303)
print(r.name, r.salary, r.pin, r.company)