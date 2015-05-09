import sys

file = open("matrix.txt", "r")
mats = []

line = file.readline()
while line != "":
    mats.append([int(x) for x in line.rstrip().split(',')])
    line = file.readline()

h = len(mats)
w = len(mats[0])

alst = {}

for i in range(0, h):
    for j in range(0, w):
            cons = {}
            if i > 0:
                cons[(i-1,j)] = mats[i-1][j]
            if i < h-1:
                cons[(i+1,j)] = mats[i+1][j]
            if j > 0:
                cons[(i,j-1)] = mats[i][j-1]
            if j < w-1:
                cons[(i,j+1)] = mats[i][j+1]
            alst[(i,j)] = cons

dist = {}
for i in range(0, h):
    for j in range(0, w):
        dist[(i,j)] = sys.maxsize
dist[(0,0)] = mats[0][0]

toVisit = list(dist.keys())
while len(toVisit) > 0:
    toCheck = {k:dist[k] for k in toVisit}
    key = min(toCheck, key=toCheck.get)
    val = dist[key]
    for t in alst[key]:
        dist[t] = min(dist[t], val + alst[key][t])
    toVisit.remove(key)

print(dist[(h-1,w-1)])
