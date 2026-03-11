import re,functools as ft,heapq

D,X,Y=map(int,re.findall(r'\d+',open('22.txt').read()))
g=lambda x,y:0 if (x,y) in ((0,0),(X,Y)) else 16807*x if y==0 else 48271*y if x==0 else e(x-1,y)*e(x,y-1)
e=ft.cache(lambda x,y:(g(x,y)+D)%20183)
r=lambda x,y:e(x,y)%3
print(sum(r(x,y) for x in range(X+1) for y in range(Y+1)))

v={}
q=[]
def p(d,x,y,t):
 if ((x,y,t) in v and d>=v[x,y,t]) or x<0 or y<0 or t==r(x,y):
  return
 v[x,y,t]=d
 heapq.heappush(q,(abs(x-X)+abs(y-Y)+d,d,x,y,t))

p(0,0,0,1)
while q:
 _,d,x,y,t=heapq.heappop(q)
 if (x,y)==(X,Y) and t==1:
  print(d) #<1057
  break
 for i,j in (-1,0),(0,-1),(1,0),(0,1):
  p(d+1,x+i,y+j,t)
 p(d+7,x,y,3-t-r(x,y))
