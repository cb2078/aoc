l=open('12.txt').read().strip().split('\n')
e=lambda x:r[x] if x in 'abcd' else int(x)

for c in 0,1:
    r={x:0 for x in 'abcd'}
    r['c']=c
    i=0
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
            case _:
                raise
        i+=1
    print(r['a'])
