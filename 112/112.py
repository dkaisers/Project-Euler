def isBouncy(n):
    s = str(n)
    return s != "".join(sorted(s)) and s != "".join(sorted(s, reverse=True))

b = 0
i = 1
while b / i != 0.99:
    i += 1
    if isBouncy(i):
        b += 1

print(i)
