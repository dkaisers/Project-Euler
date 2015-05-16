file = open("grid.txt", "r")
nums = []
maxProduct = 0

line = file.readline()
while line != "":
    nums.append([int(x) for x in line.rstrip().split(" ")])
    line = file.readline()

for i in range(0, len(nums)):
    for j in range(0, len(nums[i]) - 4):
        p = nums[i][j] * nums[i][j+1] * nums[i][j+2] * nums[i][j+3]
        maxProduct = max(maxProduct, p)

for i in range(0, len(nums) - 4):
    for j in range(0, len(nums[i])):
        p = nums[i][j] * nums[i+1][j] * nums[i+2][j] * nums[i+3][j]
        maxProduct = max(maxProduct, p)

for i in range(0, len(nums) - 4):
    for j in range(0, len(nums[i]) - 4):
        p = nums[i][j] * nums[i+1][j+1] * nums[i+2][j+2] * nums[i+3][j+3]
        maxProduct = max(maxProduct, p)

for i in range(3, len(nums)):
    for j in range(0, len(nums[i]) - 4):
        p = nums[i][j] * nums[i-1][j+1] * nums[i-2][j+2] * nums[i-3][j+3]
        maxProduct = max(maxProduct, p)

print(maxProduct)
