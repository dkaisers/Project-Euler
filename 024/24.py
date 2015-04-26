import itertools

perms = itertools.permutations(range(10))
sorted = list(map(lambda t: "".join([str(n) for n in t]), perms))
print(sorted[999999])
