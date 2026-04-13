class Employee:
    # name = "Rohit"
    language = "py"
    salary = 4500000


rohit = Employee()
rohit.name = "Rohit"
print(rohit.name, rohit.salary, rohit.language)


rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohit.salary, rohit.language)

# Here name is object attribute and salary are class attributes 
# they directly belong to the class