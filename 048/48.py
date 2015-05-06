import math

limit = int(input('Limit: '))

sum = 0
for n in range(1, limit + 1):
    sum += n ** n

print(str(sum)[-10:])
