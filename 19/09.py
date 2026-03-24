from collections import defaultdict
P=defaultdict(int)
for i,x in enumerate(open('09.txt').read().strip().split(',')):
  P[i]=int(x)

E=lambda j:p[i+j] if (x:=p[i]//10**(j+1)%10)==0 else i+j if x==1 else p[i+j]+b if x==2 else ...
e=lambda j:p[E(j)]

def a(j,x):
  global i
  p[E(j)]=x
  i+=j+1

for x in 1,2:
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
        a(1,x)
      case 4:
        print(e(1))
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
