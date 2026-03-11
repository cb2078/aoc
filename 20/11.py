s='.L#';G=g=[[s.index(y) for y in x] for x in open('11.txt').read().strip().split('\n')];ri=*range(len(g)),;rj=*range(len(g[0])),
a=lambda i,j:[g[x][y] for x,y in m[i][j]] if p else \
  [g[x][y] for x in range(i-1,i+2) for y in range(j-1,j+2) if x in ri and y in rj and (x!=i or y!=j)]
f=lambda i,j:(lambda x:2 if g[i][j]==1 and 2 not in x else 1 if g[i][j]==2 and x.count(2)>=4+p else g[i][j])(a(i,j))
o=lambda:print('\n'.join(''.join(s[g[i][j]] for j in rj) for i in ri)+'\n')
h=lambda:sum(g[i][j]*3*(i*len(g)+j) for i in ri for j in rj)

def z(i,j):
	for di in [-1,0,1]:
		for dj in [-1,0,1]:
			if di==0 and dj==0:
				continue
			n=1
			while (x:=i+di*n) in ri and (y:=j+dj*n) in rj:
				if g[x][y]:
					yield x,y
					break
				n+=1
m=[[list(z(i,j)) for j in rj] for i in ri]

for p in [0,1]:
	v=set();g=G
	while (x:=h()) not in v:v.add(x);g=[[f(i,j) for j in rj] for i in ri]
	print(sum(g[i][j]==2 for i in ri for j in rj))
