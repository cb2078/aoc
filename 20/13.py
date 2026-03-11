p=open('13.txt').read().strip().split('\n');
t=int(p[0])
b,o=zip(*[(int(x),i) for i,x in enumerate(p[1].split(',')) if x.isdigit()])
r=*range(len(b)),
x=min(b,key=lambda x:-t%x)
print(-t%x*x)

# t+o[i]==0 (mod b[i])
from math import prod
v=lambda a,m:a**(m-2)%m
X=[prod(b)//b[i] for i in r]
print(sum(-o[i]*X[i]*v(X[i],b[i]) for i in r)%prod(b))
