from collections import defaultdict

P=defaultdict(int)
for i,x in enumerate(open('23.txt').read().strip().split(',')):
  P[i]=int(x)

def f():
  E=lambda j:p[i+j] if (x:=p[i]//10**(j+1)%10)==0 else i+j if x==1 else p[i+j]+b if x==2 else ...
  e=lambda j:p[E(j)]

  def a(j,x):
    nonlocal i
    k=E(j)
    assert k>=0
    p[k]=x
    i+=j+1

  p=P.copy()
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

def e(x):
  assert next(p[i])==x

def I(*x):
  for j,y in enumerate(x):
    if j:
      e('I')
    p[i].send(y)

def O():
  return x if (x:=next(p[i]))=='I' else (x,next(p[i]),next(p[i]))

N=None
v=set()
z=0
n=50
p=[f() for _ in range(n)]
q=[[] for _ in range(n)]
for i in range(n):
  e('I')
  I(i,-1)
while True:
  if z==50:
    _,y=N
    if y in v:
      print(y)
      break
    v.add(y)
    q[0].append(N)
  match O():
    case 'I':
      if q[i]:
        I(*q[i].pop(0))
        z=0
      else:
        I(-1)
        z+=1
    case (j,x,y):
      if j==255:
        if N is None:
          print(y)
        N=x,y
      else:
        q[j].append((x,y))
      z=0
    case _:
      raise
  i=(i+1)%n
