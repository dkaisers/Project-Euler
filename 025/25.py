def fib(n):
    a = 0
    b = 1
    fib = 1
    i = 1
    while len(str(fib)) < n:
        fib = a + b
        a = b
        b = fib
        i += 1
    return i

n = int(input('Number of digits in Fibonacci number = '))
print(fib(n))
