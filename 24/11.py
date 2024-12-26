p=list(map(int,open('11.txt').read().strip().split()));P=p.copy()
def s(x):sx=str(x);n=len(sx);return [1] if x==0 else [int(sx[:n//2]),int(sx[n//2:])] if n%2==0 else [2024*x]
for k in range(25):
    for i in range(len(p))[::-1]:p[i:i+1]=s(p[i])
print(len(p))

from collections import defaultdict
d={x:1 for x in P}
for k in range(75):
    D=defaultdict(int)
    for x in d:
        for y in s(x):D[y]+=d[x]
    d=D
print(sum(d.values()))
