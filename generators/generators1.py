def sqaures_until_n(n):
    for i in range(n + 1):
        yield i**2

n = int(input("Enter a number:"))
for i in sqaures_until_n(n):
    print(i)
