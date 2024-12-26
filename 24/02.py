p=open('02.txt').read().strip().split('\n');p=[[int(x) for x in l.split()] for l in p]
s=lambda x:(x>0)-(x<0)
def f(x):n=len(x);y=[x[i]-x[i+1] for i in range(n-1)];return set(map(s,y)) in [{-1},{1}] and all(abs(z) in range(1,4) for z in y)
print(sum(map(f,p))) # p1
def g(x):n=len(x);return f(x) or any(f(x[:i]+x[1+i:]) for i in range(n))
print(sum(map(g,p))) # p2
