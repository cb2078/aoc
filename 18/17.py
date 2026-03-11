n=2200;g=[['.']*n for _ in range(n)]
for l in open('17.txt').read().strip().split('\n'):
    x,y=[z[2:] for z in l.split(', ')]
    x=range(int(x),int(x)+1)
    y0,y1=map(int,y.split('..'));y=range(y0,y1+1)
    if l.startswith('x'):x,y=y,x
    for i in x:
        for j in y:
            g[i][j]='#'
o=lambda:print('\n'.join('%4d: '%I+''.join('X' if (I,J)==(i,j) else g[I][J] for J in range(x0-9,x1+9)) for I in range(y1+9)),end='\n\n'*5)
y0,y1=[f(i for i in range(n) if any(g[i][j]=='#' for j in range(n))) for f in [min,max]]
x0,x1=[f(j for j in range(n) if any(g[i][j]=='#' for i in range(n))) for f in [min,max]]

def m(di,dj):global i;global j;i+=di;j+=dj;g[i][j]='|'
def f(i,j,d):return False if c(i+1,j) else f(i,j+d,d) if c(i,j+d) else True
def c(i,j):return i<=y1 and g[i][j] not in '#~'

s=[(0,500)];v=set(s)
while s:
    i,j=s.pop()
    if not c(i,j):continue
    while c(i+1,j):m(1,0)
    if i==y1:continue
    j0=j
    while f(i,j,-1) and f(i,j,1):
        for d in [-1,1]:
            while g[i][j]!='#':g[i][j]='~';j+=d
            j=j0
        i-=1
    for d in -1,1:
        while c(i,j+d):
            m(0,d)
            if c(i+1,j):
                if ((i,j)) not in v:v.add((i,j));s.append((i,j))
                break
for s in '~|','~':print(sum(g[i][j] in s for i in range(y0,y1+1) for j in range(n)))
