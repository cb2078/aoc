m=open('10.txt').read().strip().split('\n')
S={(j,i) for i,s in enumerate(m) for j,c in enumerate(s) if c=='#'}
w=len(m)

im=jm=None
z=0
from math import gcd as g,lcm as l,atan2 as a,pi as p
for i,j in S:
    x=0
    for di in range(-i,w-i):
        for dj in range(-j,w-j):
            if g(di,dj)-1:
                continue
            k=1
            y=0
            while True:
                s=i+di*k,j+dj*k
                k+=1
                if s[0] not in range(w) or s[1] not in range(w):
                    break
                y|=s in S
            x+=y
    if x>z:
        im,jm=i,j
        z=x
print(z)

from collections import defaultdict
d=defaultdict(list)
for i,j in S:
    d[(2*p+1e-9+a(i-im,jm-j))%(2*p)].append((i,j))
l=[sorted(d[k],key=lambda x:abs(x[0]-im)+abs(x[1]-jm)) for k in sorted(d)]

i=0
for n in range(199):
    del l[i][0]
    if not l[i]:
        del l[i]
    else:
        i+=1
        i%=len(l)
i,j=l[i][0]
print(i*100+j)
