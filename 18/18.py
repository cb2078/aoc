s='.|#';m0=m=[[s.index(y) for y in x] for x in open('18.txt').read().strip().split('\n')]
n=len(m0);r=*range(n),
o=lambda:print('\n'.join(''.join(s[y] for y in x) for x in m)) or print()
a=lambda x,y:[m[i][j] for i in range(x-1,x+2) for j in range(y-1,y+2) if i in r and j in r and (i!=x or j!=y)]
f=lambda x,y:[y.count(1)>=3,y.count(2)>=3,2 not in y or 1 not in y][x]
c=lambda x:sum(y.count(x) for y in m)
g=lambda m:[[(m[i][j]+f(m[i][j],a(i,j)))%3 for j in r] for i in r]

def v(T):
    global m;m=m0
    for t in range(T):m=g(m)
    return c(1)*c(2)
print(v(10))

h=lambda:sum(m[i][j]*3*(i+j*n) for i in r for j in r)
m=m0;d={h():0}
for t in range(9999):
    m=g(m)
    if (k:=h()) in d:T=d[k]+(1000000000-d[k])%(t-d[k]);break
    d[k]=t
print(v(T))
