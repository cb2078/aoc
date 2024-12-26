g,m=open('15.txt').read().strip().split('\n\n');g=list(map(list,g.split('\n')));m=m.replace('\n','')
n=len(g);R=list(range(n));RR=[(i,j) for i in R for j in R]
w,r,o=[{i*1J+j for i,j in RR if g[i][j]==c} for c in '#@O'];r,=r
og=lambda:print('\n'.join(''.join('#' if i*1J+j in w else '@' if i*1J+j==r else 'O' if i*1J+j in o else '.' for j in R) for i in R))
D={'<':-1,'v':1j,'>':1,'^':-1j}

for c in m:
    d=D[c];r+=d
    if r in o:
        k=1
        while True:
            if r+d*k in o:k+=1;continue
            if r+d*k in w:r-=d
            else:o.remove(r);o.add(r+d*k)
            break
    elif r in w:r-=d
    # print(c);og();print()

print('%.0f'%sum(x.real+100*x.imag for x in o))

g=[['[]'[i] if y=='O' else '@.'[i] if y=='@' else  y for y in x for i in range(2)] for x in g]
i,j=[(i,j) for i in range(len(g)) for j in range(len(g[0])) if g[i][j]=='@'].pop();g[i][j]='.'
og=lambda r=True:print('\n'.join(''.join('@' if r and (i,j)==(I,J) else g[I][J] for J in range(len(g[0]))) for I in range(len(g))))
D={'<':(0,-1),'v':(1,0),'>':(0,1),'^':(-1,0)}

def f(i,j,di):
    def h(dj):
        if f(i+di,j,di) and f(i+di,j+dj,di):
            g[i+di][j],g[i][j]=g[i][j],g[i+di][j]
            g[i+di][j+dj],g[i][j+dj]=g[i][j+dj],g[i+di][j+dj]
            return True
        return False
    match g[i][j]:
        case '#':
            return False
        case '.':
            return True
        case '[':
            return h(1)
        case ']':
            return h(-1)
    raise

def F(i,j,dj):
    if g[i][j]=='.':
        return True
    if g[i][j]=='#':
        return False
    if F(i,j+dj,dj):
        g[i][j+dj],g[i][j]=g[i][j],g[i][j+dj]
        return True
    else:
        return False

from copy import deepcopy
for c in m:
    di,dj=D[c];i,j=i+di,j+dj;r=True
    if g[i][j] in '[]':
        G=deepcopy(g)
        if not (F(i,j,dj) if dj else f(i,j,di)):
            r=False
            g=G
            i,j=i-di,j-dj
    elif g[i][j]=='#':
        i,j=i-di,j-dj
    # print(c,r);og();print()

print(sum(100*i+j for i in range(len(g)) for j in range(len(g[0])) if g[i][j]=='[')) # 1534993<
