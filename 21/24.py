import re,functools

a,b=zip(*(map(int,x)for x in re.findall(
  r'((?<=add x )-?\d+).*?((?<=add y )(?!1\b|25)\d+)',open('24.txt').read().strip(),re.S)))
k=26

for m in max,min:
  @functools.cache
  def f(z=0,i=len(a)-1):
    n=[]
    g=lambda z:n.append(x+[w]) if (x:=f(z,i-1) if i>0 else None if z else []) is not None else x
    r=lambda:range(1,10)
    if a[i]>0:
      if (w:=z%k-b[i]) in r():
        g(z//k)
    else:
      for w in r():
        g(z*k+w-a[i])
      if (w:=z%k-b[i]) in r():
        for c in range(k):
          if c!=w-a[i]:
            g(z//k*k+c)
    if n:
      return m(n)
  print(''.join(map(str,f())))
