import re,itertools

for b in itertools.count():
  u=[]
  for x in re.findall(r'(\d+).*?(\d+).*?(?:\((.*)\))? with.*?(\d+ \w+).*?(\d+)',open('24.txt').read()):
    y=[*map(int,x[:2]),[],[],(lambda x,y:[int(x),y])(*x[3].split()),int(x[4])]
    for s in x[2].split('; '):
      y[2+s.startswith('immune')]=s.split(' to ')[-1].split(', ')
    u.append(y)
  n=len(u)
  for i in range(n//2):
    u[i][4][0]+=b
  s={*range(n)}

  e=lambda i:u[i][0]*u[i][4][0]
  d=lambda i,j: e(i)*2 if (t:=u[i][4][1]) in u[j][2] else 0 if t in u[j][3] else e(i)

  v=set()
  while all(any(2*i//n==x for i in s) for x in (0,1)):
    if (x:=tuple(u[i][0] for i in s)) in v:
      break
    v.add(x)
    t={}
    for i in sorted(s,key=lambda i:((e(i),u[i][5])),reverse=True):
      j=next(filter(lambda j:2*i//n!=2*j//n and j not in t.values() and d(i,j),
                    sorted(s,key=lambda j:(d(i,j),e(j),u[j][5]),reverse=True)),None)
      if j is not None:
        t[i]=j
    for i in sorted(t,key=lambda i:u[i][5],reverse=True):
      u[t[i]][0]=max(0,u[t[i]][0]-d(i,t[i])//u[t[i]][1])
      if u[t[i]][0]<=0:
        s.remove(t[i])

  if (c:=all(i<n//2 for i in s)) or not b:
    print(sum(u[i][0] for i in s))
  if c:
    break
