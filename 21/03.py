# pi=open('3.txt').read().split('\n')[:-1]
# pi=[[int(x) for x in y] for y in pi]
# w=len(pi[0]);h=len(pi)
# gr=[int(sum(pi[i][j] for i in range(h))/h*2) for j in range(w)]
# er=[not x for x in gr]
# a,b=(sum(_r[j]<<(w-j-1) for j in range(w)) for _r in (gr,er))
# print(a*b)
# print(gr,er)

p=open('03.txt').read().strip().split(('\n'))
n=len(p[0])
a=[int(x,2) for x in p]
f=lambda z,a,i:(sum(x>>n-1-i&1 for x in a)*2>=len(a))^z
g=lambda z:sum(f(z,a,i)<<n-1-i for i in range(n))
h=lambda z,a=a,i=0:a[0] if len(a)==1 else h(z,[x for x in a if x>>n-1-i&1==f(z,a,i)],i+1)
print(g(0)*g(1),h(0)*h(1),sep='\n')
