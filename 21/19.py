import itertools,collections

a=[[[*map(int,y.split(','))] for y in x.split('\n')[1:]] for x in open('19.txt').read().strip().split('\n\n')]
n=len(a)
d=lambda u,v:[u[i]-v[i] for i in range(3)]

o={0:[0,0,0]}
s=set()
def f(i):
  if i in s:
    return
  s.add(i)
  x=a[i]
  for j in set(range(n))-s:
    for p in itertools.permutations(range(3)):
      for r in itertools.product((-1,1),repeat=3):
        y=[[u[p[i]]*r[i] for i in range(3)] for u in a[j]]
        z=collections.defaultdict(int)
        for u,v in itertools.product(x,y):
          z[*d(v,u)]+=1
        if z[u:=max(z,key=lambda u:z[u])]>=12:
          a[j]=[d(v,u) for v in y]
          o[j]=[-u[i] for i in range(3)]
          f(j)
          break
f(0)

z=set()
for i in range(n):
  for u in a[i]:
    z.add(tuple(u))
print(len(z),max(sum(map(abs,d(o[i],o[j]))) for i in range(n) for j in range(i)),sep='\n')
