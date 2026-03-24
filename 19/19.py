from collections import defaultdict
from itertools import product

P=defaultdict(int)
for i,x in enumerate(open('19.txt').read().strip().split(',')):
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
  yield 'E'

def e(x):assert next(p)==x
def E():e('E')
def I(x):e('I');return p.send(x)
def O():x=next(p);assert x!='E' or x!='I';return x

def g(w):
  for z in range(w):
    for x in range(z):
      yield x,z
      yield z,x
    yield z,z

s=0
for x,y in g(50):
  p=f()
  I(x)
  I(y)
  s+=O()
  E()
print(s)

for x,y in g(9**9):
  for i,j in product((0,99),repeat=2):
    p=f()
    I(x+i)
    I(y+j)
    if not O():
      break
    E()
  else:
    print(x*10000+y)
    quit()
