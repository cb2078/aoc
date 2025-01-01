from collections import defaultdict
g=defaultdict(list);d={}
for l in open('09.txt').read().strip().split('\n'):u,_,v,_,x=l.split();g[u].append(v);g[v].append(u);d[u,v]=d[v,u]=int(x)
def f(v,r):
    q=[(0,v)]
    while q:
        x,*p=q.pop(0);v=p[-1]
        if len(p)==len(g):return x
        for u in g[v]:
            if u not in p:q.append((x+d[v,u],*p,u))
        q.sort(reverse=r)
for m,x in [(min,False),(max,True)]:print(m(f(v,x) for v in g))
