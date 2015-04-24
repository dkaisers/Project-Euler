def smallestPrimeDividedBy(x):
    i = 2
    while True:
        if x % i == 0:
            return i
        i+=1

no = int(input('Number: '))

product = 1
primes = []

while no > 1:
    d = smallestPrimeDividedBy(no)
    no = no / d
    primes.append(d)

print(max(primes))
