def fib(x,y,limit):
    z = x + y
    if z >= limit:
        return 0
    r = z if (z % 2) == 0 else 0
    return r + fib(y,z,limit)

limit = int(input('Limit: '))
print(fib(0,1,limit))
