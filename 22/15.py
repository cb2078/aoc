import re
p=open('15.txt').read().strip().split('\n')
p=[[tuple(map(int,re.findall(r'[-\d]+',y))) for y in x.split(': ')] for x in p]

def f(y): # ranges of x given y
    r=set()
    for s,b in p:
        d=sum(abs(s[i]-b[i]) for i in range(2))    
        if (x:=d-abs(y-s[1]))>=0:
            r|={(s[0]-x,s[0]+x)}
    a=[]
    for l,h in sorted(r):
        if a and l-1<=a[-1][1]:
            a[-1][1]=max(a[-1][1],h)
        else:
            a+=[[l,h]]
    return a

print(sum(h-l for l,h in f(2000000))) # 1

for y in range(4000000):
    a=f(y)
    if len(a)!=1:
        assert len(a)==2 and a[1][0]-a[0][1]==2
        print(4000000*(a[0][1]+1)+y) # 2
        break
