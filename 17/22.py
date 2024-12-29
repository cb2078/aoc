s=open('22.txt').read().strip().split('\n')
sn=len(s)
d=[(-1,0),(0,1),(1,0),(0,-1)]
from collections import defaultdict

def f(O,n):
    def o():
        y0,y1,x0,x1=[f([i,j][k] for i,j in m if m[i,j]!='.')+y*3 for k in [0,1] for f,y in [(min,-1),(max,+1)]]
        print(*[''.join(('[' if (I,J//2)==(i,j-1) else ']' if (I,J//2)==(i,j) else ' ') if J%2 else m[I,J//2]
                        for J in range(2*x0,2*x1+2)) for I in range(y0,y1+1)],sep='\n',end='\n\n')

    m=defaultdict(lambda:'.')
    for i in range(sn):
        for j in range(sn):
            if s[i][j]=='#':
                m[i,j]='#'
    i,j=[sn//2]*2
    k=0
    r=0
    for _ in range(n):
        match m[i,j]:
            case '.':
                k-=1
            case 'W':
                pass
            case '#':
                k+=1
            case 'F':
                k+=2
            case _:
                raise
        m[i,j]=O[O.index(m[i,j])-1]
        r+=m[i,j]=='#'
        k%=4
        di,dj=d[k]
        i,j=i+di,j+dj
        # o()
    return r

print(f('#.',10000))
print(f('F#W.',10000000))
