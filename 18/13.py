m=open('13.txt').read().rstrip().split('\n');w=max(len(r)for r in m);h=len(m)
for i in range(len(m)):m[i]+=' '*(w-len(m[i]))
d={'v':(1,0),'^':(-1,0),'<':(0,-1),'>':(0,1)};D={v:k for k,v in d.items()}
c=[[(i,j),d[m[i][j]],0] for i in range(h) for j in range(w) if m[i][j] in d] # ((i,j),dir,k%3)
for i in range(h):m[i]=m[i].replace('>','-').replace('v','|').replace('<','-').replace('^','|')
def p():
    M=[list(s) for s in m]
    for C in c:M[C[0][0]][C[0][1]]='X' if M[C[0][0]][C[0][1]] in d else D[C[1]]
    print('\n'.join(''.join(r) for r in M))
p1=p2=True
while p1 or p2:
    d=[]
    for i in range(len(c)):
        if i in d:continue
        assert m[c[i][0][0]][c[i][0][1]]!=' '
        c[i][0]=tuple(c[i][0][j]+c[i][1][j] for j in range(2))
        t=m[c[i][0][0]][c[i][0][1]]
        if t=='/':c[i][1]=(-c[i][1][1],-c[i][1][0])
        elif t=='\\':c[i][1]=c[i][1][::-1]
        elif t=='+':
            if c[i][2]==0:c[i][1]=(-c[i][1][1],c[i][1][0])#left
            elif c[i][2]==2:c[i][1]=(c[i][1][1],-c[i][1][0])#right
            c[i][2]=(c[i][2]+1)%3
        for j in range(len(c)):
            if i!=j and c[j][0]==c[i][0]:
                if p1:print(*c[i][0][::-1],sep=',');p1=False # p1
                d.append(i);d.append(j)
    assert all(d.count(i)==1 for i in d)
    d.sort(reverse=True)
    for i in d:del c[i]
    c.sort()#;p()
    if len(c)==1:print(*c[0][0][::-1],sep=',');p2=False # p2
# (76,99),(100,29)
# (43,80),(124,29)
