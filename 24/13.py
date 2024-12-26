import re,numpy as np
l=[list(map(int,re.findall(r'\d+',x))) for x in open('13.txt').read().strip().split('\n\n')]
def g(a,d,b,e,c,f,p):
    if p:c+=10000000000000;f+=10000000000000
    if (b*f-e*c)%(b*d-e*a):return 0
    x=(b*f-e*c)//(b*d-e*a)
    if (c-a*x)%b:return 0
    y=(c-a*x)//b
    return 3*x+y
print(*[sum(g(*x,p) for x in l) for p in [0,1]],sep='\n')

'''
for constants a,b,c,d,e,f find x,y s.t.

ax+by=c
dx+ey=f

so:
y=(c-ax)/b
y=(f-dx)/e
=>
(c-ax)/b=(f-dx)/e
e(c-ax)=b(f-dx)
ec-eax=bf-bdx
bdx-eax=bf-ec
x(bd-ea)=bf-ec
x=(bf-ec)/(bd-ea)
=>
y=(c-a((bf-ec)/(bd-ea)))/b

integar solutions when:
- (bd-ea)|(bf-ec)
- b|(c-a((bf-ec)/(bd-ea)))
'''
