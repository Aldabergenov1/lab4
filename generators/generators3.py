def iter_until_n(n):
    for i in range(n + 1):
        if(i%3 == 0 and i%4 == 0):
            yield i
        
n = int(input("Enter a number:"))
for i in iter(iter_until_n(n)):
    print(i)