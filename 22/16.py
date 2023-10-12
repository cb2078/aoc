f=[x.split() for x in open('16.txt').read().strip().split('\n')]
v=[x[1] for x in f];aa=v.index('AA')
n=len(v)
g=[[v.index(n.replace(',','')) for n in x[9:]] for x in f]
r=[int(''.join(filter(str.isdigit,x[4]))) for x in f]

d=[[1 if j in g[i] else float('inf') for j in range(n)] for i in range(n)]
from itertools import product
for k,i,j in product(range(n),repeat=3):
    d[i][j]=min(d[i][j],d[i][k]+d[k][j])

def dfs(u,t,p=0,x=0):
    p |= 1 << u
    dp[p] = max(dp.get(p, 0), x)
    for c in range(n):
        T = t - 1 - d[u][c]
        if 1 << c & p or r[c] == 0 or T <= 0:
            continue
        dfs(c, T, p, x + r[c] * T)

dp = {}; dfs(aa, 30); print(max(dp.values()))
dp = {}; dfs(aa, 26); print(max(dp[x] + dp[y] for x in dp for y in dp if x & y == 1 << aa))
