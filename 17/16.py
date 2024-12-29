p0=[*''.join(chr(ord('a')+i) for i in range(16))]
M=open('16.txt').read().strip().split(',')

def f(n):
    p=p0.copy()
    s=set()
    k=0
    while k<n:
        t=k%len(M),''.join(p)
        if t in s and n//k:
            k=n//k*k
        else:
            s.add(t)
        m=M[k%len(M)]
        match m[0]:
            case 's':
                i=int(m[1:])
                p=p[-i:]+p[:-i]
            case 'x':
                i,j=map(int,m[1:].split('/'))
                p[i],p[j]=p[j],p[i]
            case 'p':
                i,j=p.index(m[1]),p.index(m[3])
                p[i],p[j]=p[j],p[i]
            case _:
                raise
        k+=1
    return ''.join(p)

print(f(len(M)))
print(f(1000000000))
