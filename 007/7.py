import math

nth = int(input('nth prime for n = '))

primes = [2]
no = 3

while len(primes) < nth:
    add = True
    sqrt = math.floor(math.sqrt(no))
    for div in primes:
        if div > sqrt:
            break
        if no % div == 0:
            add = False
    if add:
        primes.append(no)
    no += 2

print(primes[nth - 1])
