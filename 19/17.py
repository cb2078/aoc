from collections import defaultdict
from itertools import takewhile

P=defaultdict(int)
for i,x in enumerate(open('17.txt').read().strip().split(',')):
  P[i]=int(x)

def f(z=P[0]):
  E=lambda j:p[i+j] if (x:=p[i]//10**(j+1)%10)==0 else i+j if x==1 else p[i+j]+b if x==2 else ...
  e=lambda j:p[E(j)]

  def a(j,x):
    nonlocal i
    k=E(j)
    assert k>=0
    p[k]=x
    i+=j+1

  p=P.copy()
  p[0]=z
  b=0
  i=0
  while True:
    match p[i]%100:
      case 1:
        a(3,e(1)+e(2))
      case 2:
        a(3,e(1)*e(2))
      case 3:
        a(1,(yield 'I'))
        yield
      case 4:
        yield e(1)
        i+=2
      case 5:
        i=e(2) if e(1) else i+3
      case 6:
        i=e(2) if not e(1) else i+3
      case 7:
        a(3,e(1)<e(2))
      case 8:
        a(3,e(1)==e(2))
      case 9:
        b+=e(1)
        i+=2
      case 99:
        break
      case _:
        print(i,p[i])
        raise

I=lambda x:(p.send(ord(x[0])),O(),I(x[1:])) if x else None
# O=lambda:print(end=''.join(map(chr,takewhile(lambda x:x!='I',p))))
O=lambda:list(takewhile(lambda x:x!='I',p))

a=''.join(chr(x) for x in f()).strip().split('\n')
o=[(i,j) for i in range(1,len(a)-1) for j in range(1,len(a[i])-1) if all(a[x][y]=='#' for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)))]
print(sum(i*j for i,j in o))

def g(z,w,v,p):
  if len(v)==t:
    yield from h(','.join(map(str,p)))
  for z,w,c in (z+w,w,''),(z+w*1j,w*1j,'R'),(z+w*-1j,w*-1j,'L'):
    i,j=int(z.imag),int(z.real)
    if (i not in range(len(a)) or j not in range(len(a[i])) or
        a[i][j]=='.' or
        (i,j) not in o and z in v):
      continue
    yield from g(z,w,v|{z},p+[c,1] if c else p[:-1]+[p[-1]+1])

def h(s,d=0,r=[]):
  S='ABC'
  if d==len(S):
    if len(s)<=20 and all(x in S+',' for x in s):
      yield (s,*r)
    return
  l=s.split(',')
  j=next(j for j in range(len(l)) if l[j] not in S)
  for i in range(j,len(l)):
    x=','.join(l[j:i+1])
    if len(x)>20 or any(y in x for y in S):
      break
    yield from h(s.replace(x,S[d]),d+1,r+[x])

p=f(2)
t=sum(y!='.' for x in a for y in x)
x=next(g(z:=next(i*1j+j for i in range(len(a)) for j in range(len(a[i])) if a[i][j]=='^'),-1j,{z},[]))
O()
for y in x:
  for z in y+'\n':
    p.send(ord(z))
    O()
for z in 'n\n':
  p.send(ord(z))
  for x in p:
    if x=='I':
      break
print(x)
