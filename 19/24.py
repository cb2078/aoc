a={0:[[y=='#' for y in x] for x in open('24.txt').read().strip().split('\n')]}
d=(1,0),(0,1),(-1,0),(0,-1)
r=[(i,j) for i in range(5) for j in range(5)]
n=lambda i,j,k:sum(a[k][i+x][j+y] for x,y in d if (i+x,j+y) in r)
h=lambda:sum(a[0][i][j]<<i*5+j for i,j in r)
f=lambda i,j,k:(x:=n(i,j,k),x==1 if a[k][i][j] else x in (1,2))[1]
s=set()
while h() not in s:
  s.add(h())
  a[0]=[[f(i,j,0) for j in range(5)] for i in range(5)]
print(h())

e=[[0]*5 for _ in range(5)]
a={0:[[y=='#' for y in x] for x in open('24.txt').read().strip().split('\n')]}
g=lambda k,i,j:a[k][i][j] if k in a else 0
n=lambda i,j,k:sum(
  sum(g(k+1,min(x,0),z) if x else g(k+1,z,min(y,0)) for z in range(5)) if i+x==j+y==2
  else g(k,i+x,j+y) if (i+x,j+y) in r else g(k-1,x+2,y+2) for x,y in d)
for _ in range(200):
  a.update((k+o,e) for k,o in ((min(a),-1),(max(a),1)) if any(g(k,i,j) for i in range(5) for j in range(5)))
  a={k:[[not (i==j==2) and f(i,j,k) for j in range(5)] for i in range(5)] for k in a}
print(sum(g(k,i,j) for k in a for i,j in r))
