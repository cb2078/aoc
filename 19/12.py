import re
import math

p=[list(map(int,re.findall(r'[-\d]+',x))) for x in open('12.txt').read().strip().split('\n')]
r=tuple(range(len(p)))
v=[[0]*3 for _ in r]
f=lambda x,y:(x<y)-(x>y)
o=lambda:print(n,'\n'.join('%d: '%i+' | '.join(''.join('%3d'%x[i][k] for k in range(3   )) for x in [p,v]) for i in r),sep='\n',end='\n\n')
e=lambda x:sum(map(abs,x))
n=0
d=[set() for _ in range(3)]
c=[0]*3
while True:
    if n==1000:
        print(sum(e(p[i])*e(v[i]) for i in r))
    v=[[v[i][k]+sum(f(p[i][k],p[j][k]) for j in r) for k in range(3)] for i in r]
    p=[[p[i][k]+v[i][k] for k in range(3)] for i in r]
    for k in range(3):
        t=tuple(x[i][k] for x in [p,v] for i in r)
        if t in d[k] and not c[k]:
          c[k]=n
        else:
            d[k].add(t)
        if all(c):
            print(math.lcm(*c))
            quit()
    n+=1
