p=open('21.txt').read().strip().split('\n')
p=[x.split() for x in p][::-1]
import operator as op
d = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.floordiv}
p={x[0][:-1]: int(x[1]) if len(x[1:]) == 1 else (x[1], d[x[2]], x[3]) for x in p}
f=lambda m: p[m] if type(p[m]) == int else p[m][1](f(p[m][0]), f(p[m][2]))
print(f('root')) # 1 

s=lambda m: s(p[m][0]) or s(p[m][2]) if type(p[m]) == tuple else m == 'humn'
i = (2, 0)[s(p['root'][0])]
x = f(p['root'][2 - i])
inv = {op.add:op.sub, op.sub:op.add, op.floordiv:op.mul, op.mul:op.floordiv}
def g(m, t):
    if m == 'humn':
        return t
    i = (2, 0)[s(p[m][0])] # child containin 'humn'
    y = f(p[m][2 - i])
    x = inv[p[m][1]](t, y) if i == 0 or p[m][1] in (op.add, op.mul) else p[m][1](y, t)
    return g(p[m][i], x)
print(g(p['root'][i], x)) # 2
