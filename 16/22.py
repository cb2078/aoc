import re

l=open('22.txt').read().strip().split('\n')[2:]
n={}
for s in l:
    x,y,s,u,a=map(int,re.search(r'node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T',s).groups())
    n[x,y]=s,u,a

v=n.values()
s=0
for i,a in enumerate(v):
    for j,b in enumerate(v):
        if a[1] and i!=j and a[1]<b[2]:
            s+=1
print(s)

w,h=[1+max(z[i] for z in n) for i in [0,1]]
g=max(n,key=lambda z:(z[0],-z[1]))
f=next(z for z in n if not n[z][1])
b={z for z in n if n[z][1]>n[f][2]}
o=lambda:print('\n'.join(' '.join('_' if (x,y)==f else '#' if (x,y) in b else 'G' if (x,y)==g else '.' for x in range(w)) for y in range(h)))

q=[(f,g,0)]
v=set()
while q:
    f,g,t=q.pop(0)
    if (f,g) in v:
        continue
    v.add((f,g))
    if g==(0,0):
        print(t)
        break
    x,y=f
    for x,y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if x not in range(w) or y not in range(h):
            continue
        if (x,y) in b:
            continue
        q.append(((x,y),f if (x,y)==g else g,t+1))
