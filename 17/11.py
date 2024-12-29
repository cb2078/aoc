d=['ne','n','nw','sw','s','se']
p=[d.index(x) for x in open('11.txt').read().strip().split(',')]

def f(p):
    c=[p.count(i) for i in range(6)]
    b=True
    while b:
        b=False
        for i in range(6):
            j=(i+2)%6
            if c[i] and c[j]:
                m=min(c[i],c[j])
                c[i]-=m
                c[j]-=m
                c[(i+1)%6]+=m
                b=True
            j=(i+3)%6
            if c[i] and c[j]:
                m=min(c[i],c[j])
                c[i]-=m
                c[j]-=m
                b=True
    return sum(c)

print(f(p))
print(max(f(p[:i]) for i in range(len(p))))
