import re

f=lambda x:(lambda x,y:(y,int(x)))(*x.split())
g=lambda x:(lambda x,y:(f(y)[0],(f(y)[1],dict(map(f,x.split(', '))))))(*x.split(' => '))
r=dict(map(g,(s:=open('14.txt').read().strip()).split('\n')))

def f(x):
  d={k:(k=='FUEL')*x for k in re.findall(r'[A-Z]+',s)}
  while any(d[k]>0 for k in d if k!='ORE'):
    for k in d.keys()-{'ORE'}:
      d[k]-=r[k][0]*(c:=(d[k]+r[k][0]-1)//r[k][0])
      for K in r[k][1]:d[K]=d.get(K,0)+r[k][1][K]*c
  return d['ORE']

g=lambda a=0,b=1<<40:a if b-a==1 else g(a+m,b) if f(a+(m:=b-a>>1))<1e12 else g(a,b-m)

print(f(1),g(),sep='\n')
