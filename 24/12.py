from collections import defaultdict
m=open('12.txt').read().strip().split('\n');n=len(m);R=list(range(n))
V={(i,j) for i in R for j in R}
def S(v): # get sides
    d=[-1,1]
    c=defaultdict(list) # number of squares touching each corner
    for i,j in v:
        for di in d:
            for dj in d:
                c[i+di/2,j+dj/2].append((di,dj))
    return sum(1 if len(c[i,j]) in [1,3] else 2 if len(c[i,j])==2 and all(c[i,j][0][k]!=c[i,j][1][k] for k in range(2)) else 0 for i,j in c)
pr=lambda v:print('\n'.join(''.join(m[i][j] if (i,j) in v else ' ' for i in R) for j in R if any((i,j) in v for i in R)))
def s(i,j):
    global V
    q=[(i,j)];v=set(q);a=e=0;
    while q:
        i,j=q.pop()
        V.remove((i,j))
        a+=1
        for di,dj in [(-1,0),(0,-1),(0,1),(1,0)]:
            if i+di not in R or j+dj not in R:continue
            if m[i+di][j+dj]!=m[i][j]:continue
            e+=1
            if (i+di,j+dj) in v:continue
            v.add((i+di,j+dj))
            q.append((i+di,j+dj))
    # pr(v)
    assert e%2==0
    return a,4*a-e,S(v)
p=[0,0]
while V:i,j=sorted(V)[0];x,y,z=s(i,j);p[0]+=x*y;p[1]+=x*z#;print('%2d %2d %3d'%(x,z,x*z),'\n')
print(*p,sep='\n') # 899811<p2
