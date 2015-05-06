nums = []

file = open("matrix.txt", "r")
line = file.readline()

while line != '':
    nums.append([int(x) for x in line.rstrip().split(',')])
    line = file.readline()

size = len(nums)

for i in range(1, size):
    nums[i][0] += nums[i-1][0]
    nums[0][i] += nums[0][i-1]

for i in range(1, size):
    for j in range(1, size):
        nums[i][j] += min(nums[i-1][j], nums[i][j-1])

print(nums[size-1][size-1])
