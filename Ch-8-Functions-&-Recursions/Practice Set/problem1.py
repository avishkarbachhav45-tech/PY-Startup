def greatest(a, b ,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = 3
b = 29
c = 9

print(greatest(a, b, c))