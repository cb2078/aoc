p=[x.split() for x in open('23.txt').read().strip().split('\n')]
n=len(p)
g=lambda x:r[x] if x.isalpha() else int(x)

i=0
r={k:0 for k in 'abcdefgh'}
a=0
while i<n:
    o,x,y=p[i]
    match o:
        case 'set':
            r[x]=g(y)
        case 'sub':
            r[x]-=g(y)
        case 'mul':
            r[x]*=g(y)
            a+=1
        case 'jnz':
            i+=g(y)-1 if g(x) else 0
        case _:
            raise
    i+=1
print(a)

# a=True
# b=c=d=e=f=g=h=0
# --------------------------------------------------------------------------------
# b=81
# c=b
# if a:
#     b*=100
#     b+=100000
#     c=b
#     b+=17000
# for b in range(b,c+1,17):
#     f=True
#     for d in range(2,b):
#         for e in range(2,b):
#             if d*e==b:
#                 f=False
#     if not f:
#         h+=1
# print(h)

b,c=108100,125100
A=[1]*(c+100)
import math
for i in range(2,math.isqrt(c+100)):
    if A[i]:
        for j in range(i*i,c+100,i):
            A[j]=0
print(sum(0==A[i] for i in range(b,c+1,17)))
