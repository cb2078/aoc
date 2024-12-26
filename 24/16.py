import heapq
m=open('16.txt').read().strip().split('\n')#;print(*m,sep='\n')
n=len(m);R=list(range(n));RR=[(i,j) for i in R for j in R]
D=[(0,1),(-1,0),(0,-1),(1,0)]
(si,sj),(ei,ej)=[(i,j) for c in 'SE' for i,j in RR if m[i][j]==c]

q=[(0,si,sj,0)];v={q[0][1:-1]};p={}
while q:
    x,i,j,d=heapq.heappop(q)
    if (i,j)==(ei,ej):break
    for dd in [-1,0,1]:
        di,dj=D[(d+dd)%4]
        if m[i+di][j+dj]=='#':continue
        if (i+di,j+dj) in v:continue
        v.add((i+di,j+dj))
        heapq.heappush(q,(x+abs(di+dj)+1000*abs(dd),i+di,j+dj,(d+dd)%4))
        p[i+di,j+dj]=i,j
else:raise

M=list(map(list,m))
i,j=p[ei,ej]
while (i,j) in p:I,J=p[i,j];M[i][j]='>^<v'[D.index((i-I,j-J))];i,j=I,J
# print('\n'.join(''.join(x) for x in M))
print(x)

from collections import defaultdict
xm=x;q=[(0,si,sj,0,[])];v=defaultdict(lambda:float('inf'));v[si,sj,0]=0;s=set()
while q:
    x,i,j,d,z=heapq.heappop(q)
    if x>xm:continue
    if (i,j)==(ei,ej):s|=set(z)
    for dd in [-1,0,1]:
        di,dj=(0,0) if dd else D[(d+dd)%4]
        if m[i+di][j+dj]=='#':continue
        X=x+abs(di+dj)+1000*abs(dd)
        k=i+di,j+dj,(d+dd)%4
        if X>v[k]:continue
        v[k]=X
        heapq.heappush(q,(X,*k,z+[(i,j)]))

# print('\n'.join(''.join('O' if (i,j) in s else m[i][j] for j in R) for i in R))
print(len(s)+1)
