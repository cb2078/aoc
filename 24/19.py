T,D=[x.split(c) for x,c in zip(open('19.txt').read().strip().split('\n\n'),[', ','\n'])]
from functools import cache
@cache
def f(d):return not d or sum(f(d[len(t):]) for t in T if d.startswith(t))
print(sum(f(d)>1 for d in D),sum(map(f,D)),sep='\n')
