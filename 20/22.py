def g(c):
	while all(c):
		i=c[0][0]<c[1][0]
		j=not i
		c[i].append(c[i].pop(0))
		c[i].append(c[j].pop(0))
	return i

r=0,1
def f(c):
	v=set()
	while all(c):
		if str(c) in v:
			return 0
		else:
			v.add(str(c))
		if all(c[i][0]<=len(c[i])-1 for i in r):
			i=f([c[i][1:][:c[i][0]] for i in r])
		else:
			i=c[0][0]<c[1][0]
		j=not i
		# print(*c,c[0][0],c[1][0],'player %d'%(i+1),sep='\n',end='\n\n')
		c[i].append(c[i].pop(0))
		c[i].append(c[j].pop(0))
	return i

for h in g,f:
	c=[list(map(int,s.split('\n')[1:])) for s in open('22.txt').read().strip().split('\n\n')]
	i=h(c)
	print(sum(x+x*k for k,x in enumerate(c[i][::-1])))
