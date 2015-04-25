import math

def sieve(n):
    primes = list(range(2, n+1))

    i = 0
    while i < len(primes):
        no = primes[i]
        m = 2
        while (no * m) <= max(primes):
            if primes.count(no * m) > 0:
                primes.remove(no * m)
            m+=1

        i+=1

    return primes

def maxPower(n, limit):
    i = 1
    while math.pow(n, i + 1) <= limit:
        i += 1
    return i

limit = int(input('Limit: '))

primes = sieve(limit)
s = 1 
for x in primes:
    print(math.pow(x, maxPower(x, limit)))
    s *= math.pow(x, maxPower(x, limit))

print(s)
