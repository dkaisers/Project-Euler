sum = 0;
for n in open("numbers.txt", "r"):
    sum += int(n.strip())
print(sum)
