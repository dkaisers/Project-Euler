import math

def a(t):
    return math.pow(t[0], 2) - math.pow(t[1], 2)

def b(t):
    return 2 * t[0] * t[1]

def c(t):
    return math.pow(t[0], 2) + math.pow(t[1], 2)

def tupleSum(t):
    return a(t) + b(t) + c(t)

def branch(t):
    branches = []
    branches.append((2 * t[0] - t[1], t[0]))
    branches.append((2 * t[0] + t[1], t[0]))
    branches.append((t[0] + 2 * t[1], t[1]))
    return branches

tuples = [(2, 1), (3, 1)]

for t in tuples:
    if 1000 % tupleSum(t) == 0:
        m = 1000 / tupleSum(t)
        print(a(t) * b(t) * c(t) * math.pow(m, 3))
        break

    tuples += branch(t)
