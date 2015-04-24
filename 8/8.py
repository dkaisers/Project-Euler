import operator
import functools

number = str(open("number.txt", "r").read())
numbers = []
for i in range(0, len(number)-13):
    n = [int(i) for i in number[i:i+13]]
    numbers.append(functools.reduce(operator.mul, n, 1))

print(max(numbers))
