m=open('20.txt').read().rstrip().split('\n');w,h=max(map(len,m)),len(m)
b=lambda i,j:i<h and j<len(m[i])
l={(i+x*z,j+y*z):s for i in range(h) for j in range(len(m[i])) for x,y in ((0,1),(1,0))
   if b(i+x,j+y) and (s:=m[i][j]+m[i+x][j+y]).isalpha() for z in (-1,2) if b(i+x*z,j+y*z) and m[i+x*z][j+y*z]=='.'}
s,e=(next(k for k,v in l.items() if v==x) for x in ('AA','ZZ'))
p={k:K for k,v in l.items() for K,V in l.items() if v==V and k!=K}
o=lambda i,j:z and 1-(i in (2,h-3) or j in (2,w-3))*2

z=0;v=set();q=[(0,*s,0)]
while q:
  t,i,j,n=q.pop(0)
  if (i,j)==e and n==0:
    print(t)
    if not z:
      z=1;v=set();q=[(0,*s,0)]
      continue
    break
  if n<0 or (x:=(i,j,n)) in v:
    continue
  v.add(x)
  if (i,j) in p:
    q.append((t+1,*p[i,j],n+o(i,j)))
  for i,j in (i+1,j),(i,j+1),(i-1,j),(i,j-1):
    if m[i][j]=='.' and (i,j) not in v:
      q.append((t+1,i,j,n))


