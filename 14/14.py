import operator

def isEven(x):
    return x % 2 == 0

def calc(x):
    if isEven(x):
        return x / 2
    else:
        return x * 3 + 1

limit = int(input('Limit: '))

start = limit - 1
terms = {1:1}

while start > 2:
    no = start
    termlist = [no]

    while no > 1:
        if no not in terms:
            next = calc(no)
            termlist.append(next)
            no = next
        else:
            break

    count = terms[no]
    for term in termlist[::-1]:
        terms[term] = count
        count += 1

    start -= 1

print(sorted(terms.items(), key=operator.itemgetter(1))[-1])
