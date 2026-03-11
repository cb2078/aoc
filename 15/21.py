W=[(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
A=[(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
R=[(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)];Rn=len(R)+1
b=[int(x.split(': ')[-1]) for x in open('21.txt').read().strip().split('\n')]
r=[float('inf'),0]
for i in range(Rn):
    for j in range(min(Rn-1,i+1),Rn):
        for w in W:
            for a in A+[(0,0,0)]:
                r0,r1=[R[k] if k<Rn-1 else (0,0,0) for k in [i,j]]
                p=[[100,0,0],b.copy()]
                g,*p[0][1:]=[w[i]+a[i]+r0[i]+r1[i] for i in range(3)]
                k=0
                while p[k][0]>0:
                    p[~k][0]-=max(p[k][1]-p[~k][2],1)
                    k^=1
                r[~k]=[max,min][k](g,r[~k])
print(*r,sep='\n')
