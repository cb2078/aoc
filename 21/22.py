import itertools,math,copy

f=lambda x:('off','on').index(x)
g=lambda x:(lambda x,y:[int(x),int(y)+1])(*x[2:].split('..'))
a=[(lambda x,y:(f(x),[*map(g,y.split(',')),]))(*x.split())for x in open('22.txt').read().strip().split('\n')]
n=len(a)

g={}
for s,x in a:
  for w in itertools.product(*[range(*[min(max(y,-50),51) for y in z]) for z in x]):
    g[w]=s
print(sum(g.values()))

b=[a[0][1]]
for s,x in a[1:]:
  for i in range(len(b))[::-1]:
    y=b[i]
    if all(max(x[i][0],y[i][0])<min(x[i][1],y[i][1]) for i in range(3)):
      b.pop(i)
      for j in range(3):
        for k in range(2):
          if x[j][k] in range(*y[j]):
            z=copy.deepcopy(y)
            z[j][~k]=y[j][k]=x[j][k]
            if z[j][0]<z[j][1]:
              b.append(z)
  if s:
    b.append(x)
print(sum(math.prod(y-x for x,y in z) for z in b))
