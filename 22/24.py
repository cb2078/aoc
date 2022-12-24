p = open('24.txt').read().strip().split('\n')
w, h = len(p[0]), len(p)
c = 'v^<>'
d = ((1, 0), (-1, 0), (0, -1), (0, 1), (0, 0))
b = [(0, 1), (h - 1, w - 2)]
inside = lambda i, j: (i, j) in b or (i in range(1, h - 1) and j in range(1, w - 1))

g = {}
for i in range(h):
    for j in range(w):
        if p[i][j] not in '.#':
            g[i, j] = [d[c.index(p[i][j])]]

pp = lambda g, x = None: '\n'.join(''.join('E' if x and (i, j) == x else \
                                           '#' if not inside(i, j) else \
                                           '.' if (i, j) not in g else \
                                           c[d.index(g[i, j][0])] if 1 == len(g[i, j]) else \
                                           str(len(g[i, j])) for j in range(w)) for i in range(h)) + '\n'

from collections import defaultdict
def step(g):
    gg = defaultdict(list)
    fit = lambda i, imax: (i - 1) % (imax - 2) + 1
    for i, j in g:
        for di, dj in g[i, j]:
            gg[fit(i + di, h), fit(j + dj, w)] += [(di, dj)]
    return gg

dp = [g]
def solve(n0, a, b):
    q = [(n0, *a)] # nij
    v = set() # nij
    while q:
        (n, i, j), *q = q
        if (i, j) == b:
            return n
        if n == len(dp):
            dp.append(step(dp[-1]))
        if (n, i, j) in v or not inside(i, j) or (i, j) in dp[n]:
            continue
        v.add((n, i, j))
        for di, dj in d:
            q += [(n + 1, i + di, j + dj)]

print(n := solve(0, b[0], b[1])) # 1
n = solve(n, b[1], b[0])
print(solve(n, b[0], b[1])) # 2
