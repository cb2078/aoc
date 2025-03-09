import re,math
v=lambda a,m:a**(m-2)%m
d=[[*map(int,re.search(r'(\d+) positions.*?(\d+)\.',s).group(1,2))] for s in open('15.txt').read().strip().split('\n')]
for d in d,d+[[11,0]]:
    m,a=map(list,zip(*d))
    r=*range(len(a)),
    for i in r:a[i]=-(a[i]+i+1)%m[i] # t+a+k=0 mod m => t=-a-k mod m
    X=[math.prod(m)//m[k] for k in r]
    print(sum(a[k]*X[k]*v(X[k],m[k]) for k in r)%math.prod(m))

