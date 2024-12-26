s='XMAS';d=-1,0,1;m=open('04.txt').read().strip().split('\n');assert len(m)==len(m[0]);n=len(m)
f=lambda i,j,k,di,dj:k==4 or i+di*k in range(n) and j+dj*k in range(n) and m[i+di*k][j+dj*k]==s[k] and f(i,j,k+1,di,dj)
R=list(range(n));print(sum(f(i,j,0,di,dj) for i in R for j in R for di in d for dj in d if di or dj)) # p1
d=-1,1;a=lambda i,j:[m[i+di][j+dj] for di in d for dj in d]
x=lambda x:all({x[i],x[i-1]}==set('MS') for i in (0,2))
R=list(range(1,n-1));print(sum(m[i][j]=='A' and x(a(i,j)) for i in R for j in R)) # p2
