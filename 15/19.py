import re,functools as ft,itertools
r,m=open('19.txt').read().strip().split('\n\n');r=[x.split(' => ') for x in r.split('\n')]
f=lambda m:{m[:i]+x+m[i+len(y):] for i in range(len(m)) for x,y in r if y==m[i:i+len(y)]}
g=ft.cache(lambda m:{(o,d+1) for n in x for o,d in g(n)} if len(x:=f(m)) else {(m,0)})
h=lambda m:(ft.reduce(lambda x,y:(x[0]+y[0],x[1]+y[1]),t) for t in itertools.product(*map(g,re.split(r'(?<=Ar)',m))))
l=lambda m: min(d+l(n) if d else 0 if n=='e' else float('inf') for n,d in h(m))
print(len({m[:i]+y+m[i+len(x):] for i in range(len(m)) for x,y in r if x==m[i:i+len(x)]}),l(m),sep='\n') #1: 195<674
