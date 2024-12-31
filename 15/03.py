m={'<':-1,'>':1,'^':-1j,'v':1j}
p=[m[x] for x in open('03.txt').read().strip()]
from itertools import accumulate as acc
f=lambda x:{0}|set(acc(x))
print(len(f(p)))
print(len(f(p[::2])|f(p[1::2])))
