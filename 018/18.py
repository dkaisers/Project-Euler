lines = [list(map(int, s.rsplit())) for s in list(open("numbers.txt", "r"))]

for y in range(1, len(lines)):
    for x in range(0, len(lines[y])):
        l = lines[y-1][x-1] if x > 0 else 0
        r = lines[y-1][x] if x < len(lines[y-1]) else 0
        lines[y][x] += max(l,r)

print(max(lines[-1]))
