p=open('06.txt').read().strip().split('\n');n=len(p);R=list(range(n))
for i in R:
    if '^' in p[i]:g=i,p[i].index('^');break
o=lambda:print('\n'.join(''.join('X' if (i,j) in v else p[i][j] for j in R) for i in R))
i,j=g;v=set();d=[(-1,0),(0,1),(1,0),(0,-1)];dk=0;di,dj=d[dk]
while i in R and j in R:
    if p[i][j]=='#':i-=di;j-=dj;dk=(1+dk)%4;di,dj=d[dk]
    v.add((i,j));i+=di;j+=dj
print(len(v))

s=0;V=v-{g}
for o in V:
    i,j=g;v=set();d=[(-1,0),(0,1),(1,0),(0,-1)];k=0;di,dj=d[k]
    while i in R and j in R:
        if p[i][j]=='#' or (i,j)==o:i-=di;j-=dj;k=(1+k)%4;di,dj=d[k]
        if (i,j,k) in v:break
        v.add((i,j,k));i+=di;j+=dj
    else:
        continue
    s+=1
print(s)
