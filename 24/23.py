from collections import defaultdict;g=defaultdict(list)
for x,y in [x.split('-') for x in open('23.txt').read().strip().split('\n')]:g[x].append(y);g[y].append(x)
c={(*sorted([x,y,z]),) for x in g for y in g[x] for z in g[x] if y!=z and z in g[y]}
print(sum(any(x[0]=='t' for x in y) for y in c))

def f(s):
    c=[]
    if not s:return c
    for v in s:all(v in g[u] for u in c) and c.append(v)
    return max(c,f(s[1:]),key=len)
print(','.join(f(sorted(g.keys()))))
