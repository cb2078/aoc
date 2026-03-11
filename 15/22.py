import heapq
for z in [1,2]:
    p=[500,50,0,0,0] # mhdsr
    b=[int(x.split(': ')[-1]) for x in open('22.txt').read().strip().split('\n')]+[0] # hap
    q=[]
    v=set()
    def a(m,p,b,j):
        if (t:=(*p,*b,j)) not in v:
            v.add(t)
            heapq.heappush(q,(m,p,b,j))
    a(0,p,b,0)
    while q:
        M,P,B,j=t=heapq.heappop(q)
        P,B=P.copy(),B.copy()
        if B[0]<=0:
            print(M)
            break
        if z==2 and not j:
            P[1]-=1
        if P[1]<=0:
            continue
        B[0]-=B[2] and 3
        P[0]+=P[4] and 101
        P[2]=P[3] and 7
        for i in 3,4:
            P[i]=max(P[i]-1,0)
        B[2]=max(B[2]-1,0)
        if not j:
            for i,m in enumerate([53,73,113,173,229]):
                p,b=P.copy(),B.copy()
                if m>p[0]:
                    continue
                p[0]-=m
                match i:
                    case 0:
                        b[0]-=4
                    case 1:
                        b[0]-=2
                        p[1]+=2
                    case 2:
                        if p[3]:
                            continue
                        p[3]=6
                    case 3:
                        if b[2]:
                            continue
                        b[2]=6
                    case 4:
                        p[4]=5
                a(M+m,p,b,~j)
        else:
            P[1]-=max(1,B[1]-P[2])
            a(M,P,B,~j)
