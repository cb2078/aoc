p=open('06.txt').read().strip().split('\n');p=[tuple(map(int,z.split(','))) for z in p]
d=lambda z,w:sum(abs(z[i]-w[i]) for i in range(2));dv=lambda z:[d(z,c) for c in p]
l,h=0,400;R=tuple(range(l,h));g=[[-2 for j in R] for i in R]
def p1():
    for i in R:
        for j in R:
            ds=dv((i,j));sds=sorted(ds)
            g[i][j]=min(list(range(len(p))),key=lambda i:ds[i]) if sds[0]!=sds[1] else -1
        # if i%100==0:print(i)
    # for i in R:
    #     for j in R:
    #         k=g[i][j];print(' ' if k==-2 else
    #                         '.' if k==-1 else
    #                         chr(ord('a')+k) if (i,j) not in p else
    #                         chr(ord('A')+k),end='')
    #     print()
    def a(i,j,k):
        s=[(i,j)];v=set()
        while s:
            i,j=s.pop();v.add((i,j))
            for di,dj in [(1,0),(-1,0),(0,-1),(0,1)]:
                if i+di not in R or j+dj not in R:return -1
                if (i+di,j+dj) in v or g[i+di][j+dj]!=k:continue
                s.append((i+di,j+dj))
        return len(v)
    print(max(a(i,j,k) for k,(i,j) in enumerate(p))) # p1
assert all(10000<=sum(dv((i,j)[::o])) for j in [l,h-1] for i in R for o in [1,-1])
def p2():
    s=0
    for i in R:
        for j in R:s+=10000>sum(dv((i,j)))
        # if i%100==0:print(i)
    print(s)
p1();p2()
