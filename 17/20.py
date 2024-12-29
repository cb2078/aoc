import re
p,v,a=zip(*[[list(map(int,re.findall(r'[-\d]+',y))) for y in x.split(', ')] for x in open('20.txt').read().rstrip().split('\n')])
n=len(p);R=list(range(n))
d=lambda x:sum(map(abs,x))
m=min(map(d,a))
I=[i for i in R if d(a[i])==m]
print(min(I,key=lambda i:d(v[i])))

def q(a,b,c):
    if a==0:
        r={-c/b} if b else set()
    else:
        r={(-b+o*(b**2-4*a*c)**(1/2))/(2*a) for o in [1,-1]}
        r={x for x in r if type(x)!=complex}
    return {x for x in r if x%1==0 and x>=0}
from collections import defaultdict
c=defaultdict(list)
t=defaultdict(set)
for i in range(n):
    for j in range(i):
        x,y,z=[q((a[i][k]-a[j][k])/2,
                 v[i][k]-v[j][k]+(a[i][k]-a[j][k])/2,
                 p[i][k]-p[j][k]) for k in range(3)]
        if x&y&z:
            c[i].append(j)
            c[j].append(i)
            k=(x&y&z).pop()
            t[k].add(i)
            t[k].add(j)
print(sum(c[i]==[] for i in range(n)))

# # nasty simulation version
# from collections import defaultdict
# d=defaultdict(list)
# for t in range(1,1000):
#     for i in R:
#         for j in range(3):
#             v[i][j]+=a[i][j]
#             p[i][j]+=v[i][j]
#         d[tuple(p[i])].append(i)
#     for l in d.values():
#         if len(l)>1:
#             for i in l:
#                 if i in R:
#                     R.remove(i)
# print(len(R))

