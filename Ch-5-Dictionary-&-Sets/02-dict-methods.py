marks = {
    "Rohit" : 45,
    "Virat" : 18,
    "Jassi" : 93
}

# items
print(marks.items())

# keys
print(marks.keys())

# values
print(marks.values())

# update
marks.update({"Rohit" : 264, "Lokesh" :65})
print(marks)

# get
print(marks.get("Rohit")) #prints none
print(marks["Harry"]) # returns error

