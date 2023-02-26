import math

def Trap_Area(h, a, b):
    Area = math.pow(2, -1) * (a + b) * h
    return Area

h = float(input("Enter a heigh:"))
a = float(input("Enter a first base:"))
b = float(input("Enter a second base:"))

print("Trapezoidal Area is:", Trap_Area(h, a, b))