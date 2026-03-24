from collections import defaultdict
P=defaultdict(int)
for i,x in enumerate(open('13.txt').read().strip().split(',')):
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

s=0
p=f()
while (x:=next(p,None))!=None:
  y,t=next(p),next(p)
  s+=t==2
print(s)

d=[[' ']*42 for _ in range(24)]
p=f(2)
g=lambda x:next(j for i in range(len(d)) for j in range(len(d[0])) if d[i][j]==x)
while (x:=next(p,None))!=None:
  if x=='I':
    x=p.send(g('o')-g('|'))
  y,t=next(p),next(p)
  if x!=-1:
    d[y][x]=' #8|o'[t]
    # print()
  # else:
    # print('score',t)
  # print(*(''.join(x) for x in d),'',sep='\n')
print(t)
