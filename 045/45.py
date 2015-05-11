import math

def tri(n):
    return n * (n + 1) / 2

def isPen(n):
    return ((math.sqrt(24 * n + 1) + 1) / 6) % 1 == 0

def isHex(n):
    return ((math.sqrt(8 * n + 1) + 1) / 4) % 1 == 0

i = 286
while True:
    t = tri(i)
    if isPen(t) and isHex(t):
        print(t)
        break
    i += 1
