v=list(map(int,open('08.txt').read().strip().split()));vn=len(v)
i=0
def f():
    global i
    c,m=v[i:i+2];i+=2#;print(c,m)
    r=sum(f() for _ in range(c))+sum(v[i:i+m])
    i+=m;return r
print(f()) # p1
i=0
def g():
    global i
    c,m=v[i:i+2];i+=2#;print(c,m)
    if c:x={1+j:g() for j in range(c)};r=sum(x[j] if j in x else 0 for j in v[i:i+m])
    else:r=sum(v[i:i+m])
    i+=m;return r
print(g()) # p2
