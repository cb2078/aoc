from collections import defaultdict
P=defaultdict(int)
for i,x in enumerate(open('11.txt').read().strip().split(',')):
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
        a(1,(yield))
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

def g(y):
  z=0
  w=-1j
  m=defaultdict(int)
  m[z]=y
  x=f()
  while True:
    try:
      next(x)
    except StopIteration:
      break
    m[z]=x.send(m[z])
    w*=[-1j,1j][next(x)]
    z+=w
  return m

print(len(g(0)))
m=g(1)
x,X,y,Y=(f(int((x.imag,x.real)[i]) for x in m if m[x]) for i in (0,1) for f in (min,max))
print('\n'.join(' '.join(' #'[m[i*1j+j]] for j in range(y,Y+1)) for i in range(x,X+1)))
