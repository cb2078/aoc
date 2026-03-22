for z in 1,4:
  m=open('18.txt').read().strip().split('\n')
  r=[(x,y) for x in range(len(m)) for y in range(len(m[0]))]
  if z==4:
    X,Y=next((x,y) for x,y in r if m[x][y]=='@')
    m=[['@#'[not x-X or not y-Y] if abs(x-X)<2 and abs(y-Y)<2 else m[x][y]for y in range(len(m[x]))] for x in range(len(m))]
  n=sum(m[x][y].islower() for x,y in r)
  f=lambda x:sum(1<<ord(y)-ord('a') for y in x)
  v=set()
  q=[(0,[(x,y) for x,y in r if m[x][y]=='@'],i,'') for i in range(z)]
  p=lambda s,a,i,k:(x:=(*a,i,f(k))) not in v and (v.add(x) or q.append((s,a,i,k)))
  while q:
    s,a,i,k=q.pop(0)
    if len(k)==n:
      print(s)
      break
    for x,y in ((a[i][0]+x,a[i][1]+y) for x in range(-1,2) for y in range(-1,2) if (x,y).count(0)==1):
      if m[x][y]=='#' or m[x][y].isupper() and m[x][y].lower() not in k:
        continue
      if m[x][y].islower() and m[x][y] not in k:
        for j in range(z):
          p(s+1,a[:i]+[(x,y)]+a[i+1:],j,k+m[x][y])
      else:
        p(s+1,a[:i]+[(x,y)]+a[i+1:],i,k)
