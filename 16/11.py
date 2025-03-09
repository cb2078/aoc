import re
f=[]
for i,s in enumerate(open('11.txt').read().strip().split('\n')):
    for x in re.findall(r'(\w+)(?:-compatible)? (generator|microchip)',s):
        f.append([*x,i])
f.sort()
f=[x[-1] for x in f]

g=lambda i,j:f[j]==i and j%2==0
m=lambda i,j:f[j]==i and j%2==1

gn=lambda i:sum(g(i,j) for j in r)
mn=lambda i:sum(m(i,j) for j in r)

o=lambda:print('\n'.join(' '.join('%d%s'%(j//2,'GM'[j%2]) if f[j]==3-k else '. ' for j in range(len(f)))+' %s'%' E'[3-k==i] for k in range(4)),end='\n\n\n')

def _(d,j,k):
    global i
    global z
    assert i<3 if d>0 else i>0
    f[j]+=d
    if k is not None:
        f[k]+=d
    i+=d
    z+=1
    # o()
u=lambda j,k=None:_(+1,j,k)
d=lambda j,k=None:_(-1,j,k)

t=lambda:i==I+1
b=lambda:i==I

for f in f,f[:]+[0]*4:
    n=len(f)
    r=*range(n),
    i=0
    I=0
    z=0
    while I<3:
        if b() and mn(i+1)==2:
            x=(j for j in r if m(i+1,j+1))
            j=next(x)
            k=next(x)
            u(j,k)
            u(j,k)
            d(j)
            u(j,j+1)
            d(k)
            d(k)
            j=next(j for j in r if g(i,j) and j!=k)
            u(j,k)
        elif b() and gn(i)==mn(i):
            x=(j for j in r if g(i,j))
            j=next(x)
            k=next(x)
            u(j,k)
            d(j)
            u(j,j+1)
        elif t() and gn(i)==mn(i)+1:
            j=next(j for j in r if g(i,j) and not m(i,j+1))
            d(j)
            if mn(i)==1:
                u(j,j+1)
            else:
                k=next(k for k in r if k!=j and g(i,k))
                u(j,k)
                d(j)
                u(j,j+1)
        else:
            raise
        if mn(I)==0 and gn(I)==0:
            I+=1
    print(z)
