import math

def gauss(x):
    return (((x * x) + x) / 2)

def pyramid(x):
    return (x * (x + 1) * (x + x + 1)) / 6

limit = int(input('Limit: '))

pyr = pyramid(limit)
gau = gauss(limit)

print(gau * gau - pyr)
