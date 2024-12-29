g=[int(x.split()[-1]) for x in open('15.txt').read().strip().split('\n')]
g0=g.copy()
x=[16807,48271]
m=(1<<16)-1

r=0
for _ in range(4*10**7):
    for i in [0,1]:
        g[i]=g[i]*x[i]%2147483647
    r+=0==(g[0]^g[1])&m
print(r)

r=0
c=[3,7]
g=g0
for _ in range(5*10**6):
    for i in [0,1]:
        while True:
            g[i]=g[i]*x[i]%2147483647
            if g[i]&c[i]==0:
                break
    r+=0==(g[0]^g[1])&m
print(r)
