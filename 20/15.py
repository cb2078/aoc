l=list(map(int,open('15.txt').read().strip().split(',')))

from collections import defaultdict
d=defaultdict(list,((x,[i]) for i,x in enumerate(l)))
x=l[-1]
for t in range(len(l),30000000):
	x=0 if len(d[x])==1 else d[x][-1]-d[x][-2]
	d[x].append(t)
	if t==2019:
		print(x)
print(x)
