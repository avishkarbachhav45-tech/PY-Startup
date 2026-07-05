from functools import reduce

a = [1,2,35,435,54,45,65,84,4]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))