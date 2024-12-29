f=[(*map(int,x.split(': ')),) for x in open('13.txt').read().strip().split('\n')]
def a(t,r):r-=1;t%=2*r;return t if t<=r else r-t%r
print(sum(t*r for t,r in f if a(t,r)==0))
from itertools import count
print(next(i for i in count() if all(a(t+i,r) for t,r in f)))

# l,r=zip(*[map(int,x.split(': ')) for x in open('13.txt').read().strip().split('\n')])
# n=len(l)
# p=[2*(x-1) for x in r]
# def a(i):n=r[i]-1;j=l[i]%(2*n);return j if j<=n else n-j%n
# print(sum(l[i]*r[i] for i in range(n) if 0==a(i)))
#
# f=lambda i:[j for j in range(p[i]) if j!=-l[i]%p[i]]
# from math import lcm
# i=0
# x=f(i)
# m=p[i]
# while i<n-1:
#     y=f(i+1)
#     M=lcm(m,p[i+1])
#     x=[z for z in x for z in range(z,M,m) if z%p[i+1] in y]
#     m=M
#     i+=1
# print(min(x))

