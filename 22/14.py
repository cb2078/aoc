p=open('14.txt').read().strip().split('\n')
p=[[list(map(int,y.split(','))) for y in x.split(' -> ')] for x in p]
ymax=2+1+max(x[1] for y in p for x in y)

g0=set()
for x in p:
    for k in range(len(x)-1):
        (a,b),(c,d)=x[k],x[k+1]
        for i in range(min(b,d),max(b,d)+1):
            for j in range(min(a,c),max(a,c)+1):
                g0|={(i,j)}

def pg():
    ymin,ymax,xmin,xmax=(f(x[i] for x in g) for i in range(2) for f in (min,max))
    print('\n'.join(''.join('#' if (i,j) in g0 else 'o' if (i,j) in g
                                               else '.'
                            for j in range(xmin,x1+max)) for i in range(ymin,y1+max)))

s=0,500
from itertools import count

g=g0.copy()
for n in count():
    i,j=s
    for i in range(ymax-2):
        if (i+1,j) not in g:
            continue
        elif (i+1,j-1) not in g:
            j-=1
        elif (i+1,j+1) not in g:
            j+=1
        else:
            break
    else:
        break
    g|={(i,j)}
# pg()
print(n) # 1

g=g0.copy()
for n in count():
    i,j=s
    for i in range(ymax-1):
        if (i+1,j) not in g:
            continue
        elif (i+1,j-1) not in g:
            j-=1
        elif (i+1,j+1) not in g:
            j+=1
        else:
            break
    if (i,j)==s:
        break
    g|={(i,j)}
# pg()
print(n+1) # 2
