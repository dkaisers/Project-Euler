import math

def gauss(n):
    return (((n * n) + n) / 2)

def sumDivisibleBy(x, limit):
    return x * gauss(limit // x)

no1   = int(input('First number:   '))
no2   = int(input('Second number:  '))
limit = int(input('Limit:          ')) - 1

result = sumDivisibleBy(no1, limit) + sumDivisibleBy(no2, limit) - sumDivisibleBy(no1 * no2, limit)
print(result)
