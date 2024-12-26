p=list(map(int,open('09.txt').read().strip()))
b=sum(([-1 if i%2 else i//2]*p[i] for i in range(len(p))),[])
f=[i for i in range(len(b)) if b[i]==-1]
while -1 in b:
    while b[-1]==-1:b.pop();f.pop()
    b[f.pop(0)]=b.pop()
print(sum(i*x for i,x in enumerate(b)))

b=[];a=0
for i in range(len(p)):b.append([a,p[i]]);a+=p[i]
for i in range(len(b)-1,-1,-2):
    for j in range(1,len(b),2):
        if b[j][0]<=b[i][0] and b[i][1]<=b[j][1]:
            b[i][0]=b[j][0] # move
            b[j][1]-=b[i][1] # decrease free space
            b[j][0]+=b[i][1] # move starting index
            break
print(sum((i+j)*k for k,(i,n) in enumerate(b[::2]) for j in range(n))) # <8570102309998
