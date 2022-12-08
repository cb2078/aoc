f=open('08.txt').read().strip().split('\n')
g=[list(map(int,x)) for x in f]
w,h=len(g[0]),len(g)

def vis(i,j):
    return (all(g[i][j] > g[k][j] for k in range(i)) or
            all(g[i][j] > g[i][k] for k in range(j)) or
            all(g[i][j] > g[i][k] for k in range(j + 1, w)) or
            all(g[i][j] > g[k][j] for k in range(i + 1, h)))

for r in [[(g[i][j],vis(i,j)) for j in range(w)] for i in range(h)]:print(r)
print(sum(vis(i, j) for i in range(h) for j in range(w))) # 1

from itertools import accumulate
from functools import reduce
import operator

def score(i,j):
    scans = ([g[i][j] > g[k][j] for k in range(i)[::-1]],
             [g[i][j] > g[i][k] for k in range(j)[::-1]],
             [g[i][j] > g[i][k] for k in range(j + 1, h)],
             [g[i][j] > g[k][j] for k in range(i + 1, h)])
    scans = [(not all(scan)) + sum(accumulate(scan, operator.and_)) for scan in scans]
    return scans

for r in [[(g[i][j],score(i,j)) for j in range(w)] for i in range(h)]:print(r)
print(max(reduce(operator.mul, score(i,j)) for i in range(h) for j in range(w))) # 2
