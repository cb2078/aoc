l=open('21.txt').read().strip().split('\n')
p=list('abcdefgh')
n=len(p)

for s in l:
    match s.split():
        case ['swap', 'position', x, 'with', 'position', y]:
            i,j=int(x),int(y)
            p[i],p[j]=p[j],p[i]
        case ['swap', 'letter', x, 'with', 'letter', y]:
            i,j=p.index(x),p.index(y)
            p[i],p[j]=p[j],p[i]
        case ['rotate', z, x, 'steps' | 'step']:
            j=int(x)
            if z=='left':
                j=-j
            p=[p[(i-j)%n] for i in range(n)]
        case ['rotate', 'based', 'on', 'position', 'of', 'letter', x]:
            j=p.index(x)
            j=j+2 if j>=4 else j+1
            p=[p[(i-j)%n] for i in range(n)]
        case ['reverse', 'positions', x, 'through', y]:
            i,j=int(x),int(y)
            for k in range((1+j-i)//2):
                p[i+k],p[j-k]=p[j-k],p[i+k]
        case ['move', 'position', x, 'to', 'position', y]:
            i,j=int(x),int(y)
            p.insert(j,p.pop(i))
        case _:
            print(s)
            raise
print(''.join(p))

p=list('fbgdceah')
for s in l[::-1]:
    match s.split():
        case ['swap', 'position', x, 'with', 'position', y]:
            i,j=int(x),int(y)
            p[i],p[j]=p[j],p[i]
        case ['swap', 'letter', x, 'with', 'letter', y]:
            i,j=p.index(x),p.index(y)
            p[i],p[j]=p[j],p[i]
        case ['rotate', z, x, 'steps' | 'step']:
            j=int(x)
            if z=='left':
                j=-j
            p=[p[(i+j)%n] for i in range(n)]
        case ['rotate', 'based', 'on', 'position', 'of', 'letter', x]:
            t=[9,1,6,2,7,3,8,4]
            j=t[p.index(x)]
            p=[p[(i+j)%n] for i in range(n)]
        case ['reverse', 'positions', x, 'through', y]:
            i,j=int(x),int(y)
            for k in range((1+j-i)//2):
                p[i+k],p[j-k]=p[j-k],p[i+k]
        case ['move', 'position', x, 'to', 'position', y]:
            i,j=int(x),int(y)
            p.insert(i,p.pop(j))
        case _:
            print(s)
            raise
print(''.join(p))
