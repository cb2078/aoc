import re
p=lambda _,a,b,c,d,e,f:[[a,0,0,0],[b,0,0,0],[c,d,0,0],[e,0,f,0]]
B=[p(*map(int,re.findall(r'\d+',x))) for x in open('19.txt').read().strip().split('\n')]
for z in 0,1:
  s=z
  for i,b in enumerate(B[:3] if z else B):
    x=0
    def f(a=[0,0,0,0],r=[1,0,0,0],t=[24,32][z]):
      g=lambda f:[*map(f,range(4))]
      global x
      if t==0:
        x=max(x,a[3])
        return
      elif a[3]+r[3]*t+(t-1)*t//2<x:
        return
      for j in range(4):
        if j>0 and r[j-1]==0 or j<3 and r[j]>=max(g(lambda i:b[i][j])):
          continue
        T=1+max(g(lambda i:b[j][i] and (b[j][i]-a[i]+r[i]-1)//r[i]))
        if T>t:
          x=max(x,a[3]+r[3]*t)
        else:
          f(g(lambda i:a[i]+r[i]*T-b[j][i]),g(lambda i:r[i]+(i==j)),t-T)
    f()
    s=s*x if z else s+(i+1)*x
  print(s)
