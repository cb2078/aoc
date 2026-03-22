from collections import defaultdict
p={}
c=defaultdict(list)
for x,y in (s.split(')') for s in open('06.txt').read().strip().split('\n')):
    p[y]=x
    c[x].append(y)

n=0
for x in p:
    while x!='COM':
        x=p[x]
        n+=1
print(n)

v=set()
q=[('YOU',0)]
while q:
    x,n=q.pop(0)
    if x in v:
        continue
    v.add(x)
    if x==p['SAN']:
        print(n-1)
        break
    if x in p:
        q.append((p[x],n+1))
    for x in c[x]:
        q.append((x,n+1))

