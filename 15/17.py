b=[*map(int,open('17.txt').read().strip().split('\n'))];n=150

r=[]
q=[(n,0,())]
while q:
    n,i,p=q.pop()
    if n==0:
        r.append(p)
    elif i<len(b):
        q.append((n-b[i],i+1,(*p,b[i])))
        q.append((n,i+1,p))

m=min(map(len,r))
print(len(r),sum(len(x)==m for x in r),sep='\n')
