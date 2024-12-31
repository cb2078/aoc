p = [x.replace(': ', ' ').split() for x in open('25.txt').read().strip().split('\n')]
V = list({x for X in p for x in X})
n = len(V)
g = [[0] * n for _ in range(n)]
p = [[V.index(x) for x in X] for X in p]
for i, *J in p:
    for j in J:
        g[i][j] = g[j][i] = 1
pg = lambda: print('\n'.join(V[i] + ' | ' + ''.join('%2d '%g[i][j] for j in range(n)) for i in range(n)))

import random
def mincut(g):
    v = [*range(n)]
    p = [*range(n)]
    while len(v) > 2:
        i = random.choice(v)
        while True:
            j = random.choice(v)
            if j != i and g[i][j]:
                break
        for k in range(n):
            if k!=j and g[i][k]:
                g[k][j] += g[i][k]
                g[j][k] += g[i][k]
        for k in range(n):
            if g[i][k]:
                g[i][k] = g[k][i] = 0
        v.remove(i)
        p[i] = j
        # print(V[i], V[j])
        # print([V[i] for i in range(n) if i not in v])
        # pg()
        assert all(g[i][k]==0 for k in range(n))
    return g[v[0]][v[1]], p

from copy import deepcopy
while True:
    c, p = mincut(deepcopy(g))
    if c == 3:
        break
groups = {i:0 for i in range(n) if p[i] == i}
for i in p:
    while i not in groups:
        i = p[i]
    groups[i] += 1
x, y = groups.values()
print(x * y)
