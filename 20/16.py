g=(s for s in open('16.txt').read().strip().split('\n'))

f={}
while s:=next(g):
	k,v=s.split(': ')
	f[k]=tuple(tuple(map(int,x.split('-'))) for x in v.split(' or '))

next(g)
T=list(map(int,next(g).split(',')))

next(g)
next(g)
c=lambda x,v:any(x in range(a,b+1) for a,b in v)
t=[list(map(int,s.split(','))) for s in g]
a=0
for i in range(len(t))[::-1]:
	for x in t[i]:
		if all(not c(x,v) for v in f.values()):
			a+=x
			del t[i]
			break
print(a)

K=[]
n=len(f)
m=[[0]*n for _ in range(n)]
for i in range(n):
	for j,(k,v) in enumerate(f.items()):
		K.append(k)
		if all(c(r[i],v) for r in t):
			m[j][i]=1
o=lambda:print('\n'.join(' '.join(map(str,m[i]))+' %s'%K[i] for i in range(n)))

c={}
for _ in range(20):
	for i in range(n):
		if m[i].count(1)==1:
			j=m[i].index(1)
			c[K[i]]=j
			for k in range(n):
				m[k][j]=0
			break

from math import prod
print(prod(T[i] for k,i in c.items() if k.startswith('departure')))
