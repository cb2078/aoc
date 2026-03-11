import heapq

m=open('23.txt').read().strip().split('\n')
m=m[:3]+'  #D#C#B#A#\n  #D#B#A#C#'.split('\n')+m[3:]
b=len(m)-3
a=[[0,i,j] for x in 'ABCD' for i in range(len(m)) for j in range(len(m[i])) if m[i][j]==x]
m=[''.join('.' if y in 'ABCD' else y for y in x) for x in m]
l=[(x,y) for x in range(len(m)) for y in range(len(m[x])) if m[x][y]=='.']
r=[[[x,y] for x in range(2,len(m)-1)] for y in range(3,11,2)]
o=lambda x,y:x==1 and y in range(3,11,2)
h=lambda x,y:x==1
t=lambda i:i//b
c=lambda a,i,x,y:any([x,y]==a[j][1:] for j in range(len(a)) if j!=i)

d={}
q=[]
def P(a):
  k=g=h=0
  for i,(e,x,y) in enumerate(a):
    k+=(1<<l.index((x,y)))*(1<<len(l))**t(i)
    g+=10**t(i)*e
    h+=10**t(i)*min(abs(x-X)+abs(y-Y) for X,Y in r[t(i)])
  if k not in d or g<d[k]:
    d[k]=g
    heapq.heappush(q,(g+h,g,a))

def p(a,i,e,x,y):
  if o(x,y) or\
      any([x,y] in r[T] for T in range(4) if t(i)!=T) or\
      [x,y] in r[t(i)] and any(a[j][1:] in r[t(i)] for j in range(len(a)) if t(i)!=t(j)):
    return
  P([*a[:i],[e,x,y],*a[i+1:]])

def n(a,i,e,x,y):
  s=[(e,x,y)]
  v={(x,y)}
  while s:
    e,x,y=s.pop()
    for X,Y in [x-1,y],[x+1,y],[x,y-1],[x,y+1]:
      if (X,Y) in v or m[X][Y]!='.' or c(a,i,X,Y):
        continue
      v.add((X,Y))
      s.append(l:=(e+1,X,Y))
      yield l

P(a)
while q:
  *_,a=heapq.heappop(q)
  # print(f'{len(q)} {len(d)}\n{_[0]} {_[1]}\n'+'\n'.join(''.join(
  #   next(('ABCD'[k//b] for k in range(len(a)) if a[k][1:]==[i,j]),m[i][j])
  #   for j in range(len(m[i]))) for i in range(len(m))),end='\n\n')
  if all([x,y] in r[t(i)] for i,(e,x,y) in enumerate(a)):
    break
  for i,(e,x,y) in enumerate(a):
    I=lambda x,y:r[t(i)].index([x,y]) if [x,y] in r[t(i)] else -1
    if (k:=I(x,y))==b-1 or any(k+1==I(x,y) for _,x,y in a[i//b*b:i//b*b+b]):
      continue
    if h(x,y):
      s={*n(a,i,e,x,y)}
      if (z:=next(((e,x,y) for j in range(b)[::-1] for e,x,y in s if r[t(i)][j]==[x,y]),None)) is not None:
        p(a,i,*z)
      continue
    for e,x,y in n(a,i,e,x,y):
      p(a,i,e,x,y)
