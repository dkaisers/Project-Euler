import math

x = int(input('x = '))
terms = set()

for a in range(2, x + 1):
    for b in range(2, x + 1):
        terms.add(math.pow(a, b))

print(len(terms))
