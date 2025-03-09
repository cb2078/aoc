l=open('25.txt').read().strip().split('\n')

def f(a):
    e=lambda x:r[x] if x in 'abcd' else int(x)
    r={x:0 for x in 'abcd'}
    r['a']=a
    i=0
    z=None
    n=0
    while i<len(l):
        match l[i].split():
            case ['cpy',x,y]:
                r[y]=e(x)
            case ['inc',x]:
                r[x]+=1
            case ['dec',x]:
                r[x]-=1
            case ['jnz',x,y]:
                if e(x):
                    i+=e(y)-1
            case ['out',x]:
                if z==e(x):
                    return 0
                elif n==1000:
                    return 1
                else:
                    n+=1
                    z=e(x)
            case _:
                raise
        i+=1

from itertools import count
for a in count():
    if f(a):
        break
print(a)
