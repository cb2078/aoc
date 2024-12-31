p = open('23.txt').read().strip().split('\n')
w, h = len(p[0]), len(p)
assert w == h
S, E = (0, 1), (-1 % w, -2 % w)
from collections import deque
q = deque([(0, S, set())])
r = -1
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    d, (i, j), v = q.popleft()
    if (i, j) == E:
        r = max(r, d)
    for k, (di, dj) in enumerate(dirs):
        if i + di not in range(w) or j + dj not in range(w):
            continue
        if p[i + di][j + dj] == '#':
            continue
        if p[i + di][j + dj] in  'v^><' and p[i + di][j + dj] != 'v^><'[k]:
            continue
        if (i + di, j + dj) in v:
            continue
        q.append((1 + d,
                  (i + di, j + dj),
                  v | {(i, j)}))
print(r) # p1

from collections import defaultdict
g = defaultdict(list)
q = deque([(0, S, S)])
v = set()
while q:
    d, (i, j), parent = q.popleft()
    v.add((parent, i, j))
    nxt = []
    c = 0
    for di, dj in dirs:
        if i + di not in range(w) or j + dj not in range(w):
            continue
        if p[i + di][j + dj] == '#':
            continue
        c += 1
        if (parent, i + di, j + dj) in v:
            continue
        nxt.append((i + di, j + dj))
    if d and (c > 2 or (i, j) in (S, E)):
        if (d, (i, j)) not in g[parent] and (i, j) != parent:
            g[parent].append((d, (i, j)))
        parent = i, j
        d = 0
    for i, j in nxt:
        q.append((d + 1, (i, j), parent))

# for k, v in g.items():
#     print(k, v, len(v))
# print()
# print(len(g))
# exit()

# for i in range(w):
#     print(''.join('O' if (i, j) in g else p[i][j] for j in range(w)))

q = deque([(0, S, [S])])
r = -1
while q:
    d, n, v = q.pop()
    if n == E:
        r = max(r, d)
    for dd, c in g[n]:
        if c in v:
            continue
        q.append((d + dd,
                  c,
                  v + [c]))
print(r) # p2
