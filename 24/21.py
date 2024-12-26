from functools import cache

@cache
def t(x,y):
    d={(-1,0):'^',(0,-1):'<',(0,1):'>',(1,0):'v'}
    k=[' ^A','<v>'] if any(c in [x,y] for c in '<>^v') else ['789','456,','123',' 0A']
    w,h=len(k[0]),len(k)
    I=lambda x:[(i,j) for i in range(h) for j in range(w) if k[i][j]==x].pop()
    q=[(I(x),)]
    m=float('inf')
    r=[]
    while q:
        p=q.pop(0)
        i,j=p[-1]
        if (i,j)==I(y) and len(p)<=m:
            m=len(p)
            r.append(''.join(d[yi-xi,yj-xj] for (xi,xj),(yi,yj) in zip(p,p[1:]))+'A')
            continue
        for di,dj in d:
            if i+di not in range(h) or j+dj not in range(w):
                continue
            if k[i+di][j+dj]== ' ':
                continue
            if (i+di,j+dj) in p:
                continue
            q.append((*p,(i+di,j+dj)))
    return r

@cache
def f(z,n):
    return sum(min(f(z,n-1) for z in t(x,y)) for x,y in zip('A'+z,z)) if n else len(z)

p=open('21.txt').read().strip().split('\n')
for n in [3,26]:print(sum(int(x[:-1])*f(x,n) for x in p))
