l=[[set(x.replace(',','').split()) for x in s[:-1].split(' (contains ')] for s in open('21.txt').read().strip().split('\n')]
a={x for f in l for x in f[1]}
d={x:set.intersection(*(f[0] for f in l if x in f[1])) for x in a}
i=set.union(*(f[0] for f in l))-set.union(*d.values())
print(sum(len(f[0]&i) for f in l))

s=set(d.keys())
while s:
	s.remove(k:=next(k for k in s if len(d[k])==1))
	for K in s:d[K]-=d[k]
print(','.join(d[k].pop() for k in sorted(d)))
