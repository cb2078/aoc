m=open('20.txt').read().strip().split('\n')
n=len(m);R=list(range(n));RR=[(i,j) for i in R for j in R]
(si,sj),(ei,ej)=([(i,j) for i,j in RR if m[i][j]==c].pop() for c in 'SE')

i,j=si,sj
d=0
v={(si,sj):0}
while (i,j)!=(ei,ej):
    for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if m[i][j]=='#':continue
        if (i,j) in v:continue
        d+=1
        v[i,j]=d
        break

f=lambda k:sum(v[i+di,j+dj]-v[i,j]-abs(di)-abs(dj)>=100
               for i,j in v for di in range(-k,k+1) for dj in range(-k,k+1)
               if abs(di)+abs(dj)<=k and (i+di,j+dj) in v)
print(f(2));print(f(20))
