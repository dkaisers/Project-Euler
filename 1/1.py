no1   = int(input('First number:   '))
no2   = int(input('Second number:  '))
limit = int(input('Limit:          '))

sum = 0;
for x in range(1, limit):
    if (x % no1) == 0 or (x % no2) == 0:
        sum += x;

print(sum)
