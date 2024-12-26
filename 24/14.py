import re;p=[list(map(int,re.findall('-?\d+',x))) for x in open('14.txt').read().strip().split('\n')]
p,v=[[tuple(x[i:i+2]) for x in p] for i in [0,2]];w,h=101,103;wh=[w,h]
gm=lambda t:[tuple((p[i][j]+v[i][j]*t)%wh[j] for j in range(2)) for i in range(len(p))]
def s(t,p=True):m=gm(t);return '\n'.join(''.join(('#' if p else '%d'%k) if (k:=m.count((j,i))) else '. '[p] for j in range(w)) for i in range(h))
o=lambda t,p:print(s(t,p=False))
m=gm(100);P=1
for x in range(2):
    for y in range(2):
        sx,sy=x*(x+w//2),y*(y+h//2);P*=sum(m.count((sx+j,sy+i)) for i in range(h//2) for j in range(w//2))
print(P)

for t in range(10000):
    if '#########' in (m:=s(t)):print(t,m,sep='\n');break
