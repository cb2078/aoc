f=[x.split() for x in open('16a.txt').read().strip().split('\n')]
v=[x[1] for x in f];aa=v.index('AA')
n=len(v)
g=[[v.index(n.replace(',','')) for n in x[9:]] for x in f]
r=[int(''.join(filter(str.isdigit,x[4]))) for x in f]

d=[[0 if i==j else 1 if j in g[i] else float('inf')
    for j in range(n)] for i in range(n)]
from itertools import product
for k,i,j in product(range(n),repeat=3):
    d[i][j]=min(d[i][j],d[i][k]+d[k][j])

def dfs(u,p,t,o):
    y = 0
    if o > 0:
        y = max(y, dfs(aa, p | 1<<u, 26, o - 1))
    if t <= 0:
        return 0
    x = r[u] * t
    for c in range(n):
        if 1<<c & p or c == u:
            continue
        if not r[c]:
            continue
        y = max(y, dfs(c, p | 1<<u, t - 1 - d[u][c], o))
    return x + y

print(dfs(aa, 0, 30, 0)) # 1
print(dfs(aa, 0, 26, 1)) # 2
