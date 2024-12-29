p=[x.split(' <-> ') for x in open('12.txt').read().strip().split('\n')]
g={}
for x,y in p:
    g[x]=y.split(', ')

x='0'
q=[x]
s={x}
r=0
while q:
    x=q.pop()
    r+=1
    for x in g[x]:
        if x in s:
            continue
        s.add(x)
        q.append(x)
print(r)

s=set()
r=0
while X:=g.keys()-s:
    x=X.pop()
    q=[x]
    while q:
        x=q.pop()
        for x in g[x]:
            if x in s:
                continue
            s.add(x)
            q.append(x)
    r+=1
print(r)

