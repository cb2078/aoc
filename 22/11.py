p=open('11.txt').read().strip().split('\n\n')
p=[[y.strip() for y in x.split('\n')[1:]] for x in p]
m=[list(map(int,x[0].split(': ')[1].split(', '))) for x in p]
o=[eval('lambda old:'+x[1].split('= ')[1]) for x in p]
t=[[y.split()[-1] for y in x[-3:]] for x in p]
from math import lcm;b=lcm(*(int(x[0]) for x in t))
t=[eval(f'lambda x:[{f},{t}][0==x%{c}]') for c,t,f in t]
c=[0]*len(m)

for _ in range(10_000):
    for i in range(len(m)):
        c[i]+=len(m[i])
        for j in range(len(m[i])):
            m[i][j]=o[i](m[i][j]%b)#//3
            m[t[i](m[i][j])]+=[m[i][j]]
        m[i]=[]

x,y=sorted(c)[-2:];print(x*y) # 1,2
