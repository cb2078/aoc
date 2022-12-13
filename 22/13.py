p=open('13.txt').read().strip().split('\n\n')
p=[list(map(eval,x.split('\n'))) for x in p]

from itertools import zip_longest
def c(x,y):
    if type(x)==int and type(y)==int:
        return (y-x>0)-(y-x<0)
    elif type(x)==int:
        return c([x],y)
    elif type(y)==int:
        return c(x,[y])
    else:
        for xx,yy in zip_longest(x,y):
            if xx==None:
                return 1
            elif yy==None:
                return -1
            elif r:=c(xx,yy):
                return r
        return 0

# for i in range(len(p)):x,y=p[i];print(1+i,c(x,y))
print(sum(i+1 for i in range(len(p)) if c(*p[i])!=-1)) # 1

p=[x for y in p for x in y]+[[[2]],[[6]]]
from functools import cmp_to_key
r=sorted(p,key=cmp_to_key(c),reverse=True)
print((1+r.index([[2]]))*(1+r.index([[6]]))) # 2
