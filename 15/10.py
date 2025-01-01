X=[*map(int,open('10.txt').read().strip())]
for n in range(50):
    f=[]
    for x in X:
        if f and f[-1][1]==x:f[-1][0]+=1
        else:f.append([1,x])
    X=sum(f,[])
    if n==40:print(len(X))
print(len(X))
