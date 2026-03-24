from collections import defaultdict
P=defaultdict(int)
for i,x in enumerate(open('15.txt').read().strip().split(',')):
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
def I(x):e('I');return p.send(x)

def o():
  x,X,y,Y=(f(int((x.imag,x.real)[i]) for x in v) for i in (0,1) for f in (min,max))
  x,X,y,Y=-21,19,-19,21
  print('\n'.join(''.join(
    'S' if (w:=i*1j+j)==0 else 'Z' if w==z else '#.E'[v[w]] if w in v else ' ' for j in range(y,Y+1)) for i in range(x,X+1)))

d={0:0}
n=-1j,1j,1,-1
p=f()
v={0:1}
z=0
s=[]
while True:
  for i,w in list(enumerate(n))[::-1]:
    if z+w in v:
      continue
    v[z+w]=I(i+1)
    d[z+w]=d[z]+1
    match v[z+w]:
      case 1:
        z+=w
        s.append(i+1-i%2*2)
        break
      case 2:
        print(d[o:=z+w])
  else:
    if not s:
      break
    i=s.pop()
    I(i+1)
    z+=n[i]

t=0
a={o}
while b:={z+w for z in a for w in n if v[z+w]>0 and z+w not in a}:
  a|=b
  t+=1
print(t)
