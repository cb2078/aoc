with open('9.txt') as f:
    p = [[int(c) for c in s] for s in f.read()[:-1].split('\n')]
    w, h = len(p[0]), len(p)

res = 0
lp = []
for x in range(w):
    for y in range(h):
        b = True
        if x > 0:
            b &= p[y][x] < p[y][x - 1] 
        if x < w - 1:
            b &= p[y][x] < p[y][x + 1]
        if y > 0:
            b &= p[y][x] < p[y - 1][x]
        if y < h - 1:
            b &= p[y][x] < p[y + 1][x]
        if b:
            res += p[y][x] + 1
            lp.append((x, y))
print(res)

def search(x, y):
    found = [[0 for _ in range(w)] for _ in range(h)]
    def iter(x, y):
        if (x not in range(w) or
            y not in range(h) or
            p[y][x] == 9 or
            found[y][x] == 1):
            return 0
        found[y][x] = 1
        return 1 + (iter(x, y + 1) +
                    iter(x, y - 1) + 
                    iter(x + 1, y) +
                    iter(x - 1, y))
    return iter(x, y)

b = [search(x[0], x[1]) for x in lp]
import math
res = math.prod(sorted(b)[-3:])
print(res)
