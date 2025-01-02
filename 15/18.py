m=[[c=='#' for c in x] for x in open('18.txt').read().strip().split('\n')];n=len(m)
o=lambda:print('\n'.join(''.join('.#'[m[i][j]] for j in r) for i in r),end='\n\n')
d,r=[-1,0,1],[*range(n)]
f=lambda x,y:y in [2,3] if x else y==3

def s(m,t,p):
    def g(m):m[0][0]=m[0][-1]=m[-1][0]=m[-1][-1]=1
    if p==2:g(m)
    for _ in range(t):
        m=[[f(m[i][j],sum(m[i+di][j+dj] for di in d for dj in d if i+di in r and j+dj in r if di or dj))
            for j in range(n)] for i in range(n)]
        if p==2:g(m)
    return sum(map(sum,m))
for p in 1,2:print(s(m,100,p))
