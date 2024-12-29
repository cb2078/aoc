p=[x.split() for x in open('18.txt').read().strip().split('\n')]
r={}
for i in range(len(p)):
    r[p[i][1]]=0
    if len(p[i])==2:
        p[i].append(None)

def f(i,r,b):
    s=[]
    g=lambda x:r[x] if x.isalpha() else int(x)
    while True:
        o,x,y=p[i]
        match o:
            case 'snd':
                s.append(g(x))
            case 'set':
                r[x]=g(y)
            case 'add':
                r[x]+=g(y)
            case 'mul':
                r[x]*=g(y)
            case 'mod':
                r[x]%=g(y)
            case 'rcv':
                if b:
                    r[x]=b.pop(0)
                else:
                    break
            case 'jgz':
                if g(x)>0:
                    i+=g(y)
                    continue
        i+=1
    return i,s

print(f(0,r,[])[1][-1])

R=[{k:0 for k in r},{k:k=='p' for k in r}]
b=[]
I=[0,0]
D=[False,False]
i=0
V=[0,0]
while True:
    I[i],b=f(I[i],R[i],b)
    V[i]+=len(b)
    i=~i
    D[i]=not b
    if all(D):
        break
    # print(b,V,*R,sep='\n',end='\n\n')
print(V[1])
