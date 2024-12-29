C=[tuple(map(int,x.split('/'))) for x in open('24.txt').read().strip().split('\n')]
E=enumerate
o=lambda c,p:c[~c.index(p)]

d={}
def f(p,x):
    if (p,x) in d:
        return d[p,x]
    r=0
    for i,c in E(C):
        if x&(1<<i):
            continue
        if p not in c:
            continue
        r=max(f(o(c,p),x|(1<<i)),r)
    if r==0:
        r=sum(sum(C[i]) for i in range(64) if x&(1<<i))
    d[p,x]=r
    return r

print(max(f(o(c,0),1<<i) for i,c in E(C) if 0 in c))
print(d[max(d,key=lambda k:(k[1].bit_count(),d[k]))])
