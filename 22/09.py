f=[m.split() for m in open('09.txt').read().rstrip().split('\n')]
f=[({'R':1,'U':1j,'L':-1,'D':-1j}[d],int(n)) for d,n in f]
from itertools import accumulate
heads=tuple(accumulate(d for d,n in f for _ in range(n)))
sgn=lambda x:complex(sgn(x.real),sgn(x.imag)) if type(x)==complex else (x>0)-(x<0)
g=lambda x:accumulate(x, lambda t,h:t if abs(h-t)<=abs(1+1j) else t+sgn(h-t), initial=0)
# print(f,heads,tails,sep='\n')
print(len(set(g(heads)))) # 1
for _ in range(9):heads=g(heads)
print(len(set(heads))) # 2
