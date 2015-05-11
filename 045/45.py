def tri(n):
    return n * (n + 1) / 2

def pen(n):
    return n * (3 * n - 1) / 2

def hex(n):
    return n * (2 * n - 1)

n = 1
tris = []
pens = []
hexs = []

while True:
    t = tri(n)
    p = pen(n)
    h = hex(n)

    tris.append(t)
    pens.append(p)
    hexs.append(h)

    if n > 285 and t in pens and t in hexs:
        print(t)
        break
    
    n += 1
