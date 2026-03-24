from collections import defaultdict

P=defaultdict(int)
for i,x in enumerate(open('21.txt').read().strip().split(',')):
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

I=lambda x:p.send(x)

def O():
  for x in p:
    if x=='I':
      break
    elif x>=256:
      print(x)
      break
    # else:
    #   print(end=chr(x))

# any(a,b,c) and d
# any(a,b,c) and d and (e or h)
for s in ['''\
NOT J J
AND A J
AND B J
AND C J
NOT J J
AND D J
WALK''','''\
NOT J J
AND A J
AND B J
AND C J
NOT J J
AND D J
OR H T
OR E T
AND T J
RUN''']:
  p=f()
  O()
  for y in s:
    I(ord(y))
    O()
  I(10)
  O()
