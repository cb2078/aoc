X=list(map(int,open('22.txt').read().strip().split('\n')))
m=lambda x,s:x^s
p=lambda x:x%16777216
f0=lambda x:p(m(x*64,x))
f1=lambda x:p(m(x//32,x))
f2=lambda x:p(m(x*2048,x))
f=lambda x:f2(f1(f0(x)))

def F(x):
    for _ in range(2000):x=f(x)
    return x
print(sum(map(F,X)))

from collections import defaultdict
d=defaultdict(int)
for x in X:
    a=[x]
    for _ in range(2000):x=f(x);a.append(x)
    a=[x%10 for x in a]
    c=[y-x for x,y in zip(a,a[1:])]
    v=set()
    for i in range(len(c)-3):
        k=tuple(c[i:i+4])
        if k in v:continue
        v.add(k)
        d[k]+=a[i+4]
print(max(d.values()))
