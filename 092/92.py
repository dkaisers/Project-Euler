def square(n):
    return n ** 2

def chain(n):
    return sum([square(int(x)) for x in str(n)])

limit = int(input('Limit = '))
maxChain = 81 * len(str(limit))

chains = dict.fromkeys(list(range(1, maxChain)))
for i in chains:
    x = i
    while True:
        if x == 1:
            chains[i] = False
            break
        if x == 89:
            chains[i] = True
            break
        x = chain(x)

count = 0
for i in range(1, limit):
    if chains[chain(i)]:
        count += 1

print(count)
