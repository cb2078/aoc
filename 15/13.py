import re
from itertools import permutations as P
s=open('13.txt').read().strip()
g={(u,v):eval('+-'[s=='lose']+x) for u,s,x,v in re.findall('([A-Z][a-z]+).*?(gain|lose) (\d+).*?([A-Z][a-z]+)',s)}
K=lambda:{k[0] for k in g}
e=lambda p:sum((g[x,y]+g[y,x]) for x,y in zip(p,[p[-1],*p[:-1]]))
print(max(map(e,P(K())))) # <946
for k in K():g[k,'']=g['',k]=0
print(max(map(e,P(K()))))
