limit = int(input('Limit: '))
sum = 0
numbers = list(range(1, limit))
primes = {}
for n in numbers:
    primes[n] = True
primes[1] = False

for k,v in primes.items():
    if v:
        sum += k
    else:
        continue
    toDelete = k + k
    while toDelete in primes:
        primes[toDelete] = False
        toDelete += k

print(sum)
