a=[int(x.split()[-1])-1 for x in open('21.txt').read().strip().split('\n')]
d=1
s=[0]*2
i=0
n=0
while True:
  for j in range(3):
    a[i]=(a[i]+d)%10
    d=d%10+1
    n+=1
  s[i]+=a[i]+1
  if s[i]>=1000:
    print(s[~i]*n)
    break
  i^=1

import itertools
z={}
def f(a,s,i):
  if s[~i]>=21:
    return i,1-i
  if (*a,*s,i) in z:
    return z[*a,*s,i]
  r=0,0
  for D in itertools.product(range(1,4),repeat=3):
    A,S=a[:],s[:]
    for d in D:
      A[i]=(A[i]+d)%10
    S[i]+=A[i]+1
    x,y=f(A,S,1-i)
    r=r[0]+x,+r[1]+y
  z[*a,*s,i]=r
  return r
print(max(f(a,[0]*2,0)))
