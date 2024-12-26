m=open('08.txt').read().strip().split('\n');n=len(m);R=list(range(n))
from collections import defaultdict
d=defaultdict(list)
for i in range(n):
    for j in range(n):
        if m[i][j]!='.':d[m[i][j]].append((i,j))
s={tuple(2*A[i]-a[i] for i in range(2)) for k in d for a in d[k] for A in d[k] if a!=A}
print(sum(i in R and j in R for i,j in s))
s={tuple(a[i]+N*(A[i]-a[i]) for i in range(2)) for k in d for a in d[k] for A in d[k] for N in range(50) if a!=A}
print(sum(i in R and j in R for i,j in s))
