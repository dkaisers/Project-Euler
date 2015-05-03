import math

n = int(input('Digit sum for 2^n for n = '))
x = int(math.pow(2, n))
sum = 0
for c in str(x):
    sum += int(c)
print(sum)
