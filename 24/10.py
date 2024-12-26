from collections import defaultdict
m=[list(map(int,x)) for x in open('10.txt').read().strip().split('\n')];n=len(m)
R=list(range(n));RR=[(i,j) for i in R for j in R]
o=lambda x:print('\n'.join(''.join('%3d'%x[i][j] for j in R) for i in R))
def u(i,j,p):
    s=[(i,j)];v=defaultdict(int)
    while s:
        i,j=s.pop()
        v[i,j]+=1
        for di,dj in [(1,0),(0,1),(0,-1),(-1,0)]:
            if i+di not in R or j+dj not in R:continue
            if m[i+di][j+dj]-m[i][j]!=1:continue
            s.append((i+di,j+dj))
    return sum(v[i,j] if p==2 else 1 for i,j in v if m[i][j]==9)
print(*[sum(u(i,j,p) for i,j in RR if m[i][j]==0) for p in [1,2]],sep='\n')
