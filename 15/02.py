p=[tuple(map(int,x.split('x'))) for x in open('02.txt').read().strip().split('\n')]
f=lambda x,y,z:(z*x,z*y,x*y);a=lambda x,y,z:2*sum(f(x,y,z))
print(sum(min(f(*x))+a(*x) for x in p))
r=lambda x:2*(sum(x)-max(x));b=lambda x,y,z:x*y*z
print(sum(r(x)+b(*x) for x in p))
