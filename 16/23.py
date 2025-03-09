l=open('23.txt').read().strip().split('\n')
n=len(l)
e=lambda x:r[x] if x in 'abcd' else int(x)

def f():
    global i
    r['d']=r['a']
    r['a']=r['b']*r['d']
    r['d']=0
    r['b']-=1
    r['c']=r['b']
    r['d']=r['c']
    r['c']+=r['d']
    r['d']=0
    while p[i][0]!='tgl':
        i+=1

for a in [7,12]:
    r={x:0 for x in 'abcd'}
    r['a']=a
    i=0
    p=[x.split() for x in l]
    while i<n:
        if i==2:
            f()
        match p[i]:
            case ['cpy',x,y]:
                r[y]=e(x)
            case ['inc',x]:
                r[x]+=1
            case ['dec',x]:
                r[x]-=1
            case ['jnz',x,y]:
                if e(x):
                    i+=e(y)-1
            case ['tgl',x]:
                j=i+e(x)
                if j in range(n):
                    match p[j]:
                        case [o,_]:
                            p[j][0]='dec' if o=='inc' else 'inc'
                        case [o,_,_]:
                            p[j][0]='cpy' if o=='jnz' else 'jnz'
                        case _:
                            raise
            case _:
                raise
        i+=1
    print(r['a'])
