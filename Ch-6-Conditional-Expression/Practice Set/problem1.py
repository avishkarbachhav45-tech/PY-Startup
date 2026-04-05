a1 = int(input("Enter no 1: "))
a2 = int(input("Enter no 2: "))
a3 = int(input("Enter no 3: "))
a4 = int(input("Enter no 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Number a1 is greater among all", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Number a2 is greater among all", a2)
if(a3>a1 and a3>a2 and a3>a4):
    print("Number a3 is greater among all", a3)
else:
    print("Number a4 is greater among all")