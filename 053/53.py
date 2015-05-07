import math

limit = int(input('n = '))

facs = {}
def fac(n):
    if n not in facs:
        facs[n] = math.factorial(n)
    return facs[n]

def nOfR(n, r):
    return fac(n) / (fac(r) * fac(n - r))

count = 0
for n in range(1, limit + 1):
    for r in range(1, n + 1):
        if nOfR(n, r) > 1000000:
            count += 1

print(count)
