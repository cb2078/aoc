g = [list(map(int, list(s))) for s in open('15.txt').read()[:-1].split('\n')]

w = len(g[0])
h = len(g)
G = [[0 for _ in range(w * 5)] for _ in range(h * 5)]
for dx in range(5):
    for dy in range(5):
        for x in range(w):
            for y in range(h):
                d = g[y][x] + dx + dy
                if d > 9:
                    d -= 9
                G[y + dy * h][x + dx * w] = d

def bfs(g):
    w = len(g[0])
    h = len(g)
    q = [(0, 0, 0)]
    D = [[10000 for _ in range(w)] for _ in range(h)]; D[0][0] = 0
    v = [[False for _ in range(w)] for _ in range(h)]
    while q:
        (r, x, y), *q = q
        if x == w - 1 and y == h - 1:
            return r
        if v[y][x]:
            continue
        v[y][x] = True
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if abs(dx) == abs(dy) or \
                        x + dx not in range(w) or\
                        y  + dy not in range(h):
                    continue
                d = r + g[y + dy][x + dx]
                if  d < D[y + dy][x + dx]:
                    D[y + dy][x + dx] = d
                    q.append((d, x + dx, y + dy))
        q.sort()

print(bfs(g))
print(bfs(G))

# print('\n'.join(''.join(map(str, r)) for r in G) + '\n')
