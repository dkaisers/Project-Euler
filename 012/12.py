from itertools import groupby
from functools import reduce
from operator import mul

min = int(input('Minimum number of divisors: '))

num = 1
tri = 0

while True:
    tri += num
    num += 1

    div = 2
    pri = []
    rem = tri
    while div <= rem:
        if rem % div == 0:
            pri.append(div)
            rem /= div
        else:
            div += 1
   
    cnt = reduce(mul, [len(list(grp)) + 1 for key, grp in groupby(pri)], 1)
    if cnt > min:
        break

print(tri)
