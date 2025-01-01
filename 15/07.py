import operator as op
from functools import cache

f={'NOT':op.invert,'AND':op.and_,'OR':op.or_,'LSHIFT':op.lshift,'RSHIFT':op.rshift}
p=dict(x.split(' -> ')[::-1] for x in open('07.txt').read().strip().split('\n'))

@cache
def e(x):
    if x not in p:return int(x)
    match p[x].split():
        case [x,o,y]:return f[o](e(x),e(y))
        case [o,x]:return f[o](e(x))
        case [x]:return e(x)
        case _:print(p[x]);raise

print(x:=e('a'));e.cache_clear();p['b']='%d'%x;print(e('a'))

