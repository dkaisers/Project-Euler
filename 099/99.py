import math

file = open("numbers.txt", "r")

line = file.readline()
maxv = 0
maxl = 0
curl = 0

while line != "":
    nums = [int(x) for x in line.rstrip().split(",")]
    curl += 1
    nval = nums[1] * math.log(nums[0])
    
    if nval > maxv:
        maxv = nval
        maxl = curl

    line = file.readline()

print(maxl)
