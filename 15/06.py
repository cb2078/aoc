import re
p=[[2 if 'toggle' in x else 'turn on' in x,*map(int,re.findall(r'\d+',x))] for x in open('06.txt').read().strip().split('\n')]
n=1000
def f(g):
    m=[[0]*n for _ in range(n)]
    for x,x0,y0,x1,y1 in p:
        for i in range(x0,x1+1):
            for j in range(y0,y1+1):
                m[i][j]=g(x,m[i][j])
    return sum(m[i][j] for i in range(n) for j in range(n))
print(f(lambda x,y:not y if x==2 else x))
print(f(lambda x,y:y+x if x else max(0,y-1)))
