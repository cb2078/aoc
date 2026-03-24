P0=[list(map(int,open('07.txt').read().strip().split(','))) for _ in range(5)]
e=lambda j:p[p[i+j]] if 0==p[i]//10**(j+1)%10 else p[i+j]
def a(j,x):global i;p[p[i+j]]=x;i+=j+1

m=0
from itertools import permutations
for s in permutations(range(5)):
    o=0
    b=[1]*5
    for k in range(5):
        p=P0[0].copy()
        i=0
        while True:
            match z:=p[i]%100:
                case 1:
                    a(3,e(1)+e(2))
                case 2:
                    a(3,e(1)*e(2))
                case 3:
                    a(1,s[k] if b[k] else o)
                    b[k]=0
                case 4:
                    o=e(1)
                    i+=2
                case 5:
                    i=e(2) if e(1) else i+3
                case 6:
                    i=e(2) if not e(1) else i+3
                case 7:
                    a(3,e(1)<e(2))
                case 8:
                    a(3,e(1)==e(2))
                case 99:
                    break
                case _:
                    print(p,i,z)
                    raise
    m=max(m,o)
print(m)

m=0
from itertools import permutations
from copy import deepcopy
for s in permutations(range(5,10)):
    o=0
    k=0
    P=deepcopy(P0)
    I=[0]*5
    b=[1]*5
    d=[1]*5
    while any(d):
        p=P[k]
        i=I[k]
        while True:
            match z:=p[i]%100:
                case 1:
                    a(3,e(1)+e(2))
                case 2:
                    a(3,e(1)*e(2))
                case 3:
                    a(1,s[k] if b[k] else o)
                    b[k]=0
                case 4:
                    o=e(1)
                    i+=2
                    break
                case 5:
                    i=e(2) if e(1) else i+3
                case 6:
                    i=e(2) if not e(1) else i+3
                case 7:
                    a(3,e(1)<e(2))
                case 8:
                    a(3,e(1)==e(2))
                case 99:
                    d[k]=0
                    break
                case _:
                    print(p,i,z)
                    raise
        I[k]=i
        k+=1
        k%=5
    m=max(m,o)
print(m)
