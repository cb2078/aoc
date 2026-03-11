t=set()
d={'e':2,'se':1+1j,'sw':-1+1j,'w':-2,'nw':-1-1j,'ne':1-1j}
for s in open('24.txt').read().strip().split('\n'):
	z=0
	i=0
	while i<len(s):
		j=1+i if s[i] in 'ew' else 2+i
		z+=d[s[i:j]]
		i=j
	(set.remove if z in t else set.add)(t,z)
print(len(t))

a=lambda z:{z+w for w in d.values()}
f=lambda z:(lambda x:z in t and 1<=x<=2 or z not in t and x==2)(len(t&a(z)))
for _ in range(100):
	t={z for z in set.union(t,*map(a,t)) if f(z)}
print(len(t))
