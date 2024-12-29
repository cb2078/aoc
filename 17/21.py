d={}
for l in open('21.txt').read().strip().split('\n'):
    x,y=l.split(' => ')
    X=[x.split('/')]
    n=len(X[0])
    for s in 'm[j][i] m[~i][j] m[i][~j]'.split():
        exec('X+=[[[%s for j in range(n)] for i in range(n)] for m in X]'%s)
    X=['/'.join(''.join(m[i][j] for j in range(n)) for i in range(n)) for m in X]
    for x in X:
        d[x]=y
# for x,y in d.items():
#     print(x,'=>',y)

h=lambda i,j,n:'/'.join(m[i+k][j:j+n] for k in range(n))
f=lambda i,j,n:d[h(i,j,n)].split('/')

for p in [5,18]:
    m='.#./..#/###'.split('/')
    N=3
    for k in range(p):
        n=[2,3][N%2]
        M=[[f(i,j,n) for j in range(0,N,n)] for i in range(0,N,n)]
        m=[''.join(M[I][J][i][j] for J in range(N//n) for j in range(n+1))
           for I in range(N//n) for i in range(n+1)]
        N=len(m)
        # print(N,*m,sep='\n',end='\n\n')
    print(sum(m[i][j]=='#' for i in range(N) for j in range(N)))
