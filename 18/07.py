f=open('07.txt').read().strip().split('\n');f=[[x.split()[i] for i in [1,7]] for x in f]
from collections import defaultdict;g=defaultdict(list);o=defaultdict(int)
for p,c in f:g[p].append(c);o[c]+=1
q=sorted(n for n in g if 0==o[n]);s=[];q_=q.copy();o_=o.copy()
while q:
    n=q.pop(0);s.append(n)
    for c in g[n]:
        o[c]-=1
        if c in s or o[c]:continue
        q.append(c)
    q.sort()
print(''.join(s)) # p1
C=60;wa=lambda c:(c,ord(c)-ord('A')+C+1)
T=0;q=q_;o=o_;s=[];wn=5;w=[wa(q.pop(0)) for _ in range(min(len(q),wn))]
while w:
    T+=1
    w=[(n,t-1) for n,t in w] # time step
    for i in range(len(w))[::-1]: # try to add children
        n,t=w[i]
        if t==0: # if there's a free worker
            s.append(n);del w[i]
            for c in g[n]: # add it's children
                o[c]-=1
                if c in s or o[c]:continue
                q.append(c)
    q.sort() # sort alphabetically
    for i in range(min(len(q),wn-len(w))):w.append(wa(q.pop(0))) # add children if there are free workers
    # print('%3d'%T,*[w[i][0] if i<len(w) else '.' for i in range(wn)],''.join(s),sep='\t')
print(T) # p2 >918
