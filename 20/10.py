l=list(map(int,open('10.txt').read().strip().split('\n')))
l.append(0)
l.append(max(l)+3)
l.sort()

x,y=[sum(y-x==d for x,y in zip(l,l[1:])) for d in [1,3]]
print(x*y)

from functools import cache
@cache
def f(x):
	if x not in l:
		return 0
	if x==l[-1]:
		return 1
	return f(x+1)+f(x+2)+f(x+3)
print(f(l[0]))
