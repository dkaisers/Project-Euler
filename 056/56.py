limit = int(input('Limit = '))
sums = []
for a in range(0, limit):
    for b in range(0, limit):
        sums.append(sum([int(x) for x in str(a ** b)]))
print(max(sums))
