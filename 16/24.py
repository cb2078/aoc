m=open('24.txt').read().strip().split('\n')
w,h=len(m[0]),len(m)
r=[(i,j) for i in range(h) for j in range(w)]
d=[[1e9 for k in range(8)] for k in range(8)]

for i,j in filter(lambda t:m[t[0]][t[1]].isnumeric(),r):
    k=int(m[i][j])
    q=[(i,j,0)]
    v=[[0]*w for _ in range(h)]
    v[i][j]=1
    while q:
        i,j,t=q.pop(0)
        if m[i][j].isnumeric():
            d[k][int(m[i][j])]=t
        for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if m[i][j]=='#':
                continue
            if v[i][j]:
                continue
            v[i][j]=1
            q.append((i,j,t+1))

from itertools import permutations as p
print(min(d[0][x[0]]+sum(d[x[i]][x[i+1]] for i in range(6)) for x in p(range(1,8))))
print(min(d[x[-1]][0]+d[0][x[0]]+sum(d[x[i]][x[i+1]] for i in range(6)) for x in p(range(1,8))))

