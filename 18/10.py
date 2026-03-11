import re;p=open('10.txt').read().strip().split('\n');p=[list(map(int,re.findall(r'(-?\d+)',l)))for l in p]
p,v=[[tuple(l[i:i+2]) for l in p] for i in [0,2]];n=len(p);xr=yr=None
def b():
    global xr,yr
    xmin=ymin=float('inf');xmax=ymax=float('inf')
    xr,yr=[[f(x[o]+i for x in p) for i,f in enumerate([min,max])] for o in [0,1]]
def op():print('\n'.join(''.join('.#'[(j,i) in p] for j in range(*xr)) for i in range(*yr)))
def t():global p;p=[tuple(p[k][i]+v[k][i] for i in range(2)) for k in range(n)];b()
b();i=0
while yr[1]-yr[0]>10:t();i+=1
op() # p1
print(i) # p2
