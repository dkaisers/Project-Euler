limit = int(input('Limit: '))

def sameReverse(s):
    return s == s[::-1]

def toBinaryString(n):
    return "{0:b}".format(n)

sum = 0
for n in range(1, limit):
    if sameReverse(str(n)) and sameReverse(toBinaryString(n)):
        sum += n

print(sum)
