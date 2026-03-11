t=[]
I=[]
for s in open('20.txt').read().strip().split('\n\n'):
	l=s.split('\n')
	I.append(int(l[0][5:9]))
	del l[0]
	t.append(l)
n=len(t)

o=lambda i:print('\n'.join(''.join(x) for x in t[i])+'\n'	)
def f(y,a): # i-axis
	if a==0:
		return [x[::-1] for x in y]
	else:
		y=r(y,1)
		y=f(y,0)
		y=r(y,3)
		return y
def r(y,c): # cw
	for _ in range(c):
		y=[''.join(y[~k][j] for k in range(len(y))) for j in range(len(y))]
	return y

def e(i):
	g=lambda k,i,j,di,dj:''.join(t[k][i+di*x][j+dj*x] for x in range(10))
	return [g(i,0,0,1,0),g(i,0,0,0,1),g(i,-1,0,0,1),g(i,0,-1,1,0)] # LUDR
v={0}
def h(i,j):
	for k in range(4):
		if e(i)[k]==e(j)[3-k]:
			return k
def c(i,j):
	if i in v:
		return h(i,j)
	for x in range(2):
			t[i]=f(t[i],x)
			for y in range(4):
				t[i]=r(t[i],y)
				k=h(i,j)
				if k is not None:
					v.add(i)
					return k
from collections import defaultdict
g=defaultdict(lambda:[None]*4)
while len(v)<len(t):
	for i in range(n):
		if i in v:
			continue
		for j in v:
			k=c(i,j)
			if k is not None:
				break
for i in range(n):
	for j in range(n):
		if i==j:
			continue
		k=c(i,j)
		if k is not None:
			g[i][k]=j
from math import prod,isqrt
print(prod(I[i] for i in range(n) if g[i].count(None)==2))

i=next(i for i in g if g[i][1] is None and g[i][0] is None)
l=0
p=['']*8*isqrt(n)
for _ in range(isqrt(n)):
	k=i
	for _ in range(isqrt(n)):
		for j in range(1,9):
			p[l+j-1]+=''.join(t[i][j][1:9])
		i=g[i][3]
	i=g[k][2]
	l+=8
n=len(p)

m='                  # ','#    ##    ##    ###',' #  #  #  #  #  #   '
w=len(m[0])
for x in range(2):
	p=f(p,x)
	for y in range(4):
		p=r(p,y)
		if z:=sum(all(m[x][y]==' ' or p[i+x][j+y]=='#' for x in range(3) for y in range(w))
		          for i in range(n-3) for j in range(n-w)):
			print(sum(p[i][j]=='#' for i in range(n) for j in range(n))\
			      -z*sum(m[x][y]=='#' for x in range(3) for y in range(w)))
			quit()
