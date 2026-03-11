a=[[*map(int,x.split(','))] for x in open('25.txt').read().strip().split('\n')]
n=len(a)
d=lambda i,j:sum(abs(a[i][k]-a[j][k]) for k in range(4))

g=[[] for _ in range(n)]
for i in range(n):
  for j in range(i):
    if d(i,j)<=3:
      g[i].append(j)
      g[j].append(i)

r=0
v=set()
for i in range(n):
  s=[i]
  u=set()
  while s:
    i=s.pop()
    if i in u|v:
      continue
    u.add(i)
    for j in g[i]:
      s.append(j)
  if u:
    v|=u
    r+=1
print(r)
