p=open('04.txt').read().strip().split('\n')
p=[[list(map(int,y.split('-'))) for y in x.split(',')] for x in p]
f=lambda x,y:x[0]<=y[0] and x[1]>=y[1]
g=lambda f,x,y:f(x,y) or f(y,x)
print(sum(g(f,*x) for x in p)) # 1
h=lambda x,y:x[0]<=y[0]<=x[1]
print(sum(g(h,*x) for x in p)) # 2
