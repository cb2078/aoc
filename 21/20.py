a,b=open('20.txt').read().strip().split('\n\n')
b=b.split('\n')
d={(i,j):y for i,x in enumerate(b) for j,y in enumerate(x)}
p,q=0,len(b)
for t in range(50):
  g=lambda i,j:d[i,j] if (i,j) in d else '.#'[a[0]=='#' and t%2]
  f=lambda i,j:sum((g(x,y)=='#')<<8-k for k,(x,y) in enumerate((x,y) for x in range(i-1,i+2) for y in range(j-1,j+2)))
  p,q=p-1,q+1
  d={(i,j):a[f(i,j)] for i in range(p,q) for j in range(p,q)}
  if t+1 in (2,50):
    print(sum(d[i,j]=='#' for i in range(p,q) for j in range(p,q)))
