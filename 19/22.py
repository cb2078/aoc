def f(i):
  for s in open('22.txt').read().strip().split('\n'):
    match s.split():
      case ['deal','into','new','stack']:
        i=~i%n
      case ['cut',x]:
        i=(i-int(x))%n
      case ['deal','with','increment',x]:
        i=i*int(x)%n
  return i

n=10007
print(f(2019))

def g(i,t):
  m,c=(f(1)-f(0))%n,f(0)
  while t:
    if t&1:
      i=(i*m+c)%n
    m,c=m*m%n,(m*c+c)%n
    t>>=1
  return i

n=119315717514047
t=101741582076661
print(g(2020,-t%(n-1)))
