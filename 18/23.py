import re,itertools
r=[[*map(int,re.findall(r'-?\d+',x))] for x in open('23.txt').read().strip().split('\n')]
n=len(r)
i=max(range(len(r)),key=lambda i:r[i][3])
d=lambda x,y:sum(abs(x[k]-y[k]) for k in range(3))
print(sum(d(r[i],r[j])<=r[i][3] for j in range(n)))

a=[0]*3
b=1<<29
while b:
 def f(c):
  s=0
  for i in range(n):
   v=[]
   for k in range(3):
    x,y=a[k],a[k]+b*c[k]
    x,y=min(x,y),max(x,y)-1
    v.append(x if r[i][k]<x else y if r[i][k]>y else r[i][k])
   s+=d(v,r[i])<=r[i][3]
  return s
 c=max(itertools.product((-1,1),repeat=3),key=f)
 b>>=1
 if b:
  a=[a[k]+b*c[k] for k in range(3)]
 else:
  a=[a[k]+min(0,c[k]) for k in range(3)]
print(sum(a))
