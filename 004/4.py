def isPalindromic(n):
    s = str(n)
    return s == s[::-1]

digits = int(input('Number of digits for multiplicand: '))
x = y = int("9" * digits)
p = []
while y > 1:
    while x > 1:
        if isPalindromic(y * x):
            p.append(y * x)
        x -= 1
    x = int("9" * digits)
    y -= 1

print(max(p))
