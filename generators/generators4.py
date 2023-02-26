def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input("Enter a lowerbound:"))
b = int(input("Enter a upperbound:"))

for i in squares(a, b):
    print(i)