from collections import defaultdict
f=open('03.txt').read().strip().split('\n');d=defaultdict(int)
assert list(range(len(f))) ==[int(x.split()[0][1:])-1 for x in f]
# om=lambda:print('\n'.join(''.join('.' if d[i,j]==0 else '/' if d[i,j]==1 else '#' for j in range(32)) for i in range(32)))
for i in range(len(f)):xs=f[i].split()[-2:];xs=xs[0].split(',')+xs[1].split('x');xs[1]=xs[1][:-1];f[i]=list(map(int,xs))
for xs in f:
    for i in range(xs[0],xs[0]+xs[2]):
        for j in range(xs[1],xs[1]+xs[3]):d[i,j]+=1
s=sum(d[k]>1 for k in d);print(s) # p1
for i,xs in enumerate(f):
    if all(d[i,j]==1 for i in range(xs[0],xs[0]+xs[2]) for j in range(xs[1],xs[1]+xs[3])):print(1+i) # p2
