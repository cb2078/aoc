n=20
r=*range(n),
g=[[[[0]*n for _ in r] for _ in r] for _ in r]
d=[-1,0,1]
a=lambda i,j,k  :sum(g[(i+di)%n][(j+dj)%n][(k+dk)%n][0]        for di in d for dj in d for dk in d             if di or dj or dk)
A=lambda i,j,k,l:sum(g[(i+di)%n][(j+dj)%n][(k+dk)%n][(l+dl)%n] for di in d for dj in d for dk in d for dl in d if di or dj or dk or dl)
for i,s in enumerate(open(0).read().strip().split('\n')):
	for j,c in enumerate(s):
		g[i][j][0][0]='.#'.index(c)
from copy import deepcopy
G=deepcopy(g)
u=lambda x,y:y in [2,3] if x else y==3
def f(g,p):
	G=[[[[0]*n for _ in r] for _ in r] for _ in r]
	for i in r:
		for j in r:
			for k in r:
				if p==1:
					G[i][j][k][0]=u(g[i][j][k][0],a(i,j,k))
				else:
					for l in r:
						G[i][j][k][l]=u(g[i][j][k][l],A(i,j,k,l))
	return G
for p in 1,2:
	g=deepcopy(G)
	for _ in range(6):g=f(g,p	)
	print(sum(g[i][j][k][l] for i in r for j in r for k in r for l in r))
