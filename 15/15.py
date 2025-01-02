import re,itertools
p=[tuple(map(int,re.findall(r'-?\d+',x))) for x in open('15.txt').read().strip().split('\n')];n=len(p);#;print(p)
def f(n,r):
    if r-1:yield from ([i]+x for i in range(n+1) for x in f(n-i,r-1))
    else:yield [n]
r=R=0
for x in f(100,n):a,b,c,d,e=[max(0,sum(p[i][j]*x[i] for i in range(n))) for j in range(5)];r=max(r,y:=a*b*c*d);R=max(R,y) if e==500 else R
print(r,R,sep='\n')
