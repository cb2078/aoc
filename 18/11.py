def p(x,y,s):r=10+x;return r*(s+y*r)//100%10-5
# for x,y,s,e in [(3,5,8,4),(122,79,57,-5),(217,196,39,0),(101,153,71,4)]:print(r:=p(x,y,s),r==e)
g=[[p(1+x,1+y,1133)for x in range(300)] for y in range(300)]
s=lambda x,y,z:sum(g[i][j] for i in range(y,y+z) for j in range(x,x+z))
f=lambda z:max((s(x,y,z),x+1,y+1,z) for x in range(301-z) for y in range(301-z))
print(*f(3)[1:-1],sep=',') # p1
def S(x,y):
    if not y:print(x,end='\r')
    m=(float('-inf'),0);s=0
    for z in range(300-max(x,y)):
        s+=sum(g[y+z][x+i]+g[y+i][x+z] for i in range(z))+g[y+z][x+z];m=max(m,(s,1+z))
    return m
print(*max((*S(x,y),1+y,1+x) for x in range(300) for y in range(300))[1:][::-1],sep=',') # p2
