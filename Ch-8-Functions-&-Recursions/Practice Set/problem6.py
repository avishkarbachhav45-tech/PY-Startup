def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

cms = inch_to_cms(n)

print(f"The corresponding value in cms is {cms}")